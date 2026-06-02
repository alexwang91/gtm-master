from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "artifacts" / "dry-runs" / "generic-hardware-s00-s08-s13-s14-report-state.json"
DEFAULT_OUTPUT = ROOT / "artifacts" / "dry-runs" / "generic-hardware-s00-s08-s13-s14-dashboard.html"
SYSTEM_SECTION_IDS = {"data_gap_panel", "citation_index"}


SECTION_TITLES = {
    "market_context": "市场与本地化前置判断",
    "jtbd_scenarios": "JTBD 场景与消费者声音",
    "message_architecture": "卖点、信息架构与证明链",
    "pricing": "开盘价格策略与利润边界",
    "copy_assets": "文案资产评分与测试队列",
    "creator_kol": "KOL 与创作者策略",
    "dtc_conversion": "DTC 转化与落地页诊断",
    "launch_forecast": "上市需求预测与投入产出假设",
    "activation_return_risk": "激活、退货与上手风险",
    "insight_guardrails": "洞察、健康、安全或高风险主张护栏",
    "subscription_churn": "订阅、留存与流失",
    "review_quality_feedback": "评论、售后与质量反馈闭环",
    "validation_roadmap": "验证路线图与实验优先级",
    "data_gap_panel": "关键待确认与置信度面板",
    "citation_index": "引用与证据索引",
}

STATUS_LABELS = {
    "rendered": "已渲染",
    "rendered_with_gaps": "已渲染，有缺口",
    "skipped": "已跳过",
    "skipped_not_triggered": "未触发，已跳过",
    "skipped_future_not_triggered": "未来模块，未触发",
    "pass": "通过",
    "pass_with_caveats": "通过，有注意事项",
    "hypothesis_only": "仅假设",
    "contract_ready": "契约就绪",
    "fixture_only": "样例数据",
    "available_fixture": "样例可用",
    "missing_real_evidence": "缺真实证据",
    "forbidden": "禁止",
}

TAKEAWAY_ZH = {
    "market_context": "市场与本地化判断应说明本地搜索词、渠道图、竞品种子、人群假设和证据限制如何影响上市打法。",
    "jtbd_scenarios": "消费者场景应把市场、人群、竞品和声音证据转成优先级任务、证明需求和不购买风险。",
    "message_architecture": "信息架构应把产品能力映射到人群任务、异议、证明需求和本地化信息路线；未提供可编辑文案时不生成最终广告文案。",
    "pricing": "价格判断应先说明开盘打法、上市价格架构、利润/收入边界和 30/60/90 价格路径；私密利润判断只通过本地工具展示。",
    "copy_assets": "文案资产部分只处理可编辑文字资产；没有文案输入时先给出资料清单、评分口径和测试队列。",
    "creator_kol": "KOL 与创作者部分应解释类型、选择理由、预算占比和预期结果范围；真实候选需要本地平台证据和品牌安全复核。",
    "dtc_conversion": "DTC/PDP 部分在上线前可用竞品页面、上一代页面和信息路线生成页面要求、摩擦风险和实验优先级。",
    "launch_forecast": "需求预测应定位为情景规划，避免把单点销量数字当作结论；它需要连接生命周期、MKT 投入、渠道准备度、转化假设和验证缺口。",
    "activation_return_risk": "激活与退货部分应把设置、兼容、预期落差、退货和售后摩擦转成上市前可预防动作。",
    "insight_guardrails": "敏感主张护栏用于划定可说、需证明和需避开的边界。",
    "subscription_churn": "订阅与留存部分用于判断价值驱动、留存风险和定价联动。",
    "review_quality_feedback": "评论、客服、退货、RMA 和净推荐相关数据应分流为产品质量问题、营销误解、渠道摩擦和下一代销售建议。",
    "validation_roadmap": "验证计划应把主张、价格、需求、渠道和证据限制转成分阶段测试，用来判断哪些事项应先测试再投入。",
    "data_gap_panel": "报告必须把未解决的关键待确认项作为正文展示，避免把关键不确定性藏在附录里。",
    "citation_index": "引用索引用来区分 dry-run 样例引用和真实证据，避免把 synthetic 内容误当成市场研究结论。",
}

FEATURE_ZH = {
    "Feature A improves one frequent user task with measurable daily convenience.": "Feature A：改善一个高频用户任务，并能用日常便利性指标衡量。",
    "Feature B reduces setup or onboarding friction.": "Feature B：降低设置、上手或 onboarding 摩擦。",
    "Feature C creates a visible design, durability, battery, comfort, or portability advantage.": "Feature C：形成可感知的设计、耐用、续航、舒适或便携优势。",
    "Measurable specification: one numeric performance or endurance metric is available.": "可量化规格：至少有一个性能或续航类数值指标。",
    "Setup constraint: one pairing, installation, sizing, network, or compatibility constraint may affect adoption.": "使用约束：配对、安装、尺寸、网络或兼容性约束可能影响采用。",
    "Privacy or safety caveat: user data, body contact, charging, children, elderly, or regulated-adjacent claims need proof before marketing.": "隐私/安全 caveat：用户数据、身体接触、充电、儿童、老人或监管相邻主张在营销前需要证明。",
}

SOURCE_LABELS = {
    "S01.build-consumer-market-map": "市场与本地化证据",
    "S02.mine-jtbd-scenarios": "JTBD 场景挖掘",
    "S03.match-messages-to-segments": "信息架构匹配",
    "S04.model-price-sensitivity": "开盘定价与利润边界",
    "S05.generate-copy-assets": "文案资产生成",
    "S05.score-creative-assets": "文案资产评分",
    "S06.rank-creators-kol": "KOL 与创作者排序",
    "S06.score-kol-fit": "KOL 与创作者策略",
    "S07.audit-dtc-conversion": "DTC 转化审计",
    "S07.predict-dtc-conversion": "DTC 转化规划",
    "S08.forecast-launch-demand": "上市需求预测",
    "S09.predict-activation-risk": "激活与退货风险",
    "S10.generate-health-insights": "主张与洞察护栏",
    "S11.predict-subscription-and-churn": "订阅与流失模型",
    "S12.mine-review-quality-feedback": "评论与质量反馈",
    "S13.plan-validation-experiments": "验证实验规划",
    "S14.compose-html-gtm-dashboard": "HTML 报告合成",
    "report_audit": "报告审计",
}

