# S06 HTML Section Example

Use this only when a concrete S06 report-section example, renderer fixture, or stakeholder preview is needed. Values below are illustrative placeholders, not real KOL recommendations, prices, or outcome forecasts.

## Example Section Draft

```json
{
  "section_id": "creator_kol",
  "source_skill": "S06.score-kol-fit",
  "section_title": "达人/KOL 适配与投放预估",
  "status": "rendered_with_gaps",
  "confidence": "low",
  "executive_takeaway": "本地创作者策略应优先验证专家评测与手把手演示两类角色。当前候选名单仍需用户确认，因此候选级评分、预算和预期访问/互动均为 provisional。",
  "narrative_blocks": [
    "S06 先用本地语言关键词、竞品重叠内容、专业媒体、论坛/社区、affiliate/deal 与零售内容来源生成候选池，再进入候选确认门。",
    "未被用户确认的候选人不得作为最终 KOL 建议；被排除的候选人不进入正式预算和预期结果估算。"
  ],
  "metric_cards": [
    {
      "label": "候选确认",
      "value": "待确认",
      "note": "8 个候选项等待 include / exclude / unsure / request_more_evidence"
    },
    {
      "label": "优先角色",
      "value": "专家评测 + 演示",
      "note": "适合高证明需求的 2C 硬件上市"
    },
    {
      "label": "预算口径",
      "value": "营销费用估算",
      "note": "达人费、样品、制作、投流、追踪与预备金"
    },
    {
      "label": "结果口径",
      "value": "区间预估",
      "note": "访问、播放、点赞、评论、收藏/分享；非保证结果"
    }
  ],
  "callouts": [
    {
      "title": "候选确认门",
      "body": "请先确认候选 KOL/媒体/社区作者。确认前，候选级推荐、预算区间和预期互动区间只能作为假设看待。",
      "tone": "warning"
    }
  ],
  "visual_blocks": [
    {
      "visual_block_id": "s06-review-gate",
      "source_skill": "S06.score-kol-fit",
      "type": "status_panel",
      "title": "候选 KOL 确认门",
      "subtitle": "先让用户修正候选池，再进入正式评分和预算预估",
      "data_source": "creator_candidate_review_gate",
      "items": [
        {
          "label": "确认状态",
          "value": "pending_user_review",
          "note": "候选级输出仍为 provisional"
        },
        {
          "label": "候选项",
          "value": "8",
          "note": "从本地搜索、竞品内容、专家媒体、论坛与 affiliate 来源生成"
        },
        {
          "label": "允许动作",
          "value": "include / exclude / unsure",
          "note": "也可 request_more_evidence"
        }
      ],
      "note": "候选确认前，不得把候选级预算和结果区间写成最终建议。",
      "evidence_refs": ["E06-discovery-coverage-001"],
      "confidence": "low"
    },
    {
      "visual_block_id": "s06-archetype-fit",
      "source_skill": "S06.score-kol-fit",
      "type": "ranked_bar",
      "title": "创作者角色适配优先级",
      "subtitle": "先选角色，再选具体人",
      "data_source": "creator_archetype_fit_scorecard",
      "items": [
        {
          "label": "专家/评测媒体",
          "score": 84,
          "note": "适合技术证明、竞品对比和价格合理性解释"
        },
        {
          "label": "手把手演示型创作者",
          "score": 78,
          "note": "适合安装、场景、使用前后对比和降低使用焦虑"
        },
        {
          "label": "社区/论坛权威用户",
          "score": 69,
          "note": "适合补充本地真实语气和长期使用信任"
        },
        {
          "label": "deal / affiliate 创作者",
          "score": 61,
          "note": "适合价格敏感测试，但品牌证明力较弱"
        }
      ],
      "evidence_refs": ["H03-message-pack", "H01-channel-seed"],
      "confidence": "medium"
    },
    {
      "visual_block_id": "s06-candidate-ranking",
      "source_skill": "S06.score-kol-fit",
      "type": "ranked_bar",
      "title": "候选适配评分（待确认）",
      "subtitle": "仅示例；用户 include 后才进入正式推荐",
      "data_source": "creator_candidate_fit_scorecard + creator_candidate_review_gate",
      "items": [
        {
          "label": "候选A：本地专家评测媒体",
          "score": 82,
          "note": "强证明能力；需确认报价、排期与竞品合作冲突"
        },
        {
          "label": "候选B：手把手演示创作者",
          "score": 76,
          "note": "适合使用场景演示；需要核验受众与近 90 天互动"
        },
        {
          "label": "候选C：论坛/社区作者",
          "score": 68,
          "note": "信任语言强；传播规模不确定"
        }
      ],
      "note": "pending_user_review 状态下，评分只能作为候选排序，不是最终选择。",
      "evidence_refs": ["E06-candidate-public-001", "E06-candidate-public-002"],
      "confidence": "low"
    },
    {
      "visual_block_id": "s06-budget-range",
      "source_skill": "S06.score-kol-fit",
      "type": "range_chart",
      "title": "KOL 营销预算区间",
      "subtitle": "营销费用估算，不是批准预算",
      "data_source": "creator_budget_estimate",
      "scale_min": 0,
      "scale_max": 12000,
      "items": [
        {
          "label": "Conservative",
          "min": 1800,
          "max": 3600,
          "marker": 2600,
          "value_label": "1,800-3,600"
        },
        {
          "label": "Base",
          "min": 4200,
          "max": 7200,
          "marker": 5600,
          "value_label": "4,200-7,200"
        },
        {
          "label": "Upside",
          "min": 8000,
          "max": 11500,
          "marker": 9400,
          "value_label": "8,000-11,500"
        }
      ],
      "note": "应包含达人费、样品、寄送、制作剪辑、投流放大、追踪与预备金；币种由项目 brief 或国家市场确定。",
      "evidence_refs": ["E06-rate-proxy-001"],
      "confidence": "hypothesis_only"
    },
    {
      "visual_block_id": "s06-expected-outcome-range",
      "source_skill": "S06.score-kol-fit",
      "type": "range_chart",
      "title": "预期访问与互动区间",
      "subtitle": "基于公开 proxy / benchmark 的方向性估算",
      "data_source": "creator_expected_outcome_estimate",
      "scale_min": 0,
      "scale_max": 120000,
      "items": [
        {
          "label": "播放/曝光",
          "min": 24000,
          "max": 110000,
          "marker": 62000,
          "value_label": "24k-110k"
        },
        {
          "label": "点赞",
          "min": 400,
          "max": 4200,
          "marker": 1800,
          "value_label": "400-4,200"
        },
        {
          "label": "评论",
          "min": 30,
          "max": 520,
          "marker": 160,
          "value_label": "30-520"
        },
        {
          "label": "点击/访问",
          "min": 180,
          "max": 2600,
          "marker": 950,
          "value_label": "180-2,600"
        }
      ],
      "note": "访问估算需要 tracking 或 landing page 上下文；没有归因数据时不得估算销量。",
      "evidence_refs": ["E06-public-metric-proxy-001"],
      "confidence": "low"
    },
    {
      "visual_block_id": "s06-risk-gate",
      "source_skill": "S06.score-kol-fit",
      "type": "status_panel",
      "title": "KOL 风险门",
      "subtitle": "品牌安全、披露、声明边界和数据质量",
      "data_source": "brand_safety_risk_review + sponsorship_disclosure_risk_review",
      "items": [
        {
          "label": "品牌安全",
          "value": "需复核",
          "note": "候选人历史内容和竞品合作仍需检查"
        },
        {
          "label": "广告披露",
          "value": "必须",
          "note": "遵守当地平台和广告披露规则"
        },
        {
          "label": "数据质量",
          "value": "Proxy",
          "note": "公开播放、点赞、评论只作为 proxy"
        }
      ],
      "evidence_refs": ["E06-risk-public-001"],
      "confidence": "low"
    }
  ],
  "tables": [
    {
      "title": "候选确认表",
      "headers": ["候选项", "类型", "为什么展示", "默认建议", "用户动作"],
      "rows": [
        ["候选A", "专家评测媒体", "本地语言专家内容 + 竞品评测重叠 + 强证明能力", "include", "待用户确认"],
        ["候选B", "手把手演示创作者", "适合展示安装/使用场景，能降低使用焦虑", "include", "待用户确认"],
        ["候选C", "论坛/社区作者", "本地社区信任语言强，但触达规模不确定", "unsure", "待用户确认"],
        ["候选D", "deal / affiliate", "可测试价格敏感与点击访问，但品牌证明弱", "request_more_evidence", "待用户确认"]
      ]
    },
    {
      "title": "推荐理由表",
      "headers": ["对象", "推荐理由", "不确定/反对理由", "预算理由", "预期理由"],
      "rows": [
        ["专家评测媒体", "能解释技术证明、竞品差异和价格合理性", "排期、报价和竞品合作冲突未知", "通常需要内容费 + 样品 + 可能的制作成本", "更可能带来高质量观看和深度评论"],
        ["演示创作者", "适合把卖点翻译成真实使用场景", "公开受众画像可能不可靠", "中等费用，可搭配少量投流放大", "更可能带来点赞、收藏、点击和使用问题评论"],
        ["论坛/社区作者", "能补充本地真实语气和长期信任", "规模和可控性较弱", "可能更偏样品/合作成本", "互动质量可能高，但访问规模不稳定"]
      ]
    },
    {
      "title": "预算假设拆分",
      "headers": ["费用项", "Conservative", "Base", "Upside", "说明"],
      "rows": [
        ["达人/媒体费用", "低", "中", "高", "取决于候选人报价或公开 rate proxy"],
        ["样品与寄送", "1-2 件", "2-4 件", "4+ 件", "硬件样品价值应单独记录"],
        ["制作/剪辑", "轻量", "标准", "多素材复用", "若创作者自带制作能力，可降低外部成本"],
        ["投流放大", "无或少量", "中等", "强放大", "只在素材通过 proof/risk gate 后增加"],
        ["追踪/落地页", "基础 UTM", "专属 landing", "多渠道归因", "影响访问和转化估算置信度"]
      ]
    }
  ],
  "next_actions": [
    "请用户对候选确认表逐项标记 include / exclude / unsure / request_more_evidence。",
    "对 include 候选收集报价、近 90 天公开内容表现、竞品合作冲突和披露要求。",
    "只有在 tracking/landing page 可用后，才把点击/访问和转化估算接入 S08。"
  ],
  "citations": [
    {
      "ref_id": "E06-discovery-coverage-001",
      "label": "S06 discovery coverage report"
    },
    {
      "ref_id": "E06-public-metric-proxy-001",
      "label": "Public metric proxy sample"
    }
  ],
  "data_gaps": [
    "pending_creator_candidate_review",
    "creator_candidate_review_decisions_missing",
    "missing_budget_basis",
    "missing_expected_metric_basis",
    "no_first_party_performance_data"
  ]
}
```

## Example User Decisions

When the user reviews the candidate list, store decisions like this:

```json
[
  {
    "candidate_ref": "candidate_a",
    "decision": "include",
    "reason": "专家评测能力强，适合证明核心卖点"
  },
  {
    "candidate_ref": "candidate_b",
    "decision": "include",
    "reason": "演示能力适合首发教育内容"
  },
  {
    "candidate_ref": "candidate_c",
    "decision": "unsure",
    "reason": "社区影响可能有价值，但需要更多互动质量证据"
  },
  {
    "candidate_ref": "candidate_d",
    "decision": "exclude",
    "reason": "品牌调性不匹配或风险较高"
  }
]
```

After decisions are applied:

```text
include -> enter formal candidate scoring, budget estimate, and expected outcome estimate
exclude -> stay in decision log; do not appear in recommendation or budget/outcome tables
unsure -> keep as hypothesis or evidence task; mark candidate-level outputs provisional
request_more_evidence -> create focused evidence task before scoring
```
