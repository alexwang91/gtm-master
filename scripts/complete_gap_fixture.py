from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "artifacts" / "dry-runs" / "generic-hardware-s00-s08-s13-s14-report-state.json"


def status_items(items: list[tuple[str, str, str]]) -> list[dict[str, str]]:
    return [{"label": label, "status": status, "note": note} for label, status, note in items]


def visual(
    visual_block_id: str,
    visual_type: str,
    title: str,
    data_source: str,
    *,
    items: list[dict] | None = None,
    rows: list[dict] | None = None,
    columns: list[str] | None = None,
    note: str = "",
    wide: bool = False,
    evidence_ref: str = "",
) -> dict:
    block = {
        "visual_block_id": visual_block_id,
        "type": visual_type,
        "title": title,
        "data_source": data_source,
        "note": note,
        "evidence_refs": [evidence_ref or f"dryrun://evidence/{visual_block_id}"],
        "confidence": "hypothesis_only",
    }
    if wide:
        block["layout"] = "wide"
    if items is not None:
        block["items"] = items
    if rows is not None:
        block["rows"] = rows
        block["columns"] = columns or list(rows[0].keys())
        block["scale_min"] = 0
        block["scale_max"] = 100
    return block


def section(
    section_id: str,
    source_skill: str,
    title: str,
    takeaway: str,
    visual_blocks: list[dict],
    tables: list[dict],
    gaps: list[str],
    citation: str,
    handoff: str,
) -> dict:
    return {
        "section_id": section_id,
        "source_skill": source_skill,
        "section_title": title,
        "status": "rendered_with_gaps",
        "executive_takeaway": takeaway,
        "visual_blocks": visual_blocks,
        "tables": tables,
        "confidence_badges": [
            {
                "label": "条件草案",
                "reason": "dry-run 只补齐方法、输入缺口和可审核输出，不代表真实市场结论。",
            }
        ],
        "data_gaps": gaps,
        "citations": [citation],
        "handoff_ref": handoff,
    }