DISPLAY_ZH = {
    "GTM Master 试跑看板": "GTM Master GTM 报告",
    "dryrun-generic-hardware-s00-s08-s13-s14": "通用硬件报告样例",
    "dry-run fixture": "报告样例",
    "S00 -> S14 Golden Dry-run": "GTM 报告链路样例",
    "Generic Hardware Fixture": "通用硬件样例",
    "Example target country": "示例目标国家",
    "Example local currency price band": "示例本地价格段",
    "Input": "输入",
    "standard": "标准模式",
    "Hypothesis": "假设",
    "Needs Evidence": "需要证据",
    "Proof Gap": "证明缺口",
    "Private Inputs Withheld": "私密输入已隔离",
    "Validation Plan": "验证计划",
    "Transparent": "透明展示",
    "Fixture Only": "仅样例",
    "Local Tool": "本地工具",
    "Context Safety": "上下文安全",
    "Audit": "审计",
    "handoff only": "来源摘要",
    "module": "业务板块",
    "status": "状态",
    "source_skill": "来源板块",
    "source": "来源",
    "type": "类型",
    "used_by": "使用位置",
    "quality_label": "质量标签",
    "citation_id": "引用 ID",
    "gap_id": "缺口 ID",
    "gap": "缺口",
    "severity": "严重度",
    "recommended_resolution": "建议补齐方式",
    "blocks": "影响模块",
    "check": "检查项",
    "input": "输入项",
    "required": "是否必需",
    "output": "输出项",
    "included": "是否包含",
    "source_type": "来源类型",
    "collection_rule": "采集规则",
    "lookup_id": "查询 ID",
    "reason": "原因",
    "budget_item": "预算项",
    "used": "已用",
    "limit": "上限",
    "test": "测试",
    "skill_id": "来源 ID",
    "handoff": "来源摘要",
    "html_section": "HTML 区块",
    "quality_gate": "质量门禁",
    "reopen_conditions": "可重开条件",
    "product_capability": "产品能力",
    "category_driver": "品类驱动",
    "fit_score": "匹配分",
    "proof_readiness": "证明成熟度",
    "segment": "人群",
    "channel": "渠道",
    "job": "任务",
    "risk": "风险",
    "message_route": "信息路线",
    "feature": "功能",
    "benefit": "利益点",
    "required_proof": "所需证明",
    "proof_score": "证明分",
    "wtp_score": "支付意愿分",
    "price_sensitivity": "价格敏感度",
    "proof_dependency": "证明依赖度",
    "assumption": "假设",
    "test_feasibility": "测试可行性",
    "recommended_action": "建议动作",
    "phase": "阶段",
    "decision_unlocked": "解锁决策",
    "label": "标签",
    "value": "值",
    "status_panel": "状态面板",
    "ranked_bar": "排序条形图",
    "matrix_heatmap": "矩阵热力图",
    "range_chart": "区间图",
    "status panel": "状态面板",
    "ranked bar": "排序条形图",
    "matrix heatmap": "矩阵热力图",
    "range chart": "区间图",
    "evidence_collection_summary": "证据覆盖摘要",
    "category_selling_point_map": "品类卖点地图",
    "competitor_threat_scores": "竞品威胁评分",
    "segment_channel_touchpoint_map": "人群-渠道触点图",
    "local_channel_priority": "本地渠道优先级",
    "local_search_term_map": "本地搜索词地图",
    "competitor_candidate_scoring": "竞品候选评分",
    "local_voice_source_map": "本地声音来源地图",
    "top1_previous_generation_voice_scope": "TOP1与上一代声音范围",
    "bain_nss_journey_seed_panel": "贝恩旅程评分种子",
    "copy_input_coverage_gate": "文案输入覆盖门禁",
    "copy_message_fit_scorecard": "文案信息适配评分",
    "channel_copy_fit_matrix": "渠道文案适配矩阵",
    "copy_test_backlog": "文案测试队列",
    "creator_input_coverage_gate": "创作者输入覆盖门禁",
    "creator_archetype_fit_scorecard": "创作者类型适配评分",
    "creator_budget_expected_outcome": "创作者预算与预期结果",
    "brand_safety_disclosure_review": "品牌安全与披露风险",
    "conversion_input_coverage_gate": "转化输入覆盖门禁",
    "competitor_previous_page_benchmark": "竞品与上一代页面基准",
    "funnel_friction_scorecard": "转化摩擦评分",
    "page_experiment_plan": "页面实验计划",
    "activation_return_trigger_check": "激活与退货触发检查",
    "activation_journey_risk_map": "上手旅程风险图",
    "return_prevention_priority": "退货预防优先级",
    "insight_claim_trigger_check": "主张风险触发检查",
    "claim_guardrail_matrix": "主张护栏矩阵",
    "privacy_safety_proof_need": "隐私与安全证明需求",
    "subscription_retention_trigger_check": "订阅留存触发检查",
    "retention_value_driver_map": "留存价值驱动图",
    "churn_risk_priority": "流失风险优先级",
    "feedback_loop_trigger_check": "反馈闭环触发检查",
    "review_support_source_map": "评论与售后来源地图",
    "quality_feedback_priority": "质量反馈优先级",
    "feedback_loop_action_map": "反馈闭环动作图",
    "upstream_input_coverage_gate": "上游输入覆盖门禁",
    "scenario_priority_scorecard": "场景优先级评分卡",
    "product_job_fit_matrix": "产品-任务适配矩阵",
    "anti_jtbd_risk_list": "Anti-JTBD 风险清单",
    "segment_message_architecture": "人群信息架构",
    "feature_benefit_proof_matrix": "功能-利益-证明矩阵",
    "objection_matrix": "异议矩阵",
    "claim_risk_and_proof_gate": "主张风险与证明门禁",
    "local_price_credibility_model": "本地价格可信模型",
    "opening_price_strategy": "开盘价格策略",
    "opening_price_strategy.strategy_scores": "开盘策略评分",
    "launch_price_architecture": "上市价格架构",
    "opening_strategy_scorecard": "开盘策略适配度评分",
    "rapid_price_prior": "快速 WTP 先验",
    "rapid_price_prior.factor_scores": "快速 WTP 因子评分",
    "price_value_proof_matrix": "价格价值证明矩阵",
    "private_profit_revenue_optimizer_spec": "私密利润与收入优化器规格",
    "price_path_30_60_90": "30/60/90 价格路径",
    "segment_wtp_hypothesis": "人群支付意愿假设",
    "price_risk_guardrail": "价格风险护栏",
    "private_pricing_calculator_spec": "私密定价计算器规格",
    "forecast_input_coverage_gate": "预测输入覆盖门禁",
    "launch_scenario_forecast": "上市情景预测",
    "marketing_response_model": "营销响应模型",
    "channel_contribution_hypothesis": "渠道贡献假设",
    "forecast_sensitivity_risk": "预测敏感性风险",
    "validation_input_coverage_gate": "验证输入覆盖门禁",
    "experiment_priority_scorecard": "实验优先级评分卡",
    "assumption_risk_vs_test_feasibility": "假设风险与测试可行性",
    "timeline_and_decision_unlock_map": "时间线与决策解锁图",
    "validation_decision_gate": "验证决策门禁",
    "experiment_portfolio_by_module": "按业务问题聚合的实验组合",
    "data_gap_log": "关键待确认日志",
    "citation_index": "引用索引",
    "market_context": "市场与本地化",
    "jtbd_scenarios": "JTBD 场景",
    "message_architecture": "信息架构",
    "pricing": "定价",
    "launch_forecast": "上市预测",
    "validation_roadmap": "验证路线图",
    "data_gap_panel": "关键待确认面板",
    "citation_index": "引用索引",
    "copy_assets": "文案资产",
    "creator_kol": "KOL 与创作者",
    "dtc_conversion": "DTC 转化",
    "activation_return_risk": "激活与退货风险",
    "insight_guardrails": "洞察与主张护栏",
    "subscription_churn": "订阅与流失",
    "review_quality_feedback": "评论与质量反馈",
}

PHRASE_ZH = {
    "Dry-run has no live web collection.": "本样例未执行联网采集。",
    "Fixture scores are only contract placeholders.": "样例分数只用于验证报告结构，不代表真实市场判断。",
    "Real run must identify local ecommerce leaders first, then score competitors by visibility, price overlap, review volume, feature overlap, and decision substitution.": "真实运行时应先识别本地主要电商，再按可见度、价格重叠、评论量、功能重叠和决策替代性给竞品评分。",
    "Weak but commercially important segments stay as hypotheses with data gaps.": "弱证据但商业上重要的人群会保留为假设，并标记关键待确认。",
    "Real run should keep original voice atoms in local artifacts and pass only compressed clusters downstream.": "真实运行时应把原始消费者声音保存在本地 artifact，下游只接收压缩后的主题簇。",
    "Score combines job frequency, dissatisfaction, willingness to switch, product fit, proof readiness, and channel reach.": "评分综合任务频率、不满程度、切换意愿、产品适配、证明成熟度和渠道触达。",
    "Proof gaps are passed to S03 and S13.": "证明缺口会进入信息架构和后续验证计划。",
    "Anti-JTBD informs message proof, pricing risk, activation risk, and validation experiments.": "Anti-JTBD 会影响信息证明、定价风险、激活风险和验证实验。",
    "Dry-run routes are placeholders.": "样例中的信息路线只是占位。",
    "Proof requirements become S13 validation tasks.": "证明要求会转成后续验证任务。",
    "Objections should not be hidden; they become proof and test requirements.": "异议不应被隐藏，而应转成证明和测试要求。",
    "If regulated-adjacent claims appear, future S10 should be triggered.": "如果出现监管相邻主张，未来应触发主张护栏模块。",
    "Indexed dry-run values only; real run must use local currency and competitor anchors.": "这里只是样例指数值；真实报告必须使用本地货币和竞品价格锚点。",
    "WTP is a hypothesis until tested with survey, landing page, retail test, or channel signal.": "WTP 在通过问卷、落地页、零售测试或渠道信号验证前都只是消费者支付意愿假设。",
    "Jump-tier risk is kept even when primary target price band is clear.": "即使目标价格段清晰，也要保留消费者跳档决策风险。",
    "COGS means cost of goods sold; it should not be required for public research stages.": "COGS 指商品销售成本；公开研究阶段不应强制要求上传。",
    "Real run must ask for forecast horizon, channel plan, and marketing spend where available.": "真实运行应尽量询问预测周期、渠道计划和营销投入。",
    "Indexed demand only; do not interpret as units.": "这里只是需求指数，不能解释为销量单位。",
    "The model should expose assumptions instead of pretending precision.": "模型应暴露假设，避免伪装成精确预测。",
    "Carrier channel stays a hypothesis until commercial access is confirmed.": "运营商或捆绑渠道在商业准入确认前只保留为假设。",
    "These risks feed S13 validation priority.": "这些风险会进入后续验证优先级排序。",
    "No targeted lookup was executed in this dry-run.": "本样例未执行目标化查询。",
    "Priority combines decision impact, uncertainty, cost, speed, and downstream unlock value.": "优先级综合决策影响、不确定性、成本、速度和下游解锁价值。",
    "High-risk assumptions without feasible tests become executive decision caveats.": "高风险但难测试的假设会成为汇报中的决策限制。",
    "Timing is illustrative and should be resized by launch urgency.": "时间安排仅为示意，应按上市紧迫度调整。",
    "S13 should make blockers explicit instead of burying uncertainty.": "后续验证计划应明确展示阻塞项，避免掩盖不确定性。",
    "This lets the dashboard show which previous module creates the largest validation debt.": "这样报告可以显示哪个业务板块产生了最大的验证负债。",
    "Severity uses decision impact and downstream dependency.": "严重度按决策影响和下游依赖判断。",
    "Real report must replace fixture refs with source URLs, access dates, and evidence quality labels.": "真实报告必须用来源 URL、访问日期和证据质量标签替换样例引用。",
}

VALUE_ZH = {
    "fixture_only": "样例数据",
    "available_fixture": "样例可用",
    "missing_real_evidence": "缺真实证据",
    "requires_live_search": "需要联网搜索",
    "requires_trends_or_search_signals": "需要趋势或搜索信号",
    "recommended": "建议提供",
    "optional_private": "可选私密输入",
    "not_provided_in_fixture": "样例未提供",
    "hypothesis": "假设",
    "research_first": "先研究再决策",
    "not_started": "未开始",
    "local_only_blank_field": "本地空白字段",
    "excluded": "不嵌入",
    "forbidden": "禁止",
    "not_executed": "未执行",
    "high": "高",
    "medium": "中",
    "low": "低",
    "synthetic": "合成样例",
    "absent": "不存在",
    "not_real_evidence": "非真实证据",
    "synthetic_fixture": "合成样例",
    "True": "是",
    "False": "否",
    True: "是",
    False: "否",
    "daily convenience": "日常便利",
    "setup simplicity": "设置简单",
    "visible value": "可见价值",
    "Local ecommerce": "本地电商",
    "Consumer electronics retail": "消费电子零售",
    "Owned DTC": "自营 DTC",
    "Carrier or bundle channel": "运营商或捆绑渠道",
    "Feature A": "功能 A",
    "Feature B": "功能 B",
    "Feature C": "功能 C",
    "Segment A": "人群 A",
    "Segment B": "人群 B",
    "Job A": "任务 A",
    "Job B": "任务 B",
    "benefit-first": "利益优先",
    "friction-removal": "降低摩擦",
    "measurable before-after or benchmark": "前后对比或基准测试",
    "setup time and failure-rate evidence": "设置耗时与失败率证据",
    "claim needs evidence": "主张需要证据",
    "voice evidence missing": "缺少消费者声音证据",
    "needs_benchmark": "需要基准测试",
    "avoid_or_validate": "规避或验证",
    "needs_source": "需要来源",
    "needs_validation": "需要验证",
    "blocked_until_value_proof": "需价值证明后解锁",
    "blocked_until_wtp_signal": "需支付意愿信号后解锁",
    "blocked_until_channel_and_conversion_signal": "需渠道与转化信号后解锁",
    "test_before_message_lock": "信息锁定前测试",
    "test_before_channel_commit": "渠道承诺前测试",
    "partner_discovery": "伙伴可行性探索",
    "week 1": "第 1 周",
    "week 2": "第 2 周",
    "week 3": "第 3 周",
    "week 4": "第 4 周",
    "message route": "信息路线",
    "price corridor": "价格走廊",
    "channel priority": "渠道优先级",
    "go or revise": "推进或修订",
}

EXTRA_ZH = {
    "S05 is optional and should run only when user provides copy requirements, approved message routes, tone constraints, channel formats, or launch-material needs.": "S05 是可选模块；只有当用户提供文案需求、已批准的信息路线、品牌语气约束、渠道格式或上市素材需求时才运行。",
    "S06 is optional and should prioritize competitor KOL patterns, budget, expected reach or engagement, relevance rationale, and evidence quality when triggered.": "S06 是可选模块；触发后应优先分析竞品 KOL 模式、预算、预期触达或互动、匹配理由和证据质量。",
    "S07 is optional before launch; when there is no live page, it should use competitor pages, previous-generation pages, or user-provided text to generate recommendations.": "S07 在上市前是可选模块；如果没有真实页面，应基于竞品页面、上一代页面或用户提供的页面文字给出建议。",
    "Omitted because the product fixture does not trigger setup, sizing, installation, app pairing, or return-risk analysis beyond S04/S08 caveats.": "本样例未触发激活、尺寸、安装、App 配对或退货风险分析；相关风险只保留在 S04/S08 的 caveat 中。",
    "Omitted unless the product or messages include regulated-adjacent, health, safety, AI insight, children, elderly, or sensitive claims.": "仅当产品或信息包含监管相邻、健康、安全、AI 洞察、儿童、老人或敏感主张时才启用。",
    "Omitted unless the product has subscription, paid app, consumable, warranty, service plan, or recurring retention economics.": "仅当产品包含订阅、付费 App、耗材、延保、服务计划或持续留存经济模型时才启用。",
    "Omitted before launch unless the user provides post-launch reviews, support tickets, RMA, returns, NSS/NPS, or app-store review data.": "上市前默认省略；除非用户提供上市后评论、客服工单、RMA、退货、NSS/NPS 或应用商店评论数据。",
    "Direct competitor type A": "直接竞品类型 A",
    "Direct competitor type B": "直接竞品类型 B",
    "Adjacent substitute type C": "相邻替代品类型 C",
    "Lower price jump-down option": "低价跳档备选",
    "Higher price jump-up option": "高价跳档备选",
    "local ecommerce discovery": "本地电商识别",
    "local forum and video source discovery": "本地论坛与视频来源识别",
    "local language search term expansion": "本地语言搜索词扩展",
    "real_local_ecommerce_leader_list": "真实本地头部电商名单",
    "real_local_search_terms": "真实本地搜索词",
    "real_competitor_review_and_price_evidence": "真实竞品评论与价格证据",
    "real_forum_or_video_voice_atoms": "真实论坛或视频消费者声音原子",
    "S01 segment seeds": "S01 人群种子",
    "voice atoms": "消费者声音原子",
    "competitor and substitute map": "竞品与替代品地图",
    "Scenario A: frequent daily trigger": "场景 A：高频日常触发",
    "Scenario B: proof-heavy premium trigger": "场景 B：强证明驱动的高价触发",
    "Scenario C: setup-friction avoidance": "场景 C：规避设置摩擦",
    "I do not trust the promised benefit": "我不相信承诺的利益点",
    "I can solve it with an existing device": "我可以用已有设备解决",
    "Setup or compatibility feels risky": "设置或兼容性看起来有风险",
    "local forum": "本地论坛",
    "discover country-category forums, preserve source URL and language": "发现目标国家和品类论坛，并保留来源 URL 与语言",
    "video comments": "视频评论",
    "collect public comments only where access and policy allow": "仅在访问权限和平台政策允许时采集公开评论",
    "retailer reviews": "零售商评论",
    "sample by competitor, price tier, and review recency": "按竞品、价格档位和评论时间抽样",
    "voice_atom_corpus": "消费者声音原子语料库",
    "language_specific_phrases": "本地语言特有表达",
    "forum_source_accessibility_check": "论坛来源可访问性检查",
    "competitor_previous_generation_reviews": "竞品或上一代产品评论",
    "lower setup friction": "降低设置摩擦",
    "benefit not credible": "利益点可信度不足",
    "price feels high without proof": "缺少证明时价格显得偏高",
    "setup or compatibility anxiety": "设置或兼容性焦虑",
    "performance claim": "性能主张",
    "needs benchmark": "需要基准测试",
    "wellness or safety-adjacent claim": "健康或安全相邻主张",
    "avoid or validate": "规避或验证",
    "competitive superiority claim": "相对竞品优势主张",
    "needs source": "需要来源",
    "message architecture": "信息架构",
    "final ad copy": "最终广告文案",
    "image or creative asset generation": "图片或创意资产生成",
    "local_language_message_terms": "本地语言信息表达",
    "claim_evidence_sources": "主张证据来源",
    "objection_voice_atoms": "异议声音原子",
    "target indexed band": "目标指数价格带",
    "jump-down watch zone": "低价跳档观察区",
    "jump-up premium zone": "高价跳档观察区",
    "value proof below price expectation": "价值证明低于价格预期",
    "channel margin unknown": "渠道毛利未知",
    "consumer jump to adjacent price tier": "消费者跳到相邻价格档位",
    "COGS input": "销售成本输入",
    "local only blank field": "仅本地空白字段",
    "gross margin target": "目标毛利率",
    "channel policy": "渠道政策",
    "raw private values in report state": "报告状态中的原始私密值",
    "best_for": "适用场景",
    "survey or conjoint-lite": "问卷或轻量联合分析",
    "early WTP and feature tradeoff": "早期支付意愿与功能取舍",
    "landing page price test": "落地页价格测试",
    "traffic to intent signal": "从流量观察意向信号",
    "local retail or ecommerce pilot": "本地零售或电商小规模试点",
    "real conversion and channel feasibility": "真实转化与渠道可行性",
    "real_competitor_price_anchors": "真实竞品价格锚点",
    "channel_margin_terms": "渠道毛利条款",
    "cogs_or_bom_inputs": "销售成本或物料成本输入",
    "validated_wtp_evidence": "已验证支付意愿证据",
    "Scenario": "情景",
    "market size seed": "市场规模种子",
    "marketing budget": "营销预算",
    "not provided in fixture": "样例未提供",
    "channel readiness": "渠道准备度",
    "conversion assumptions": "转化假设",
    "30 day demand index": "30 天需求指数",
    "60 day demand index": "60 天需求指数",
    "90 day demand index": "90 天需求指数",
    "expected_effect": "预期效果",
    "confidence": "置信度",
    "dependency": "依赖条件",
    "paid media": "付费媒体",
    "traffic lift": "流量提升",
    "creative proof": "创意证明",
    "retail feature placement": "零售资源位",
    "conversion lift": "转化提升",
    "channel access": "渠道准入",
    "creator content": "创作者内容",
    "trust and consideration": "信任与考虑度",
    "S06 trigger": "S06 触发条件",
    "market size evidence missing": "缺少市场规模证据",
    "price proof weak": "价格证明偏弱",
    "channel readiness uncertain": "渠道准备度不确定",
    "creative or proof not validated": "创意或证明未验证",
    "forecast horizon": "预测周期",
    "marketing spend by channel": "按渠道拆分的营销投入",
    "channel launch plan": "渠道上市计划",
    "previous-generation sales curve": "上一代销量曲线",
    "market_size_seed": "市场规模种子",
    "channel_launch_commitment": "渠道上市承诺",
    "marketing_budget_by_channel": "按渠道拆分的营销预算",
    "conversion_rate_benchmarks": "转化率基准",
    "previous_generation_sales_curve": "上一代销量曲线",
    "S01 market evidence": "S01 市场证据",
    "S02 JTBD proof gaps": "S02 JTBD 证明缺口",
    "S03 claim risks": "S03 主张风险",
    "S04 price assumptions": "S04 价格假设",
    "S08 forecast assumptions": "S08 预测假设",
    "value proof benchmark test": "价值证明基准测试",
    "price corridor and WTP test": "价格走廊与支付意愿测试",
    "local search term and message smoke test": "本地搜索词与信息冒烟测试",
    "retail channel feasibility interview": "零售渠道可行性访谈",
    "setup friction usability test": "设置摩擦可用性测试",
    "benefit claim is credible": "利益点主张可信",
    "target price is acceptable": "目标价格可接受",
    "local channel can create reach": "本地渠道能形成触达",
    "local language search and message smoke test": "本地语言搜索与信息冒烟测试",
    "price corridor survey or landing page split": "价格走廊问卷或落地页分流测试",
    "retail or channel feasibility check": "零售或渠道可行性检查",
    "integrated launch forecast refresh": "整合上市预测刷新",
    "launch message lock": "上市信息锁定",
    "blocked until value proof": "需价值证明后解锁",
    "price lock": "价格锁定",
    "blocked until wtp signal": "需支付意愿信号后解锁",
    "forecast confidence upgrade": "预测置信度升级",
    "blocked until channel and conversion signal": "需渠道与转化信号后解锁",
    "S04 pricing": "S04 定价",
    "S03 message proof": "S03 信息证明",
    "S08 forecast": "S08 预测",
    "S02 JTBD voice": "S02 JTBD 声音",
    "none": "无",
    "no_live_web_for_dry_run": "dry-run 不执行联网搜索",
    "upstream_full_artifact_opening": "打开上游完整 artifact",
    "targeted_lookup": "目标化查询",
    "main_visual_blocks": "主要可视化块",
    "real paid media A/B": "真实付费媒体 A/B 测试",
    "requires live budget and campaign assets": "需要真实预算与投放素材",
    "retailer pilot": "零售商试点",
    "requires commercial access": "需要商业准入",
    "large-scale survey": "大规模问卷",
    "out of dry-run scope": "超出 dry-run 范围",
    "validated_claim_benchmarks": "已验证主张基准",
    "real_price_test_results": "真实价格测试结果",
    "channel_feasibility_signal": "渠道可行性信号",
    "local_language_search_signal": "本地语言搜索信号",
    "conversion_benchmark": "转化基准",
    "market and competitor evidence": "市场与竞品证据",
    "voice atoms and JTBD source corpus": "消费者声音原子与 JTBD 来源语料",
    "pricing and WTP validation": "定价与支付意愿验证",
    "channel readiness and conversion assumptions": "渠道准备度与转化假设",
    "Real local ecommerce, retailer, forum, video, and search-term discovery was not run.": "未运行真实本地电商、零售商、论坛、视频和搜索词发现。",
    "Run S01 with live web MCP search under the target country and category.": "在目标国家和品类下，用联网搜索补齐本地市场证据。",
    "No real consumer voice atoms, local language phrases, NSS/NPS, reviews, or forum comments are present.": "当前没有真实消费者声音原子、本地语言表达、NSS/NPS、评论或论坛留言。",
    "Collect public reviews, local forum posts, video comments, and optional private NSS/NPS material.": "采集公开评论、本地论坛帖子、视频评论，并可选加入私密 NSS/NPS 材料。",
    "No real price anchors, COGS, gross margin, channel policy, WTP evidence, or channel terms are embedded.": "当前未嵌入真实价格锚点、销售成本、毛利、渠道政策、支付意愿证据或渠道条款。",
    "Use public competitor price evidence plus optional local-only private calculator inputs.": "使用公开竞品价格证据，并可选使用仅本地计算的私密输入。",
    "No market size seed, budget-by-channel, conversion benchmark, channel commitment, or previous-generation sales curve is available.": "当前缺少市场规模种子、按渠道拆分预算、转化基准、渠道承诺或上一代销量曲线。",
    "Ask user for forecast horizon, marketing spend, channel plan, and optional previous-generation data.": "向用户索取预测周期、营销投入、渠道计划，以及可选的上一代产品数据。",
    "Validation roadmap is generated from dry-run assumptions, not executed tests.": "验证路线图来自样例假设，尚未接入已执行测试结果。",
    "go_no_go_confidence": "是否推进的置信度",
    "Run targeted validation tests and update S13 with actual results.": "运行目标化验证测试，并用真实结果更新后续验证计划。",
    "fixture citations": "样例引用",
    "live citations": "真实引用",
    "source confidence": "来源置信度",
    "handoff": "来源摘要",
    "isolated_with_gaps": "已记录，仍有缺口",
    "pass_with_caveats": "通过，有注意事项",
    "suite routing failure; missing required module trigger decision": "套件路由失败；缺少必需模块触发决策",
    "competitor source challenge; missing local channel source; market map contradiction": "竞品来源质疑；缺少本地渠道来源；市场地图出现矛盾",
    "voice source audit; JTBD cluster dispute; local phrase translation challenge": "声音来源审计；JTBD 簇争议；本地表达翻译质疑",
    "claim legality or proof challenge; copy generation trigger; segment-message mismatch": "主张合法性或证明质疑；触发文案生成；人群与信息不匹配",
    "private calculator audit; price anchor dispute; channel margin scenario needed": "私密计算器审计；价格锚点争议；需要渠道毛利情景",
    "user requests copy assets; approved claims and brand tone are provided": "用户请求文案资产；已提供批准主张和品牌语气",
    "user asks for KOL plan; marketing budget and target platform are provided; competitor creator activity is available": "用户要求 KOL 计划；已提供营销预算和目标平台；可获得竞品创作者活动",
    "landing page text or URL is provided; competitor page benchmark requested; previous-generation page material provided": "已提供落地页文字或 URL；要求竞品页面基准；已提供上一代页面材料",
    "forecast assumption challenge; new marketing budget; new channel commitment; private previous-generation data provided": "预测假设被质疑；出现新营销预算；出现新渠道承诺；提供了私密上一代数据",
    "validation priority dispute; targeted lookup escalation approved; new private experiment result provided": "验证优先级争议；批准目标化查询升级；提供了新的私密实验结果",
    "visual block rendering failure; citation mismatch; section omitted despite trigger": "可视化块渲染失败；引用不匹配；已触发模块却被省略",
    "competitor_selection": "竞品选择",
    "message_localization": "信息本地化",
}