def build_sections() -> dict[str, dict]:
    return {
        "copy_assets": section(
            "copy_assets",
            "S05.score-creative-assets",
            "文案资产",
            "S05 作为文字资产评分与修订模块保留在看板中；没有可编辑文案时，它输出输入清单、评分标准、测试队列和修订方向。",
            [
                visual(
                    "s05-copy-input-gate",
                    "status_panel",
                    "文案输入覆盖门禁",
                    "copy_input_coverage_gate",
                    items=status_items(
                        [
                            ("S03 信息路线", "样例可用", "可用于判断文案是否贴合人群任务。"),
                            ("可编辑文字", "缺真实输入", "需要标题、PDP 要点、落地页文字、脚本或广告文案。"),
                            ("品牌语气", "缺真实输入", "需要品牌定位、禁用词、批准主张或历史素材。"),
                            ("渠道格式", "缺真实输入", "需要电商、广告、零售、KOL 或官网投放位置。"),
                        ]
                    ),
                    note="S05 只处理可编辑文字；图片、视频和版式作为约束，不作为可直接修改对象。",
                ),
                visual(
                    "s05-copy-scorecard",
                    "matrix_heatmap",
                    "文案评分与修订需求",
                    "copy_message_fit_scorecard",
                    rows=[
                        {"资产类型": "主标题", "信息适配": 66, "证明清晰": 42, "本地语言": 38, "修订动作": "补本地搜索词和可验证利益点"},
                        {"资产类型": "PDP 要点", "信息适配": 61, "证明清晰": 48, "本地语言": 35, "修订动作": "把规格转成购买理由和证据"},
                        {"资产类型": "价格说法", "信息适配": 55, "证明清晰": 40, "本地语言": 32, "修订动作": "加入价格锚点、保修和渠道信任"},
                        {"资产类型": "零售话术", "信息适配": 58, "证明清晰": 44, "本地语言": 36, "修订动作": "转成导购可解释的对比话术"},
                    ],
                    note="评分 = 信息路线适配 30% + 证明清晰 25% + 本地语言 20% + 渠道格式 15% + 风险合规 10%。",
                ),
                visual(
                    "s05-channel-copy-fit",
                    "matrix_heatmap",
                    "渠道文案适配矩阵",
                    "channel_copy_fit_matrix",
                    rows=[
                        {"渠道": "本地电商", "主张清晰": 62, "证明需求": 76, "风险": "需要竞品同屏对比"},
                        {"渠道": "零售导购", "主张清晰": 58, "证明需求": 72, "风险": "需要一句话解释和演示点"},
                        {"渠道": "品牌自营", "主张清晰": 64, "证明需求": 68, "风险": "需要承接评测和 FAQ"},
                        {"渠道": "创作者内容", "主张清晰": 54, "证明需求": 80, "风险": "需要真实体验和披露规则"},
                    ],
                    note="同一卖点在不同渠道需要不同证据密度和表达长度。",
                ),
                visual(
                    "s05-copy-test-backlog",
                    "ranked_bar",
                    "文案测试优先级",
                    "copy_test_backlog",
                    items=[
                        {"label": "主标题利益点冒烟测试", "score": 82, "note": "先验证消费者是否理解核心价值。"},
                        {"label": "PDP 证明顺序测试", "score": 74, "note": "比较规格、评测、保修和渠道信任的排序。"},
                        {"label": "价格说法测试", "score": 70, "note": "检查高开、促销和价值锚点的接受度。"},
                        {"label": "零售导购话术测试", "score": 62, "note": "用于渠道培训和线下转化。"},
                    ],
                    note="优先级按决策影响、修改成本、测试速度和下游依赖计算。",
                ),
            ],
            [
                {
                    "table_id": "s05-copy-request-list",
                    "title": "文案资料需求清单",
                    "rows": [
                        {"输入": "可编辑文案", "用途": "评分、修订建议和测试变体", "状态": "需要用户提供"},
                        {"输入": "品牌语气与禁用词", "用途": "避免风格偏移和风险词", "状态": "建议提供"},
                        {"输入": "渠道格式", "用途": "确定字数、结构、CTA 和证明密度", "状态": "建议提供"},
                        {"输入": "历史广告或落地页文字", "用途": "识别延续资产和低效表达", "状态": "可选但高价值"},
                    ],
                },
                {
                    "table_id": "s05-method",
                    "title": "文案评分方法",
                    "rows": [
                        {"步骤": "输入覆盖", "方法": "确认是否有可编辑文字、批准主张、品牌语气和渠道格式。"},
                        {"步骤": "信息适配", "方法": "对照 S03 人群信息路线、S02 证明需求和 S04 价格护栏。"},
                        {"步骤": "修订建议", "方法": "只改文字和话术，不要求用户上传图片，也不改不可编辑素材。"},
                        {"步骤": "测试队列", "方法": "把高风险主张、价格说法和本地语言不确定性送入 S13。"},
                    ],
                },
            ],
            ["可编辑文案", "品牌语气", "渠道格式", "批准主张或证明素材"],
            "C-DRY-005",
            "dryrun://handoff/S05-copy-assets",
        ),
        "creator_kol": section(
            "creator_kol",
            "S06.score-kol-fit",
            "KOL 与创作者策略",
            "S06 给出创作者类型、选择理由、预算和预期范围，再等待真实候选与本地平台数据。",
            [
                visual(
                    "s06-creator-input-gate",
                    "status_panel",
                    "创作者输入覆盖门禁",
                    "creator_input_coverage_gate",
                    items=status_items(
                        [
                            ("目标平台", "缺真实输入", "需要国家本地平台或用户指定平台。"),
                            ("预算范围", "缺真实输入", "需要总预算、单人预算或样品成本。"),
                            ("竞品创作者历史", "待联网确认", "用于判断行业常用 KOL 类型和内容形式。"),
                            ("候选名单", "未提供", "没有候选时先输出类型和发现计划。"),
                        ]
                    ),
                    note="S06 不直接拍板人选，先给筛选逻辑、预算区间和预期结果范围。",
                ),
                visual(
                    "s06-archetype-fit",
                    "matrix_heatmap",
                    "创作者类型适配评分",
                    "creator_archetype_fit_scorecard",
                    rows=[
                        {"创作者类型": "专业评测媒体", "证明力": 82, "触达": 58, "预算压力": 62, "建议": "优先用于建立可信证明"},
                        {"创作者类型": "本地科技 KOL", "证明力": 74, "触达": 68, "预算压力": 58, "建议": "适合对比和开箱内容"},
                        {"创作者类型": "生活方式创作者", "证明力": 52, "触达": 72, "预算压力": 54, "建议": "适合场景化种草但需强 brief"},
                        {"创作者类型": "零售专家/导购", "证明力": 66, "触达": 45, "预算压力": 38, "建议": "适合渠道信任和线下转化"},
                    ],
                    note="适配分由人群信任、证明需求、平台相关、预算可行和品牌安全共同决定。",
                ),
                visual(
                    "s06-budget-outcome",
                    "matrix_heatmap",
                    "KOL预算与预期结果",
                    "creator_budget_expected_outcome",
                    rows=[
                        {"方案": "专业评测 1-2 个", "预算占比": "35%-45%", "预期访问": "中", "预期点赞/互动": "中", "核心理由": "证明产品价值、降低购买风险、可沉淀到 PDP 和渠道"},
                        {"方案": "本地科技 KOL 3-5 个", "预算占比": "30%-40%", "预期访问": "中-高", "预期点赞/互动": "中", "核心理由": "覆盖搜索、对比和开箱内容"},
                        {"方案": "生活方式或垂类小号 8-15 个", "预算占比": "15%-25%", "预期访问": "分散", "预期点赞/互动": "中-高", "核心理由": "测试场景语言和人群兴趣"},
                        {"方案": "零售/媒体合作内容", "预算占比": "10%-20%", "预期访问": "低-中", "预期点赞/互动": "低", "核心理由": "提升渠道信任和导购解释效率"},
                    ],
                    note="正式运行会用本地平台费率、历史互动、投放目标和追踪链路刷新预算与预期；当前只给结构。",
                    wide=True,
                ),
                visual(
                    "s06-risk-review",
                    "ranked_bar",
                    "品牌安全与披露风险",
                    "brand_safety_disclosure_review",
                    items=[
                        {"label": "体验夸大或未证明主张", "score": 78},
                        {"label": "赞助披露不清", "score": 70},
                        {"label": "受众与目标人群错配", "score": 62},
                        {"label": "历史争议或竞品绑定", "score": 58},
                    ],
                    note="高风险候选进入排除或人工复核，不直接进入推荐。",
                ),
            ],
            [
                {
                    "table_id": "s06-creator-method",
                    "title": "创作者筛选方法",
                    "rows": [
                        {"步骤": "类型优先", "方法": "先判断专业评测、科技 KOL、生活方式、零售专家分别解决什么信任问题。"},
                        {"步骤": "候选发现", "方法": "正式运行用本地平台、竞品内容、搜索词和评测来源生成候选长名单。"},
                        {"步骤": "预算估算", "方法": "用费率、样品成本、制作成本、目标访问和互动范围估算。"},
                        {"步骤": "结果解释", "方法": "访问、点赞和互动只作为上游信号，不直接当作销量。"},
                    ],
                }
            ],
            ["目标平台", "预算范围", "本地创作者候选", "竞品创作者历史"],
            "C-DRY-006",
            "dryrun://handoff/S06-creator-kol",
        ),
        "dtc_conversion": section(
            "dtc_conversion",
            "S07.predict-dtc-conversion",
            "DTC 转化与落地页诊断",
            "S07 在没有自有页面时，先用竞品页面、上一代页面和上游信息路线生成页面要求、摩擦风险和测试计划。",
            [
                visual(
                    "s07-conversion-input-gate",
                    "status_panel",
                    "转化输入覆盖门禁",
                    "conversion_input_coverage_gate",
                    items=status_items(
                        [
                            ("自有页面文字", "缺真实输入", "没有页面时进入上线前规划模式。"),
                            ("竞品页面", "待联网确认", "用于识别本地 PDP 和落地页标准。"),
                            ("上一代页面", "需要用户资料", "可提炼有效结构和历史摩擦。"),
                            ("追踪方案", "缺真实输入", "需要事件、渠道参数和转化目标。"),
                        ]
                    ),
                    note="S07 不承诺 CVR 或销量，只输出摩擦评分、假设区间和实验计划。",
                ),
                visual(
                    "s07-page-benchmark",
                    "matrix_heatmap",
                    "竞品/上一代页面基准",
                    "competitor_previous_page_benchmark",
                    rows=[
                        {"基准对象": "TOP1竞品页面", "价值证明": 72, "价格信任": 68, "退换/保修": 60, "可借鉴点": "首屏证明、对比表、评价入口"},
                        {"基准对象": "上一代产品页面", "价值证明": 55, "价格信任": 50, "退换/保修": 48, "可借鉴点": "保留有效 FAQ，修复解释不足"},
                        {"基准对象": "本地电商 PDP", "价值证明": 66, "价格信任": 74, "退换/保修": 70, "可借鉴点": "配送、保修、评价和支付信任"},
                    ],
                    note="正式运行需保存来源、页面日期和可访问状态；当前仅定义比较结构。",
                    wide=True,
                ),
                visual(
                    "s07-friction-scorecard",
                    "ranked_bar",
                    "转化摩擦优先级",
                    "funnel_friction_scorecard",
                    items=[
                        {"label": "价值证明不足", "score": 82},
                        {"label": "价格与保修信任不足", "score": 76},
                        {"label": "首屏任务不清", "score": 69},
                        {"label": "追踪事件不完整", "score": 64},
                    ],
                    note="摩擦分越高，越应先补证明、信任、CTA 或追踪。",
                ),
                visual(
                    "s07-page-experiments",
                    "ranked_bar",
                    "页面实验优先级",
                    "page_experiment_plan",
                    items=[
                        {"label": "首屏利益点 A/B", "score": 80},
                        {"label": "价格锚点与保障组合", "score": 76},
                        {"label": "竞品对比表位置", "score": 70},
                        {"label": "评价/评测证据模块", "score": 68},
                    ],
                    note="上线前可用静态页面、广告点击或小流量实验验证。",
                ),
            ],
            [
                {
                    "table_id": "s07-page-materials",
                    "title": "页面与转化资料需求",
                    "rows": [
                        {"输入": "页面文字或结构", "用途": "判断信息顺序、CTA 和证明密度"},
                        {"输入": "竞品或上一代页面", "用途": "建立本地页面基准"},
                        {"输入": "流量来源计划", "用途": "检查广告到页面的信息连续性"},
                        {"输入": "追踪事件", "用途": "保证后续能解释点击、加购、跳出和购买"},
                    ],
                }
            ],
            ["页面文字", "竞品或上一代页面", "追踪事件", "真实转化数据"],
            "C-DRY-007",
            "dryrun://handoff/S07-dtc-conversion",
        ),
        "activation_return_risk": section(
            "activation_return_risk",
            "S09.predict-activation-risk",
            "激活、退货与上手风险",
            "S09 当设置、配对、尺寸、安装、兼容或预期落差影响采用时，用硬件旅程拆解激活和退货风险。",
            [
                visual(
                    "s09-trigger-check",
                    "status_panel",
                    "激活与退货触发检查",
                    "activation_return_trigger_check",
                    items=status_items(
                        [
                            ("设置/配对", "待确认", "产品如有应用、网络或账号设置则触发。"),
                            ("尺寸/安装", "待确认", "佩戴、安装、尺寸或兼容要求会影响退货。"),
                            ("预期落差", "样例风险", "来自 S03 主张和 S01 消费者声音。"),
                            ("退换政策", "缺真实输入", "需要本地渠道退换、保修和客服承诺。"),
                        ]
                    ),
                    note="如果正式产品没有这些风险，S09 可保持低权重；如果有，则进入 S13 验证。",
                ),
                visual(
                    "s09-journey-risk",
                    "matrix_heatmap",
                    "上手旅程风险图",
                    "activation_journey_risk_map",
                    rows=[
                        {"旅程阶段": "购买前", "风险": "预期过高或规格误解", "风险分": 72, "预防动作": "页面和导购明确适用条件"},
                        {"旅程阶段": "开箱", "风险": "配件、尺寸或说明不清", "风险分": 64, "预防动作": "首屏说明和包装内上手卡"},
                        {"旅程阶段": "设置/配对", "风险": "应用、账号、网络或兼容失败", "风险分": 78, "预防动作": "快速教程、兼容清单和客服入口"},
                        {"旅程阶段": "前 7 天", "风险": "体验低于承诺或习惯未形成", "风险分": 69, "预防动作": "提醒、教育内容和可见成就"},
                    ],
                    note="风险分 = 发生概率 30% + 退货影响 30% + 体验损伤 20% + 可预防性 20%。",
                    wide=True,
                ),
                visual(
                    "s09-return-prevention",
                    "ranked_bar",
                    "退货预防动作优先级",
                    "return_prevention_priority",
                    items=[
                        {"label": "兼容与适用条件说明", "score": 82},
                        {"label": "开箱上手卡与视频教程", "score": 76},
                        {"label": "首周使用教育", "score": 68},
                        {"label": "客服和退换政策入口", "score": 64},
                    ],
                    note="优先做能降低误购、误设和预期落差的动作。",
                ),
            ],
            [
                {
                    "table_id": "s09-method",
                    "title": "S09触发规则与输入",
                    "rows": [
                        {"触发": "设置、配对、尺寸、安装、兼容或退货风险", "输入": "说明书、兼容规则、退换政策、上一代退货原因", "输出": "激活风险图和退货预防计划"},
                        {"触发": "健康、安全、儿童或老人相邻体验", "输入": "安全说明、适用人群、主张边界", "输出": "传给 S10 的护栏输入"},
                    ],
                }
            ],
            ["设置流程", "兼容规则", "退换政策", "上一代退货原因"],
            "C-DRY-009",
            "dryrun://handoff/S09-activation-risk",
        ),
        "insight_guardrails": section(
            "insight_guardrails",
            "S10.generate-health-insights",
            "洞察、健康、安全或高风险主张护栏",
            "S10 当产品涉及健康、安全、AI 洞察、隐私、儿童或老人场景时，定义能说、不能说、需要证明和需要法务确认的边界。",
            [
                visual(
                    "s10-trigger-check",
                    "status_panel",
                    "主张风险触发检查",
                    "insight_claim_trigger_check",
                    items=status_items(
                        [
                            ("健康/安全主张", "待确认", "涉及身体、健康、儿童或老人时触发。"),
                            ("AI 洞察", "待确认", "涉及建议、诊断、预测或自动解释时触发。"),
                            ("隐私数据", "样例风险", "穿戴、应用或云服务通常需要数据边界。"),
                            ("合规约束", "缺真实输入", "需要批准说法、禁用词和当地法规线索。"),
                        ]
                    ),
                    note="S10 不做法律意见，只把主张边界、证明要求和复核队列显性化。",
                ),
                visual(
                    "s10-claim-guardrail",
                    "matrix_heatmap",
                    "主张风险护栏矩阵",
                    "claim_guardrail_matrix",
                    rows=[
                        {"主张类型": "性能/准确性", "风险分": 70, "允许表达": "描述测试条件和相对改善", "禁止方向": "绝对化或无条件保证"},
                        {"主张类型": "健康/安全", "风险分": 88, "允许表达": "教育性和辅助性描述", "禁止方向": "诊断、治疗或医疗承诺"},
                        {"主张类型": "AI 洞察", "风险分": 76, "允许表达": "趋势、提醒和解释", "禁止方向": "替代专业判断"},
                        {"主张类型": "隐私/数据", "风险分": 82, "允许表达": "数据用途、控制权和存储边界", "禁止方向": "未证明的绝对安全"},
                    ],
                    note="风险分越高，越需要证据、限定语和人工复核。",
                    wide=True,
                ),
                visual(
                    "s10-proof-needs",
                    "ranked_bar",
                    "隐私/安全证明需求",
                    "privacy_safety_proof_need",
                    items=[
                        {"label": "测试条件和证据来源", "score": 84},
                        {"label": "适用人群和限制说明", "score": 78},
                        {"label": "数据用途和用户控制", "score": 76},
                        {"label": "风险提示和客服路径", "score": 66},
                    ],
                    note="S10 输出会传给 S03/S05/S13，作为主张、文案和验证护栏。",
                ),
            ],
            [
                {
                    "table_id": "s10-method",
                    "title": "S10方法与边界",
                    "rows": [
                        {"步骤": "主张分类", "方法": "把性能、健康、安全、AI、隐私和适用人群主张分开处理。"},
                        {"步骤": "风险分级", "方法": "按监管相邻度、误导风险、证据强度和人群敏感性评分。"},
                        {"步骤": "护栏输出", "方法": "给 S03/S05 提供允许表达、禁止方向、限定语和复核队列。"},
                    ],
                }
            ],
            ["批准主张", "禁用词", "合规约束", "测试证据"],
            "C-DRY-010",
            "dryrun://handoff/S10-claim-guardrails",
        ),
        "subscription_churn": section(
            "subscription_churn",
            "S11.predict-subscription-and-churn",
            "订阅、留存与流失",
            "S11 当产品包含付费应用、订阅、耗材、延保或服务计划时，拆解留存价值、流失风险和续费验证。",
            [
                visual(
                    "s11-trigger-check",
                    "status_panel",
                    "订阅留存触发检查",
                    "subscription_retention_trigger_check",
                    items=status_items(
                        [
                            ("订阅/付费应用", "待确认", "有付费权益时触发。"),
                            ("延保/服务计划", "待确认", "影响定价、渠道和复购。"),
                            ("耗材/周期购买", "待确认", "会改变生命周期收入。"),
                            ("留存数据", "缺真实输入", "需要历史 cohort、使用频率或续费数据。"),
                        ]
                    ),
                    note="如果产品没有 recurring revenue，S11 只保留触发检查和数据缺口。",
                ),
                visual(
                    "s11-retention-driver",
                    "matrix_heatmap",
                    "留存价值驱动图",
                    "retention_value_driver_map",
                    rows=[
                        {"驱动": "持续洞察价值", "留存影响": 76, "证明难度": 70, "动作": "展示首月到三个月的价值累积"},
                        {"驱动": "服务/保修权益", "留存影响": 62, "证明难度": 48, "动作": "明确服务边界和响应承诺"},
                        {"驱动": "生态或应用习惯", "留存影响": 68, "证明难度": 64, "动作": "设计使用提醒和成就反馈"},
                    ],
                    note="留存价值需要和开盘价格、服务成本和激活体验一起判断。",
                ),
                visual(
                    "s11-churn-risk",
                    "ranked_bar",
                    "流失风险优先级",
                    "churn_risk_priority",
                    items=[
                        {"label": "首月价值感不足", "score": 80},
                        {"label": "付费权益解释不清", "score": 72},
                        {"label": "应用使用频率低", "score": 68},
                        {"label": "服务成本与权益错配", "score": 60},
                    ],
                    note="流失风险应回到 S13 做续费意愿、权益理解和使用频率验证。",
                ),
            ],
            [
                {
                    "table_id": "s11-method",
                    "title": "S11输入与方法",
                    "rows": [
                        {"输入": "订阅或服务权益", "方法": "拆成价值驱动、成本压力、续费触发和取消原因。"},
                        {"输入": "历史 cohort 或应用使用", "方法": "用于校准留存曲线；没有则只输出假设和验证计划。"},
                        {"输入": "价格与促销", "方法": "结合 S04 判断免费期、捆绑、分期和续费风险。"},
                    ],
                }
            ],
            ["订阅权益", "留存数据", "服务成本", "续费或取消原因"],
            "C-DRY-011",
            "dryrun://handoff/S11-subscription-churn",
        ),
        "review_quality_feedback": section(
            "review_quality_feedback",
            "S12.mine-review-quality-feedback",
            "评论、售后与质量反馈闭环",
            "S12 当有上市后评论、上一代评论、客服、退货、RMA 或净推荐相关数据时，把质量问题和 GTM 问题分流到产品、客服、渠道和下一代营销。",
            [
                visual(
                    "s12-trigger-check",
                    "status_panel",
                    "反馈闭环触发检查",
                    "feedback_loop_trigger_check",
                    items=status_items(
                        [
                            ("上市后评论", "缺真实输入", "新产品未上市时可用上一代或 beta 评论。"),
                            ("客服/退货/RMA", "缺真实输入", "用于区分质量、设置、渠道和误购。"),
                            ("净推荐相关输入", "可选输入", "可和 S01 的净推荐 proxy 种子对齐。"),
                            ("应用商店评论", "条件触发", "有应用体验时进入反馈闭环。"),
                        ]
                    ),
                    note="S12 不把评论直接等同真实销量；它负责把反馈转成可行动 backlog 和证据图更新。",
                ),
                visual(
                    "s12-source-map",
                    "matrix_heatmap",
                    "评论/售后来源地图",
                    "review_support_source_map",
                    rows=[
                        {"来源": "零售评论", "能回答": "购买后满意/不满", "质量信号": 70, "用途": "卖点修正和退货风险"},
                        {"来源": "客服工单", "能回答": "设置、售后和质量根因", "质量信号": 76, "用途": "FAQ、教程和客服脚本"},
                        {"来源": "RMA/退货", "能回答": "硬件质量或误购", "质量信号": 82, "用途": "质量闭环和渠道承诺"},
                        {"来源": "应用商店评论", "能回答": "应用体验和配对问题", "质量信号": 68, "用途": "应用改进和激活风险"},
                    ],
                    note="正式运行要保存原始记录引用，并按 source item 与 voice atom 分开计数。",
                    wide=True,
                ),
                visual(
                    "s12-quality-priority",
                    "ranked_bar",
                    "质量反馈主题优先级",
                    "quality_feedback_priority",
                    items=[
                        {"label": "设置/配对问题", "score": 78},
                        {"label": "可靠性或耐用性", "score": 74},
                        {"label": "价格价值不匹配", "score": 66},
                        {"label": "售后响应和退换体验", "score": 64},
                    ],
                    note="优先级按频次、情绪强度、退货影响、净推荐方向和跨来源一致性计算。",
                ),
                visual(
                    "s12-action-map",
                    "matrix_heatmap",
                    "闭环动作路线图",
                    "feedback_loop_action_map",
                    rows=[
                        {"问题类型": "质量根因", "负责人": "产品/质量", "动作": "进入缺陷或下一代改进", "优先级": 78},
                        {"问题类型": "误解或预期落差", "负责人": "营销/页面", "动作": "修正主张、FAQ 和导购话术", "优先级": 72},
                        {"问题类型": "渠道或售后摩擦", "负责人": "渠道/客服", "动作": "调整承诺、脚本和退换流程", "优先级": 68},
                    ],
                    note="S12 的输出会回流 S01-S04、S09 和下一代 GTM。",
                ),
            ],
            [
                {
                    "table_id": "s12-method",
                    "title": "S12反馈闭环方法",
                    "rows": [
                        {"步骤": "来源分层", "方法": "区分评论、客服、RMA、退货、应用评论和净推荐相关数据。"},
                        {"步骤": "根因分流", "方法": "把产品质量、设置教育、营销误解、渠道摩擦和售后问题分开。"},
                        {"步骤": "回流机制", "方法": "把可行动项回流到 S01-S04、S09 和下一代营销销售建议。"},
                    ],
                }
            ],
            ["上市后评论", "上一代评论", "客服/退货/RMA", "净推荐或应用评论"],
            "C-DRY-012",
            "dryrun://handoff/S12-review-feedback",
        ),
    }