TERM_REPLACEMENTS = (
    ("管理层摘要", "GTM判断"),
    ("给管理层的摘要", "GTM判断"),
    ("post-skill isolation", "来源治理"),
    ("Post-skill", "来源治理"),
    ("post-skill", "来源治理"),
    ("section drafts", "区块草稿"),
    ("section draft", "区块草稿"),
    ("section", "区块"),
    ("handoff refs", "来源摘要引用"),
    ("handoff", "来源摘要"),
    ("data gap", "关键待确认"),
    ("citations", "引用"),
    ("citation", "引用"),
    ("dry-run", "样例"),
    ("Dry-run", "样例"),
    ("full artifact", "完整产物"),
    ("fixture", "样例"),
    ("artifact", "产物"),
    ("synthetic", "合成样例"),
    ("caveat", "注意事项"),
    ("onboarding", "上手流程"),
    ("Feature A", "功能 A"),
    ("Feature B", "功能 B"),
    ("Feature C", "功能 C"),
    ("App", "应用"),
    ("S14", "最终看板合成器"),
    ("S13", "后续验证计划"),
    ("S12", "后续反馈闭环"),
    ("S11", "后续留存模型"),
    ("S10", "后续主张护栏"),
    ("refs", "引用"),
)


def soften_report_tone(text: str) -> str:
    text = re.sub(r"不是([^。；\n]{1,60}?)[，,、\s]*而是", r"不宜理解为\1；重点在于", text)
    text = text.replace("而不是", "，避免仅停留在")
    return text


def normalize_terms(value: Any) -> str:
    text = str(value)
    if "://" in text:
        return text
    for source, target in TERM_REPLACEMENTS:
        text = text.replace(source, target)
    return soften_report_tone(text)


def display_value(value: Any) -> Any:
    if value is None:
        return ""
    if isinstance(value, list):
        return "；".join(str(display_value(item)) for item in value)
    if isinstance(value, dict):
        return json.dumps({str(display_value(k)): display_value(v) for k, v in value.items()}, ensure_ascii=False)
    if value in VALUE_ZH:
        return VALUE_ZH[value]
    text = str(value)
    if text in SOURCE_LABELS:
        return normalize_terms(SOURCE_LABELS[text])
    if text in DISPLAY_ZH:
        return normalize_terms(DISPLAY_ZH[text])
    if text in PHRASE_ZH:
        return normalize_terms(PHRASE_ZH[text])
    if text in EXTRA_ZH:
        return normalize_terms(EXTRA_ZH[text])
    return normalize_terms(text)

def desc(section: dict[str, Any]) -> str:
    return str(display_value(section.get("source_skill") or ""))


def esc(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=False)
    return html.escape(str(value), quote=True)


def d(value: Any) -> str:
    return esc(display_value(value))


def slug(value: Any) -> str:
    text = str(value or "section").lower()
    text = re.sub(r"[^\w\u4e00-\u9fff]+", "_", text, flags=re.UNICODE)
    return text.strip("_") or "section"


def label(value: Any) -> str:
    text = str(value or "")
    return STATUS_LABELS.get(text, text.replace("_", " "))