def update_state(data: dict) -> dict:
    data["report_id"] = "通用硬件试跑：S00-S09 当前看板"
    data["purpose"] = "Current dry-run for validating S00 orchestration, S01-S09 analysis handoffs, and Chinese HTML dashboard composition without live web search."

    new_sections = build_sections()
    for index, item in enumerate(data["sections"]):
        section_id = item.get("section_id")
        if section_id in new_sections:
            data["sections"][index] = new_sections[section_id]

    for item in data["sections"]:
        if item.get("section_id") == "data_gap_panel":
            item["source_skill"] = "report_audit"
            item["executive_takeaway"] = "最终看板必须把未解决的数据缺口作为正文展示，避免把关键不确定性藏在附录里。"
            for block in item.get("visual_blocks", []):
                block["evidence_refs"] = ["dryrun://evidence/report-data-gaps"]
        if item.get("section_id") == "citation_index":
            item["source_skill"] = "report_audit"
            item["executive_takeaway"] = "引用索引用来区分试跑样例引用和真实证据，避免把合成样例内容误当成市场研究结论。"
            for block in item.get("visual_blocks", []):
                block["evidence_refs"] = ["dryrun://evidence/report-citations"]

    rendered_order = [
        "market_context",
        "jtbd_scenarios",
        "message_architecture",
        "pricing",
        "copy_assets",
        "creator_kol",
        "dtc_conversion",
        "launch_forecast",
        "activation_return_risk",
        "data_gap_panel",
        "citation_index",
    ]
    section_refs = {
        "copy_assets": ("S05.score-creative-assets", "dryrun://section/S05-copy-assets", "dryrun://handoff/S05-copy-assets", 4),
        "creator_kol": ("S06.score-kol-fit", "dryrun://section/S06-creator-kol", "dryrun://handoff/S06-creator-kol", 4),
        "dtc_conversion": ("S07.predict-dtc-conversion", "dryrun://section/S07-dtc-conversion", "dryrun://handoff/S07-dtc-conversion", 4),
        "activation_return_risk": ("S09.predict-activation-risk", "dryrun://section/S09-activation-risk", "dryrun://handoff/S09-activation-risk", 3),
    }
    existing_drafts = {item["section_id"]: item for item in data["html_section_drafts"]}
    drafts = []
    for section_id in rendered_order:
        if section_id in section_refs:
            source_skill, section_ref, handoff_ref, count = section_refs[section_id]
            drafts.append(
                {
                    "section_id": section_id,
                    "source_skill": source_skill,
                    "html_section_ref": section_ref,
                    "handoff_ref": handoff_ref,
                    "status": "rendered_with_gaps",
                    "visual_block_count": count,
                }
            )
        elif section_id in existing_drafts:
            drafts.append(existing_drafts[section_id])
    data["html_section_drafts"] = drafts

    for number, section_id, source_skill in [
        (5, "copy_assets", "S05.score-creative-assets"),
        (6, "creator_kol", "S06.score-kol-fit"),
        (7, "dtc_conversion", "S07.predict-dtc-conversion"),
        (9, "activation_return_risk", "S09.predict-activation-risk"),
    ]:
        citation_id = f"C-DRY-{number:03d}"
        if not any(item.get("citation_id") == citation_id for item in data["citation_index"]):
            data["citation_index"].append(
                {
                    "citation_id": citation_id,
                    "source": f"dryrun://fixture/{section_id}",
                    "type": "synthetic_fixture",
                    "used_by": [section_id],
                    "quality_label": "not_real_evidence",
                }
            )
        evidence_ref = f"dryrun://evidence/S{number:02d}-fixture"
        if not any(item.get("ref") == evidence_ref for item in data["evidence_ledger_refs"]):
            data["evidence_ledger_refs"].append(
                {
                    "ref": evidence_ref,
                    "source_skill": source_skill,
                    "evidence_type": "synthetic_fixture",
                    "quality": "fixture_only",
                }
            )

    hidden_citation_ids = {"C-DRY-010", "C-DRY-011", "C-DRY-012", "C-DRY-013"}
    data["citation_index"] = [item for item in data["citation_index"] if item.get("citation_id") not in hidden_citation_ids]
    hidden_evidence_refs = {
        "dryrun://evidence/S10-fixture",
        "dryrun://evidence/S11-fixture",
        "dryrun://evidence/S12-fixture",
        "dryrun://evidence/S13-fixture",
    }
    data["evidence_ledger_refs"] = [item for item in data["evidence_ledger_refs"] if item.get("ref") not in hidden_evidence_refs]

    new_gaps = [
        ("DG-002", "S02.mine-jtbd-scenarios", "当前没有真实消费者声音原子、本地语言表达、净推荐相关数据、评论或论坛留言。", "high", ["jtbd_scenarios", "message_architecture"], "采集公开评论、本地论坛帖子、视频评论，并可选加入私密净推荐相关材料。"),
        ("DG-006", "S05.score-creative-assets", "缺少可编辑文案、品牌语气、渠道格式和批准主张。", "medium", ["copy_assets"], "上传标题、PDP 要点、落地页文字、广告文案、品牌语气和渠道格式。"),
        ("DG-007", "S06.score-kol-fit", "缺少本地创作者候选、预算范围、目标平台和竞品创作者历史。", "medium", ["creator_kol", "launch_forecast"], "补充平台、预算、候选或允许联网发现本地创作者和竞品内容。"),
        ("DG-008", "S07.predict-dtc-conversion", "缺少页面文字、竞品/上一代页面、追踪事件和真实转化数据。", "medium", ["dtc_conversion", "launch_forecast"], "上传页面文字或 URL、竞品/上一代页面、流量来源和追踪事件。"),
        ("DG-009", "S09.predict-activation-risk", "缺少设置流程、兼容规则、退换政策和上一代退货原因。", "medium", ["activation_return_risk"], "补充说明书、上手流程、兼容清单、退换政策或售后资料。"),
    ]
    hidden_gap_ids = {"DG-005", "DG-010", "DG-011", "DG-012"}
    data["data_gap_log"] = [item for item in data["data_gap_log"] if item.get("gap_id") not in hidden_gap_ids]
    existing_gaps = {item.get("gap_id"): item for item in data["data_gap_log"]}
    for gap_id, source_skill, gap, severity, blocks, resolution in new_gaps:
        entry = {
            "gap_id": gap_id,
            "source_skill": source_skill,
            "gap": gap,
            "severity": severity,
            "blocks": blocks,
            "recommended_resolution": resolution,
        }
        if gap_id in existing_gaps:
            existing_gaps[gap_id].update(entry)
        else:
            data["data_gap_log"].append(
                entry
            )

    data["decision_log"] = [
        data["decision_log"][0],
        {
            "decision_id": "DL-002",
            "decision": "Render S05, S06, and S07 as prelaunch completion drafts with explicit gaps.",
            "reason": "The user wants all gaps filled before a single-pass audit; optional modules remain evidence-light but visible.",
        },
        {
            "decision_id": "DL-003",
            "decision": "当前看板只展示到 S09，S10-S13 暂不进入正文。",
            "reason": "S10-S13 仍保留在系统架构中，但本轮看板先聚焦上市前主链路和激活退货风险。",
        },
        data["decision_log"][3],
    ]

    summary = data.get("management_summary", {})
    for block in summary.get("decision_blocks", []):
        if block.get("title") == "下一步验证动作":
            block["points"] = [
                "运行 S01 联网采集，确认本地电商、搜索词、论坛和竞品名单。",
                "运行价格与信息小样本测试，刷新周均销量和 MKT 分配。",
                "用户如提供上一代销量或渠道数据，优先重算 S08 预测。",
            ]

    packs = {item["skill_id"]: item for item in data["compressed_handoff_packs"]}
    for skill_id, ref, downstream, fields in [
        ("S05", "dryrun://handoff/S05-copy-assets", ["S06", "S07", "S13", "S14"], ["copy_input_coverage_gate", "copy_message_fit_scorecard", "channel_copy_fit_matrix", "copy_test_backlog", "data_gaps"]),
        ("S06", "dryrun://handoff/S06-creator-kol", ["S07", "S08", "S13", "S14"], ["creator_archetype_fit_scorecard", "creator_budget_estimate", "creator_expected_outcome_estimate", "brand_safety_risk_review", "creator_test_backlog", "data_gaps"]),
        ("S07", "dryrun://handoff/S07-dtc-conversion", ["S08", "S13", "S14"], ["conversion_input_coverage_gate", "competitor_previous_page_benchmark", "funnel_friction_scorecard", "page_experiment_plan", "tracking_readiness_audit", "data_gaps"]),
        ("S09", "dryrun://handoff/S09-activation-risk", ["S10", "S12", "S13", "S14"], ["activation_return_trigger_check", "activation_journey_risk_map", "return_prevention_priority", "data_gaps"]),
        ("S10", "dryrun://handoff/S10-claim-guardrails", ["S11", "S13", "S14"], ["insight_claim_trigger_check", "claim_guardrail_matrix", "privacy_safety_proof_need", "data_gaps"]),
        ("S11", "dryrun://handoff/S11-subscription-churn", ["S12", "S13", "S14"], ["subscription_retention_trigger_check", "retention_value_driver_map", "churn_risk_priority", "data_gaps"]),
        ("S12", "dryrun://handoff/S12-review-feedback", ["S01", "S02", "S03", "S09", "S13", "S14"], ["feedback_loop_trigger_check", "review_support_source_map", "quality_feedback_priority", "feedback_loop_action_map", "data_gaps"]),
    ]:
        packs[skill_id] = {"skill_id": skill_id, "ref": ref, "allowed_downstream": downstream, "canonical_fields": fields}
    data["compressed_handoff_packs"] = [packs[item] for item in ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10", "S11", "S12", "S13"] if item in packs]

    records = {item["skill_id"]: item for item in data["post_skill_isolation_records"]}
    for skill_id, artifact, handoff, section_ref, withheld, reopen in [
        ("S05", "dryrun://artifacts/S05-copy-full", "dryrun://handoff/S05-copy-assets", "dryrun://section/S05-copy-assets", ["原始文案草稿", "被放弃的文案变体", "私密品牌说明"], ["上传新的可编辑文案", "品牌语气变化", "主张审核结果变化"]),
        ("S06", "dryrun://artifacts/S06-creator-full", "dryrun://handoff/S06-creator-kol", "dryrun://section/S06-creator-kol", ["原始创作者长名单", "报价卡细节", "品牌安全备注"], ["新增创作者候选", "预算变化", "目标平台变化"]),
        ("S07", "dryrun://artifacts/S07-conversion-full", "dryrun://handoff/S07-dtc-conversion", "dryrun://section/S07-dtc-conversion", ["原始页面抓取", "分析数据导出", "私密漏斗备注"], ["提供页面链接或文字", "可获得分析数据", "优惠或权益变化"]),
        ("S09", "dryrun://artifacts/S09-activation-full", "dryrun://handoff/S09-activation-risk", "dryrun://section/S09-activation-risk", ["原始上手说明", "客服细节", "退换政策草稿"], ["上手流程变化", "可获得退货数据", "出现兼容问题"]),
        ("S10", "dryrun://artifacts/S10-guardrails-full", "dryrun://handoff/S10-claim-guardrails", "dryrun://section/S10-claim-guardrails", ["原始主张草稿", "法务备注", "敏感证据"], ["新增敏感主张", "合规约束变化", "证明来源变化"]),
        ("S11", "dryrun://artifacts/S11-subscription-full", "dryrun://handoff/S11-subscription-churn", "dryrun://section/S11-subscription-churn", ["原始留存 cohort 数据", "服务成本备注", "账单细节"], ["新增订阅或服务计划", "提供留存数据", "定价模型变化"]),
        ("S12", "dryrun://artifacts/S12-feedback-full", "dryrun://handoff/S12-review-feedback", "dryrun://section/S12-review-feedback", ["原始评论", "客服工单", "RMA 记录", "净推荐原文"], ["上传上市后反馈", "出现质量问题", "可获得新的评论语料"]),
    ]:
        records[skill_id] = {
            "skill_id": skill_id,
            "status": "isolated_with_gaps",
            "full_artifact_ref": artifact,
            "compressed_handoff_ref": handoff,
            "html_section_ref": section_ref,
            "allowed_downstream_refs": [handoff, section_ref],
            "withheld_context": withheld,
            "reopen_conditions": reopen,
            "quality_gate_status": "pass_with_caveats",
        }
    data["post_skill_isolation_records"] = [records[item] for item in ["S00", "S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09"] if item in records]

    qg = data["quality_gate_summary"]
    qg["checks"] = [
        {"gate": "required_top_level_fields", "status": "pass"},
        {"gate": "post_skill_isolation_records_present", "status": "pass"},
        {"gate": "S05_S07_prelaunch_sections_rendered", "status": "pass"},
        {"gate": "S09_activation_section_rendered", "status": "pass_with_caveats", "note": "S09 已作为激活与退货风险草案渲染，并展示明确缺口。"},
        {"gate": "S10_S13_hidden_from_current_dashboard", "status": "pass", "note": "S10-S13 保留为系统能力，但当前看板不展示。"},
        {"gate": "dashboard_composer_hidden_as_module", "status": "pass", "note": "最终合成器只生成看板，不作为模块展示。"},
        {"gate": "no_live_web_contamination", "status": "pass"},
        {"gate": "raw_private_inputs_not_embedded", "status": "pass"},
        {"gate": "context_budget", "status": "pass_with_caveats", "note": "试跑只使用合成 handoff 引用，尚未测量真实上下文预算。"},
    ]
    qg["rendered_sections"] = rendered_order
    qg["skipped_sections"] = []
    qg["future_sections_omitted"] = []
    qg["visual_block_count"] = 49
    qg["isolation_record_count"] = 10
    qg["validation_warnings"] = [
        "所有证据均为合成试跑样例数据。",
        "未执行真实联网 MCP 搜索。",
        "未嵌入私密商业输入。",
        "S05-S09 已作为可审核草案渲染，并展示明确数据缺口。",
        "S10-S13 暂不进入当前看板正文。",
    ]

    return data


def main() -> None:
    data = json.loads(STATE.read_text(encoding="utf-8"))
    data = update_state(data)
    STATE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