def number(value: Any, default: float = 0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def percent(value: Any, minimum: Any = 0, maximum: Any = 100) -> str:
    low = number(minimum, 0)
    high = number(maximum, 100)
    span = high - low or 1
    raw = (number(value, low) - low) / span
    return f"{max(0, min(100, raw * 100)):.1f}%"


def first_sentence(value: str, limit: int = 140) -> str:
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"


def display_takeaway(section: dict[str, Any]) -> str:
    section_id = str(section.get("section_id") or "")
    return TAKEAWAY_ZH.get(section_id, section.get("executive_takeaway") or "")


def display_feature(item: Any) -> Any:
    if isinstance(item, str):
        return FEATURE_ZH.get(item, item)
    return item


def row_value(row: dict[str, Any], column: str) -> Any:
    if column in row:
        return row[column]
    key = slug(column)
    return row.get(key, "")


def headers_from_rows(rows: list[Any]) -> list[str]:
    for row in rows:
        if isinstance(row, dict):
            keys = list(row.keys())
            return keys[:8]
        if isinstance(row, list):
            return [f"列 {index + 1}" for index in range(len(row))]
    return []


def render_badge(status: Any) -> str:
    raw = str(status or "unknown")
    return f'<span class="badge {esc(slug(raw))}">{d(label(raw))}</span>'


def render_list(items: list[Any]) -> str:
    if not items:
        return '<p class="muted">未提供。</p>'
    parts = []
    for item in items:
        if isinstance(item, dict):
            title = item.get("label") or item.get("title") or item.get("gap") or item.get("decision") or item.get("item")
            note = item.get("reason") or item.get("note") or item.get("recommended_resolution") or item.get("status")
            parts.append(
                "<li>"
                f"<strong>{d(title)}</strong>"
                + (f"<span>{d(note)}</span>" if note else "")
                + "</li>"
            )
        else:
            parts.append(f"<li>{d(item)}</li>")
    return '<ul class="clean-list">' + "".join(parts) + "</ul>"


def render_table(title: str, rows: list[Any], headers: list[str] | None = None) -> str:
    if not rows:
        return ""
    headers = headers or headers_from_rows(rows)
    if not headers:
        return ""
    body_rows = []
    for row in rows:
        if isinstance(row, dict):
            cells = [row_value(row, header) for header in headers]
        elif isinstance(row, list):
            cells = row
        else:
            cells = [row]
        body_rows.append("<tr>" + "".join(f"<td>{d(cell)}</td>" for cell in cells) + "</tr>")
    return (
        '<div class="table-block">'
        f"<h4>{d(title)}</h4>"
        '<div class="table-scroll"><table><thead><tr>'
        + "".join(f"<th>{d(header)}</th>" for header in headers)
        + "</tr></thead><tbody>"
        + "".join(body_rows)
        + "</tbody></table></div></div>"
    )


def table_rows_from_ref(table: dict[str, Any], report_state: dict[str, Any]) -> list[Any]:
    ref = table.get("rows_ref")
    if ref and isinstance(report_state.get(ref), list):
        return report_state[ref]
    return table.get("rows") or []


def render_tables(tables: list[dict[str, Any]], report_state: dict[str, Any]) -> str:
    parts = []
    for table in tables or []:
        rows = table_rows_from_ref(table, report_state)
        headers = table.get("headers")
        title = table.get("title") or table.get("table_id") or "表格"
        parts.append(render_table(str(title), rows, headers))
    return "".join(parts)


def render_visual_header(block: dict[str, Any]) -> str:
    title = block.get("title") or block.get("visual_block_id") or "证据视图"
    subtitle = block.get("subtitle") or block.get("data_source") or ""
    return (
        '<div class="visual-head">'
        f"<div><h4>{d(title)}</h4>"
        + (f"<p>{d(subtitle)}</p>" if subtitle else "")
        + "</div>"
        f"<span>{d(label(block.get('type')))}</span>"
        "</div>"
    )


def render_visual_footer(block: dict[str, Any]) -> str:
    refs = block.get("evidence_refs") or block.get("citations") or []
    refs = refs if isinstance(refs, list) else [refs]
    ref_text = ", ".join(str(ref) for ref in refs[:4])
    more = f" +{len(refs) - 4}" if len(refs) > 4 else ""
    note = block.get("note") or ""
    footer = ""
    if note:
        footer += f'<p class="visual-note">{d(note)}</p>'
    if ref_text:
        footer += f'<p class="visual-note">证据引用：{esc(ref_text + more)}</p>'
    return footer


def render_visual_article(block: dict[str, Any], body: str) -> str:
    classes = ["visual-card"]
    if block.get("layout") == "wide" or block.get("width") == "full":
        classes.append("visual-card-wide")
    return f'<article class="{" ".join(classes)}">{body}</article>'


def render_status_panel(block: dict[str, Any]) -> str:
    items = block.get("items") or []
    body = "".join(
        '<div class="status-item">'
        f"<strong>{d(item.get('label') or item.get('title'))}</strong>"
        f"<b>{d(label(item.get('status') or item.get('value')))}</b>"
        f"<small>{d(item.get('note') or item.get('source') or item.get('owner'))}</small>"
        "</div>"
        for item in items
        if isinstance(item, dict)
    )
    return render_visual_article(block, render_visual_header(block) + f'<div class="status-grid">{body}</div>' + render_visual_footer(block))


def render_ranked_bar(block: dict[str, Any]) -> str:
    items = block.get("items") or []
    maximum = block.get("scale_max") or block.get("max") or 100
    rows = []
    for item in items:
        if not isinstance(item, dict):
            continue
        score = number(item.get("score"), 0)
        rows.append(
            '<div class="bar-row">'
            f'<div class="bar-label"><strong>{d(item.get("label") or item.get("name"))}</strong><span>{d(item.get("note") or item.get("reason"))}</span></div>'
            f'<div class="bar-track"><span style="--score:{percent(score, 0, maximum)}"></span></div>'
            f'<b>{d(item.get("score_label") or int(score) if score.is_integer() else score)}</b>'
            "</div>"
        )
    return render_visual_article(block, render_visual_header(block) + '<div class="bar-list">' + "".join(rows) + "</div>" + render_visual_footer(block))


def render_matrix(block: dict[str, Any]) -> str:
    rows = block.get("rows") or []
    columns = block.get("columns") or block.get("headers") or headers_from_rows(rows)
    maximum = block.get("scale_max") or block.get("max") or 100
    body_rows = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        cells = []
        for col in columns:
            value = row_value(row, str(col))
            if isinstance(value, (int, float)):
                cells.append(f'<td class="score-cell"><span style="--score:{percent(value, 0, maximum)}">{esc(value)}</span></td>')
            else:
                cells.append(f"<td>{d(value)}</td>")
        body_rows.append("<tr>" + "".join(cells) + "</tr>")
    table = (
        '<div class="table-scroll"><table><thead><tr>'
        + "".join(f"<th>{d(col)}</th>" for col in columns)
        + "</tr></thead><tbody>"
        + "".join(body_rows)
        + "</tbody></table></div>"
    )
    return render_visual_article(block, render_visual_header(block) + table + render_visual_footer(block))


def render_range_chart(block: dict[str, Any]) -> str:
    items = block.get("items") or []
    scale_min = block.get("scale_min", 0)
    scale_max = block.get("scale_max", 100)
    rows = []
    for item in items:
        if not isinstance(item, dict):
            continue
        low = item.get("min", scale_min)
        high = item.get("max", scale_max)
        left = percent(low, scale_min, scale_max)
        right = percent(high, scale_min, scale_max)
        width = f"{max(0, float(right.rstrip('%')) - float(left.rstrip('%'))):.1f}%"
        rows.append(
            '<div class="range-row">'
            f'<div><strong>{d(item.get("label"))}</strong><span>{d(item.get("note"))}</span></div>'
            f'<div class="range-track"><span style="--left:{left};--width:{width}"></span></div>'
            f"<b>{d(item.get('value_label') or f'{low} - {high}')}</b>"
            "</div>"
        )
    return render_visual_article(block, render_visual_header(block) + '<div class="range-list">' + "".join(rows) + "</div>" + render_visual_footer(block))


def render_visual(block: dict[str, Any]) -> str:
    visual_type = block.get("type")
    if visual_type == "status_panel":
        return render_status_panel(block)
    if visual_type == "ranked_bar":
        return render_ranked_bar(block)
    if visual_type == "matrix_heatmap":
        return render_matrix(block)
    if visual_type == "range_chart":
        return render_range_chart(block)
    return render_visual_article(block, render_visual_header(block) + render_list(block.get("items") or []) + render_visual_footer(block))


def render_section(section: dict[str, Any], report_state: dict[str, Any]) -> str:
    section_id = section.get("section_id")
    title = SECTION_TITLES.get(str(section_id), section.get("section_title") or section_id)
    visual_blocks = section.get("visual_blocks") or []
    badges = section.get("confidence_badges") or []
    badge_text = badges[0].get("label") if badges and isinstance(badges[0], dict) else section.get("status")
    narrative = "".join(f"<p>{d(block)}</p>" for block in section.get("narrative_blocks") or [])
    data_gaps = section.get("data_gaps") or []
    eyebrow = "报告审计" if section_id in SYSTEM_SECTION_IDS else d(section.get("source_skill"))
    return (
        f'<section class="report-section" id="{esc(section_id)}">'
        '<div class="section-title-row">'
        f"<div><p class='eyebrow'>{eyebrow}</p><h2>{d(title)}</h2></div>"
        f"{render_badge(badge_text)}"
        "</div>"
        f'<p class="takeaway"><strong>核心判断：</strong>{d(display_takeaway(section))}</p>'
        f"{narrative}"
        '<div class="visual-grid">'
        + "".join(render_visual(block) for block in visual_blocks)
        + "</div>"
        + render_tables(section.get("tables") or [], report_state)
        + (f'<div class="gap-box"><strong>本节数据缺口</strong>{render_list(data_gaps)}</div>' if data_gaps else "")
        + "</section>"
    )


def render_module_coverage(report_state: dict[str, Any], section_by_id: dict[str, dict[str, Any]]) -> str:
    qg = report_state.get("quality_gate_summary", {})
    rows = []
    for sid in qg.get("rendered_sections", []):
        if sid in SYSTEM_SECTION_IDS:
            continue
        section = section_by_id.get(sid, {})
        rows.append({"板块": sid, "状态": "已进入正文", "说明": desc(section)})
    for sid in qg.get("skipped_sections", []):
        section = section_by_id.get(sid, {})
        rows.append({"板块": sid, "状态": "可选跳过", "说明": display_value(section.get("executive_takeaway", ""))})
    for sid in qg.get("future_sections_omitted", []):
        section = section_by_id.get(sid, {})
        rows.append({"板块": sid, "状态": "未来省略", "说明": display_value(section.get("executive_takeaway", ""))})
    return (
        '<section class="report-section" id="module_coverage">'
        '<div class="section-title-row"><div><p class="eyebrow">附录</p><h2>交付范围说明</h2></div>'
        f'{render_badge(qg.get("status"))}</div>'
        "<p>报告只展示已具备结构化输入的业务板块；可选或未触发内容不会被伪装成完整分析。</p>"
        + render_table("交付范围表", rows, ["板块", "状态", "说明"])
        + "</section>"
    )


def render_data_gap_summary(report_state: dict[str, Any]) -> str:
    gaps = report_state.get("data_gap_log", [])
    return (
        '<section class="report-section" id="data_gap_audit">'
        '<div class="section-title-row"><div><p class="eyebrow">决策风险</p><h2>会改变结论的问题</h2></div>'
        f'{render_badge("pass_with_caveats")}</div>'
        + render_table("结论敏感问题", gaps, ["gap_id", "source_skill", "gap", "severity", "recommended_resolution"])
        + "</section>"
    )


def render_isolation_audit(report_state: dict[str, Any]) -> str:
    records = []
    for record in report_state.get("post_skill_isolation_records", []):
        records.append(
            {
                "skill_id": record.get("skill_id"),
                "status": record.get("status"),
                "source_summary": record.get("compressed_handoff_ref"),
                "html_section": record.get("html_section_ref"),
                "quality_gate": record.get("quality_gate_status"),
                "reopen_conditions": "; ".join(record.get("reopen_conditions") or []),
            }
        )
    return (
        '<section class="report-section" id="isolation_audit">'
        '<div class="section-title-row"><div><p class="eyebrow">来源治理</p><h2>来源与生成审计</h2></div>'
        f'{render_badge("source_governance")}</div>'
        "<p>报告合成只使用业务区块草稿、来源摘要与报告状态；默认不打开上游完整产物。</p>"
        + render_table("来源记录", records, ["skill_id", "status", "source_summary", "html_section", "quality_gate", "reopen_conditions"])
        + "</section>"
    )


def render_private_calculator() -> str:
    return """
    <section class="report-section" id="private_pricing_calculator">
      <div class="section-title-row">
        <div><p class="eyebrow">本地工具</p><h2>私密定价计算器</h2></div>
        <span class="badge contract_ready">仅本地</span>
      </div>
      <p>COGS、毛利率和渠道政策属于商业敏感输入。这里的输入只在浏览器本地计算，不写回报告状态。</p>
      <div class="calculator">
        <label>建议零售价<input id="msrp" type="number" min="0" step="0.01" placeholder="0.00"></label>
        <label>销售成本 / 物料成本<input id="cogs" type="number" min="0" step="0.01" placeholder="0.00"></label>
        <label>目标毛利率 %<input id="target" type="number" min="0" max="99" step="0.1" placeholder="35"></label>
        <label>渠道费用<input id="channel" type="number" min="0" step="0.01" placeholder="0.00"></label>
        <label>折扣<input id="discount" type="number" min="0" step="0.01" placeholder="0.00"></label>
        <label>物流/支付补贴<input id="subsidy" type="number" min="0" step="0.01" placeholder="0.00"></label>
      </div>
      <div class="calc-actions">
        <button type="button" id="calc-run">计算</button>
        <button type="button" id="calc-reset">重置</button>
      </div>
      <div id="calc-results" class="metric-strip"></div>
    </section>
    """


def render_private_profit_optimizer() -> str:
    return """
    <section class="report-section" id="private_profit_revenue_optimizer">
      <div class="section-title-row">
        <div><p class="eyebrow">本地工具</p><h2>私密利润与收入优化器</h2></div>
        <span class="badge contract_ready">仅本地</span>
      </div>
      <p>这个工具用于离网测试“开盘价、促销价、收入最大点、利润最大点”。输入保留在当前浏览器页面，不写回 JSON，也不进入报告状态。</p>
      <div class="calculator">
        <label>候选最低价<input id="opt-min" type="number" min="0" step="0.01" placeholder="300"></label>
        <label>候选最高价<input id="opt-max" type="number" min="0" step="0.01" placeholder="400"></label>
        <label>价格点数量<input id="opt-points" type="number" min="3" max="80" step="1" placeholder="31"></label>
        <label>参考价 / 当前锚点<input id="opt-reference-price" type="number" min="0" step="0.01" placeholder="350"></label>
        <label>基准需求量<input id="opt-base-demand" type="number" min="0" step="1" placeholder="1000"></label>
        <label>自身价格弹性<input id="opt-elasticity" type="number" step="0.05" placeholder="-1.4"></label>
        <label>销售成本 / 物料成本<input id="opt-cogs" type="number" min="0" step="0.01" placeholder="0.00"></label>
        <label>单台可变服务/退货成本<input id="opt-variable-cost" type="number" min="0" step="0.01" placeholder="0.00"></label>
        <label>固定 MKT 投入<input id="opt-mkt-spend" type="number" min="0" step="0.01" placeholder="0.00"></label>
        <label>渠道费用/单台<input id="opt-channel-fee" type="number" min="0" step="0.01" placeholder="0.00"></label>
        <label>促销折扣/单台<input id="opt-discount" type="number" min="0" step="0.01" placeholder="0.00"></label>
        <label>MKT 响应倍率<input id="opt-mkt-mult" type="number" min="0" step="0.05" placeholder="1.00"></label>
        <label>渠道可得性倍率<input id="opt-channel-mult" type="number" min="0" step="0.05" placeholder="1.00"></label>
        <label>证明成熟度倍率<input id="opt-proof-mult" type="number" min="0" step="0.05" placeholder="1.00"></label>
      </div>
      <div class="calc-actions">
        <button type="button" id="opt-run">寻找最大点</button>
        <button type="button" id="opt-reset">重置</button>
      </div>
      <div id="opt-results" class="metric-strip"></div>
      <div id="opt-table" class="table-block" hidden></div>
    </section>
    """


def render_management_summary(report_state: dict[str, Any], brief: dict[str, Any], qg: dict[str, Any]) -> str:
    summary = report_state.get("management_summary") or {}
    judgment = report_state.get("gtm_judgment_cover") or summary.get("gtm_judgment_cover") or {}
    headline = summary.get("headline") or f"{display_value(brief.get('product_name_or_codename') or '产品')} GTM 判断"
    confidence_note = summary.get("confidence_note") or judgment.get("core_recommendation") or "先形成价格证明、渠道资源和内容种草的可执行打法，再用最小验证降低首销风险。"
    channels = [item for item in summary.get("local_channel_priority") or [] if isinstance(item, dict)]
    kpis = summary.get("judgment_cards") or summary.get("kpis") or [
        {"label": "GTM判断", "value": judgment.get("judgment_label") or judgment.get("judgment") or "待判断", "note": judgment.get("core_recommendation") or "判断进入、守价、谨慎上市或先验证。"},
        {"label": "首要打法", "value": judgment.get("opening_move") or "待确定", "note": "价格、渠道、内容或offer的第一动作。"},
        {"label": "先打人群", "value": judgment.get("priority_segment") or "待确定", "note": "以需求强度、支付意愿和触达效率排序。"},
        {"label": "Must-win渠道", "value": judgment.get("must_win_channel") or "待确定", "note": "正式版应落到本地渠道名。"},
        {"label": "价格/Offer", "value": judgment.get("price_or_offer_stance") or "待确定", "note": "说明如何守价、促销或用权益托住。"},
        {"label": "会改变结论的问题", "value": judgment.get("decision_changing_question") or "待确认", "note": "只保留会改变打法的关键不确定性。"},
    ]
    if channels:
        channel_value = " > ".join(str(item.get("channel_name") or "") for item in channels[:3] if item.get("channel_name"))
        kpis = [
            {
                **item,
                "value": channel_value or item.get("value"),
                "note": "由本地渠道证据与优先级列表生成",
            }
            if isinstance(item, dict) and item.get("label") == "渠道优先级"
            else item
            for item in kpis
        ]
    decision_blocks = summary.get("decision_blocks") or []
    kpi_html = "".join(
        '<div class="metric exec-metric">'
        f'<span>{d(item.get("label"))}</span>'
        f'<strong>{d(item.get("value"))}</strong>'
        f'<small>{d(item.get("note"))}</small>'
        "</div>"
        for item in kpis
        if isinstance(item, dict)
    )
    blocks_html = "".join(
        '<article class="exec-block">'
        f'<h3>{d(block.get("title"))}</h3>'
        f'{render_list(block.get("points") or [])}'
        "</article>"
        for block in decision_blocks
        if isinstance(block, dict)
    )
    channel_html = ""
    if channels:
        channel_items = "".join(
            '<article class="exec-channel-item">'
            f'<strong>{esc(item.get("rank"))}. {d(item.get("channel_name"))}</strong>'
            f'<span>{d(item.get("channel_type"))} / {d(item.get("role"))}</span>'
            f'<small>{d(item.get("reason"))}</small>'
            f'<em>{d(item.get("evidence_status"))}</em>'
            "</article>"
            for item in channels[:4]
        )
        channel_html = (
            '<div class="exec-channel-panel">'
            "<h3>渠道名与角色</h3>"
            f'<div class="exec-channel-list">{channel_items}</div>'
            "</div>"
        )
    context_items = summary.get("commercial_context_chips") or []
    context_html = "".join(f"<span>{d(item)}</span>" for item in context_items)
    return (
        '<section class="hero exec-hero" id="executive_summary">'
        '<div class="section-title-row exec-title-row">'
        f'<div><p class="eyebrow">GTM判断</p><h2>{d(headline)}</h2></div>'
        f'{render_badge(summary.get("status") or "pass_with_caveats")}'
        "</div>"
        f'<p class="takeaway">{d(confidence_note)}</p>'
        + (f'<div class="exec-context">{context_html}</div>' if context_html else "")
        + f'<div class="exec-kpis">{kpi_html}</div>'
        + f"{channel_html}"
        + f'<div class="exec-blocks">{blocks_html}</div>'
        "</section>"
    )


def build_html(report_state: dict[str, Any]) -> str:
    brief = report_state.get("project_brief", {})
    qg = report_state.get("quality_gate_summary", {})
    section_by_id = {section.get("section_id"): section for section in report_state.get("sections", [])}
    rendered_ids = qg.get("rendered_sections") or []
    rendered_sections = [section_by_id[sid] for sid in rendered_ids if sid in section_by_id]
    feature_items = [display_feature(item) for item in brief.get("product_features_and_specs") or []]
    visual_count = qg.get("visual_block_count", 0)
    isolation_count = qg.get("isolation_record_count", 0)

    nav_items = [
        ("executive_summary", "GTM判断"),
        ("module_coverage", "交付范围"),
        *[(section.get("section_id"), SECTION_TITLES.get(section.get("section_id"), section.get("section_title"))) for section in rendered_sections],
        ("data_gap_audit", "会改变结论的问题"),
        ("isolation_audit", "来源治理"),
        ("private_pricing_calculator", "定价计算器"),
        ("private_profit_revenue_optimizer", "利润/收入优化器"),
    ]
    nav_html = "".join(f'<a href="#{esc(item_id)}"><span>{d(title)}</span></a>' for item_id, title in nav_items)
    sections_html = "".join(render_section(section, report_state) for section in rendered_sections)

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>GTM 报告</title>
  <style>
    :root {{
      --paper: #f6f7f9;
      --surface: #ffffff;
      --ink: #17202a;
      --muted: #667085;
      --line: #d8dee8;
      --blue: #2457d6;
      --green: #157f5b;
      --amber: #b25b00;
      --red: #b42318;
      --violet: #6941c6;
      --radius: 8px;
      --shadow: 0 10px 28px rgba(23, 32, 42, 0.08);
      --font: "Noto Sans SC", "Microsoft YaHei", "PingFang SC", "Segoe UI", system-ui, sans-serif;
      --mono: ui-monospace, SFMono-Regular, Consolas, monospace;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{ margin: 0; font-family: var(--font); color: var(--ink); background: var(--paper); line-height: 1.55; }}
    a {{ color: inherit; text-decoration: none; }}
    .layout {{ display: grid; grid-template-columns: 260px minmax(0, 1fr); min-height: 100vh; }}
    .rail {{ position: sticky; top: 0; height: 100vh; padding: 22px 18px; background: #142033; color: #f8fafc; overflow-y: auto; }}
    .brand {{ padding-bottom: 18px; border-bottom: 1px solid rgba(255,255,255,.16); }}
    .brand h1 {{ margin: 0; font-size: 21px; line-height: 1.18; letter-spacing: 0; }}
    .brand p, .rail small {{ color: #b8c2d3; margin: 7px 0 0; font-size: 13px; }}
    .nav {{ display: grid; gap: 4px; margin-top: 18px; }}
    .nav a {{ padding: 9px 10px; border-radius: 6px; color: #e8eef7; font-size: 14px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
    .nav a:hover {{ background: rgba(255,255,255,.08); }}
    .main {{ min-width: 0; padding: 26px; }}
    .container {{ max-width: 1220px; margin: 0 auto; display: grid; gap: 18px; }}
    .hero {{ background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); padding: 24px; box-shadow: var(--shadow); }}
    .exec-hero {{ padding: 18px; }}
    .eyebrow {{ margin: 0 0 6px; color: var(--blue); font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: .08em; }}
    h1, h2, h3, h4, p {{ margin-top: 0; }}
    .hero h2 {{ margin: 0; font-size: 34px; line-height: 1.12; letter-spacing: 0; }}
    .exec-hero h2 {{ font-size: 27px; max-width: 900px; }}
    .hero-grid {{ display: grid; grid-template-columns: minmax(0, 1fr); gap: 18px; align-items: start; margin-top: 16px; }}
    .exec-context {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px; color: var(--muted); font-size: 12px; font-weight: 700; }}
    .exec-context span {{ padding: 2px 8px; border: 1px solid var(--line); border-radius: 999px; background: #f8fafc; }}
    .exec-kpis {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 8px; margin-top: 12px; }}
    .exec-metric {{ min-height: 72px; padding: 11px; }}
    .exec-metric small {{ display: block; margin-top: 3px; color: var(--muted); font-size: 12px; line-height: 1.35; }}
    .exec-blocks {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; margin-top: 12px; }}
    .exec-block {{ padding: 12px; border: 1px solid var(--line); border-radius: var(--radius); background: #f8fafc; min-width: 0; }}
    .exec-block h3 {{ margin-bottom: 8px; font-size: 14px; line-height: 1.25; }}
    .exec-block .clean-list {{ gap: 5px; padding-left: 16px; font-size: 13px; line-height: 1.45; }}
    .exec-channel-panel {{ margin-top: 10px; padding: 12px; border: 1px solid var(--line); border-radius: var(--radius); background: #fff; }}
    .exec-channel-panel h3 {{ margin-bottom: 8px; font-size: 14px; line-height: 1.25; }}
    .exec-channel-list {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; }}
    .exec-channel-item {{ display: grid; gap: 4px; padding: 10px; border: 1px solid var(--line); border-radius: 6px; background: #f8fafc; min-width: 0; }}
    .exec-channel-item strong, .exec-channel-item span, .exec-channel-item small, .exec-channel-item em {{ overflow-wrap: anywhere; }}
    .exec-channel-item span, .exec-channel-item small {{ color: var(--muted); font-size: 12px; line-height: 1.35; }}
    .exec-channel-item em {{ color: var(--amber); font-size: 12px; font-style: normal; font-weight: 800; }}
    .metric-strip {{ display: grid; grid-template-columns: repeat(4, minmax(170px, 1fr)); gap: 10px; }}
    .metric {{ padding: 13px; background: #f8fafc; border: 1px solid var(--line); border-radius: var(--radius); min-height: 78px; }}
    .metric span {{ display:block; color: var(--muted); font-size: 12px; font-weight: 700; }}
    .metric strong {{ display:block; margin-top: 5px; font-size: 19px; overflow-wrap: anywhere; }}
    .report-section {{ padding: 26px 0; border-top: 1px solid var(--line); display: grid; gap: 16px; }}
    .section-title-row {{ display: flex; justify-content: space-between; gap: 18px; align-items: flex-start; }}
    .section-title-row h2 {{ margin: 0; font-size: 25px; line-height: 1.22; letter-spacing: 0; }}
    .takeaway {{ max-width: 980px; font-size: 15px; }}
    .badge {{ display: inline-flex; align-items: center; min-height: 28px; padding: 4px 10px; border-radius: 999px; border: 1px solid var(--line); color: var(--muted); background: #fff; font-size: 12px; font-weight: 800; white-space: nowrap; }}
    .badge.rendered_with_gaps, .badge.pass_with_caveats, .badge.hypothesis_only {{ color: var(--amber); background: #fff7ed; border-color: #fed7aa; }}
    .badge.contract_ready, .badge.pass {{ color: var(--green); background: #ecfdf3; border-color: #b7e4c7; }}
    .badge.handoff_only {{ color: var(--violet); background: #f4f3ff; border-color: #d9d6fe; }}
    .visual-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }}
    .visual-card, .table-block, .gap-box, .calculator, .calc-actions {{ background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow); }}
    .visual-card {{ padding: 16px; display: grid; gap: 12px; min-width: 0; }}
    .visual-card-wide {{ grid-column: 1 / -1; }}
    .visual-head {{ display: flex; justify-content: space-between; gap: 12px; align-items: flex-start; border-bottom: 1px solid var(--line); padding-bottom: 10px; }}
    .visual-head h4 {{ margin: 0; font-size: 16px; letter-spacing: 0; }}
    .visual-head p, .visual-note, .muted {{ margin: 4px 0 0; color: var(--muted); font-size: 13px; }}
    .visual-head span {{ color: var(--blue); font-size: 12px; font-weight: 800; white-space: nowrap; }}
    .status-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 9px; }}
    .status-item {{ padding: 11px; border: 1px solid var(--line); border-radius: 6px; background: #f8fafc; min-width: 0; }}
    .status-item strong, .status-item b, .status-item small {{ display: block; overflow-wrap: anywhere; }}
    .status-item b {{ color: var(--blue); margin-top: 4px; }}
    .status-item small {{ color: var(--muted); margin-top: 3px; }}
    .bar-list, .range-list {{ display: grid; gap: 10px; }}
    .bar-row, .range-row {{ display: grid; grid-template-columns: minmax(150px, 1fr) minmax(130px, 230px) 54px; gap: 10px; align-items: center; }}
    .bar-label strong, .bar-label span, .range-row strong, .range-row span {{ display: block; overflow-wrap: anywhere; }}
    .bar-label span, .range-row span {{ color: var(--muted); font-size: 12px; }}
    .bar-track, .range-track {{ position: relative; height: 10px; background: #e7ecf3; border-radius: 999px; overflow: hidden; }}
    .bar-track span {{ display: block; height: 100%; width: var(--score); background: linear-gradient(90deg, var(--blue), var(--green)); border-radius: inherit; }}
    .range-track span {{ position: absolute; left: var(--left); width: var(--width); height: 100%; background: linear-gradient(90deg, var(--amber), var(--blue)); border-radius: inherit; }}
    .table-block {{ padding: 16px; min-width: 0; }}
    .table-block h4 {{ margin-bottom: 10px; }}
    .table-scroll {{ overflow-x: auto; }}
    table {{ width: 100%; border-collapse: collapse; min-width: 620px; }}
    th, td {{ padding: 10px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; font-size: 13px; }}
    th {{ color: var(--muted); background: #f8fafc; font-weight: 800; }}
    .score-cell span {{ display: inline-flex; min-width: 42px; justify-content: center; padding: 3px 7px; border-radius: 6px; background: color-mix(in srgb, var(--blue) var(--score), #eef3ff); color: #122033; font-weight: 800; }}
    .clean-list {{ margin: 0; padding-left: 18px; display: grid; gap: 8px; }}
    .clean-list li span {{ display:block; color: var(--muted); font-size: 13px; }}
    .gap-box {{ padding: 14px; border-left: 4px solid var(--amber); }}
    .calculator {{ padding: 16px; display: grid; grid-template-columns: repeat(3, minmax(150px, 1fr)); gap: 12px; }}
    label {{ display: grid; gap: 6px; color: var(--muted); font-size: 13px; font-weight: 700; }}
    input {{ min-height: 38px; border: 1px solid var(--line); border-radius: 6px; padding: 7px 9px; font: inherit; }}
    .calc-actions {{ padding: 12px; display: flex; gap: 10px; flex-wrap: wrap; }}
    button {{ min-height: 36px; border: 1px solid var(--line); border-radius: 6px; background: #fff; color: var(--ink); font: inherit; font-weight: 800; padding: 6px 12px; cursor: pointer; }}
    button:first-child {{ background: var(--blue); color: #fff; border-color: var(--blue); }}
    @media (max-width: 980px) {{
      .layout {{ grid-template-columns: 1fr; }}
      .rail {{ position: relative; height: auto; }}
      .hero-grid, .visual-grid {{ grid-template-columns: 1fr; }}
      .metric-strip, .calculator, .exec-kpis {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
      .exec-blocks, .exec-channel-list {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    }}
    @media (max-width: 620px) {{
      .main {{ padding: 16px; }}
      .hero {{ padding: 18px; }}
      .hero h2 {{ font-size: 27px; }}
      .metric-strip, .calculator, .status-grid, .exec-kpis, .exec-blocks, .exec-channel-list {{ grid-template-columns: 1fr; }}
      .bar-row, .range-row {{ grid-template-columns: 1fr; }}
      .section-title-row {{ display: grid; }}
    }}
  </style>
</head>
<body>
  <div class="layout">
    <aside class="rail">
      <div class="brand">
        <h1>GTM Master GTM 报告</h1>
        <p>{d(report_state.get("report_id"))}</p>
        <small>离线 HTML / 报告样例</small>
      </div>
      <nav class="nav">{nav_html}</nav>
    </aside>
    <main class="main">
      <div class="container">
        {render_management_summary(report_state, brief, qg)}

        <section class="report-section" id="judgment_assumptions">
          <div class="section-title-row"><div><p class="eyebrow">判断前提</p><h2>影响打法的产品与商业前提</h2></div>{render_badge(brief.get("report_depth"))}</div>
          <p class="takeaway">这里只保留会影响卖点、人群、价格、渠道或验证动作的前提；完整输入清单放入来源治理附录。</p>
          {render_list(feature_items)}
        </section>

        {render_module_coverage(report_state, section_by_id)}
        {sections_html}
        {render_data_gap_summary(report_state)}
        {render_isolation_audit(report_state)}
        {render_private_calculator()}
        {render_private_profit_optimizer()}
      </div>
    </main>
  </div>
  <script>
    function n(id) {{
      const value = Number(document.getElementById(id).value);
      return Number.isFinite(value) ? value : 0;
    }}
    function money(value) {{ return Number.isFinite(value) ? value.toFixed(2) : "0.00"; }}
    function pct(value) {{ return Number.isFinite(value) ? (value * 100).toFixed(1) + "%" : "0.0%"; }}
    function card(label, value, note) {{
      return '<div class="metric"><span>' + label + '</span><strong>' + value + '</strong><span>' + note + '</span></div>';
    }}
    document.getElementById("calc-run").addEventListener("click", function () {{
      const msrp = n("msrp"), cogs = n("cogs"), target = n("target") / 100;
      const net = msrp - n("channel") - n("discount") - n("subsidy");
      const gm = net > 0 ? (net - cogs) / net : 0;
      const floor = target < 1 ? cogs / (1 - target) : 0;
      const gap = net - floor;
      document.getElementById("calc-results").innerHTML =
        card("估算净价", money(net), "零售价减去可见扣减") +
        card("毛利率", pct(gm), "仅本地计算") +
        card("毛利缺口", money(gap), gap >= 0 ? "高于底线" : "低于底线");
    }});
    document.getElementById("calc-reset").addEventListener("click", function () {{
      ["msrp", "cogs", "target", "channel", "discount", "subsidy"].forEach(function (id) {{ document.getElementById(id).value = ""; }});
      document.getElementById("calc-results").innerHTML = "";
    }});
    function positive(id, fallback) {{
      const value = n(id);
      return value > 0 ? value : fallback;
    }}
    function runOptimizer() {{
      let minPrice = positive("opt-min", 300);
      let maxPrice = positive("opt-max", 400);
      if (maxPrice < minPrice) {{
        const tmp = minPrice;
        minPrice = maxPrice;
        maxPrice = tmp;
      }}
      const points = Math.max(3, Math.min(80, Math.round(positive("opt-points", 31))));
      const reference = positive("opt-reference-price", (minPrice + maxPrice) / 2);
      const baseDemand = positive("opt-base-demand", 1000);
      const elasticityInput = document.getElementById("opt-elasticity").value;
      const elasticity = elasticityInput === "" ? -1.4 : n("opt-elasticity");
      const cogs = n("opt-cogs");
      const variableCost = n("opt-variable-cost");
      const mktSpend = n("opt-mkt-spend");
      const channelFee = n("opt-channel-fee");
      const discount = n("opt-discount");
      const mktMult = positive("opt-mkt-mult", 1);
      const channelMult = positive("opt-channel-mult", 1);
      const proofMult = positive("opt-proof-mult", 1);
      const rows = [];
      let revenueBest = null;
      let profitBest = null;
      for (let index = 0; index < points; index += 1) {{
        const rawPrice = minPrice + ((maxPrice - minPrice) * index) / (points - 1);
        const netPrice = Math.max(0, rawPrice - channelFee - discount);
        const priceIndex = reference > 0 ? Math.max(0.01, netPrice / reference) : 1;
        const units = Math.max(0, baseDemand * Math.pow(priceIndex, elasticity) * mktMult * channelMult * proofMult);
        const revenue = netPrice * units;
        const unitContribution = netPrice - cogs - variableCost;
        const profit = unitContribution * units - mktSpend;
        const row = {{ price: rawPrice, netPrice, units, revenue, unitContribution, profit }};
        rows.push(row);
        if (!revenueBest || revenue > revenueBest.revenue) revenueBest = row;
        if (!profitBest || profit > profitBest.profit) profitBest = row;
      }}
      const profitNote = profitBest.unitContribution < 0 ? "单台贡献为负，需要检查 COGS 或折扣" : "按当前输入估算";
      document.getElementById("opt-results").innerHTML =
        card("收入最大点", money(revenueBest.price), "收入 " + money(revenueBest.revenue) + " / 量 " + Math.round(revenueBest.units)) +
        card("利润最大点", money(profitBest.price), "贡献利润 " + money(profitBest.profit)) +
        card("建议开盘口径", money(Math.max(profitBest.price, revenueBest.price)), "用利润点守底线，用收入点看规模") +
        card("风险提示", money(profitBest.unitContribution), profitNote);
      const sample = rows.filter(function (_, index) {{
        return index === 0 || index === rows.length - 1 || index === Math.floor(rows.length / 2) || rows[index] === revenueBest || rows[index] === profitBest;
      }});
      let table = '<h4>候选价格抽样</h4><div class="table-scroll"><table><thead><tr><th>价格</th><th>净价</th><th>销量指数</th><th>收入</th><th>贡献利润</th></tr></thead><tbody>';
      sample.forEach(function (row) {{
        table += '<tr><td>' + money(row.price) + '</td><td>' + money(row.netPrice) + '</td><td>' + Math.round(row.units) + '</td><td>' + money(row.revenue) + '</td><td>' + money(row.profit) + '</td></tr>';
      }});
      table += '</tbody></table></div>';
      const tableEl = document.getElementById("opt-table");
      tableEl.innerHTML = table;
      tableEl.hidden = false;
    }}
    document.getElementById("opt-run").addEventListener("click", runOptimizer);
    document.getElementById("opt-reset").addEventListener("click", function () {{
      ["opt-min", "opt-max", "opt-points", "opt-reference-price", "opt-base-demand", "opt-elasticity", "opt-cogs", "opt-variable-cost", "opt-mkt-spend", "opt-channel-fee", "opt-discount", "opt-mkt-mult", "opt-channel-mult", "opt-proof-mult"].forEach(function (id) {{
        document.getElementById(id).value = "";
      }});
      document.getElementById("opt-results").innerHTML = "";
      document.getElementById("opt-table").hidden = true;
      document.getElementById("opt-table").innerHTML = "";
    }});
  </script>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a static GTM dashboard from report-state JSON.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    report_state = json.loads(args.input.read_text(encoding="utf-8"))
    html_text = build_html(report_state)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html_text, encoding="utf-8", newline="\n")

    rendered_sections = report_state.get("quality_gate_summary", {}).get("rendered_sections", [])
    print(f"Rendered {len(rendered_sections)} sections to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
