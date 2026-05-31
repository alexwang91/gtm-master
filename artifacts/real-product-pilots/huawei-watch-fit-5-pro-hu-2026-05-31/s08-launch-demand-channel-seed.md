# S08 上市需求预测与渠道种子

Run id: `huawei-watch-fit-5-pro-hu-2026-05-31`
Mode: `real_product_pilot`
产品: HUAWEI WATCH FIT 5 Pro
国家: 匈牙利
预测边界: `reachable_launch_demand` 与渠道分配种子
状态: `directional_only`

## 输入覆盖门禁

| 输入组 | 状态 | 结论 |
|---|---|---|
| 国家/产品/价格 | pass | 匈牙利、FIT 5 Pro、约 `99,990 Ft`。 |
| 渠道上下文 | partial | Huawei official、Alza、MediaMarkt、Euronics、Yettel、Arukereso 可见；Telekom/One 未确认。 |
| 价格模型 | pass_with_caveat | S04 给出 `58/100` 价格可信度，需证明和 bundle 支撑。 |
| 人群/JTBD | pass_with_caveat | S02 有场景种子，但没有真实 segment size。 |
| 市场规模/TAM | missing | 无法推导真实单位销量上限。 |
| 上一代销量/渠道表现 | missing_private | 无法校准 FIT 4 Pro 到 FIT 5 Pro 的动销速度。 |
| MKT 预算与媒体计划 | missing | 不能计算营销增量销量。 |
| 库存/渠道 PO | missing_private | 不能判断 stockout/overstock。 |

S08 当前可以输出：渠道优先级、假设树、相对需求场景、生命周期曲线、敏感性和需要验证的输入。

S08 当前不输出：真实 30/60/90 天单位销量、收入、ROAS、库存采购量。

## 预测公式

`Reachable Launch Unit Sales = addressable_segment_pool * launch_reach_or_channel_availability * segment_priority_weight * price_acceptance_factor * proof_and_trust_readiness_factor * conversion_or_action_rate_factor * lifecycle_phase_multiplier * marketing_response_factor * timing_and_competition_factor * supply_or_inventory_cap`

本次缺少 `addressable_segment_pool`、`conversion_or_action_rate_factor`、`marketing_response_factor`、`supply_or_inventory_cap` 的真实数据，所以只保留假设树。

## 假设树

| 因子 | 当前估计 | 置信 | 影响 |
|---|---|---|---|
| 渠道可达性 | medium | medium | 多渠道可见，但 operator 深度不足。 |
| 价格接受度 | medium_low | low | 99,990 Ft 需要强证明，Watch7 低价压制明显。 |
| 产品-任务适配 | medium_high | medium | 续航、轻薄、健康、睡眠、时尚适配较强。 |
| 证明成熟度 | medium_low | low | 官方规格强，本地买家声量弱。 |
| MKT 响应 | unknown | hypothesis_only | 没有预算、媒体、历史响应数据。 |
| 竞争压力 | high | medium | Watch7、FIT 4 Pro、GT 6 都会压价或分流。 |
| 库存约束 | unknown | hypothesis_only | 无库存/PO/补货周期。 |

## 相对需求场景

这里用“指数”替代单位销量：`Base 30-day reachable demand index = 100`。真实单位销量需要上一代销售或渠道承诺校准。

| 场景 | 30 天指数 | 60 天指数 | 90 天指数 | 条件 |
|---|---:|---:|---:|---|
| Conservative | 45-70 | 75-115 | 95-145 | 价格证明弱、支付 FAQ 不清、Watch7/GT6 压力强、operator 渠道有限。 |
| Base | 100 | 160-210 | 220-290 | Alza/MediaMarkt/Yettel/Huawei 同步清晰陈列，bundle 支撑，续航/支付证明上线。 |
| Upside | 135-175 | 240-330 | 360-480 | Yettel 或 operator bundle 放大，零售页证明强，KOL/PR 带来搜索和 PDP 流量，库存充足。 |

换算方式：

- 如果用户提供 `Base 30-day target = X units`，则 Conservative 30 天为 `0.45X-0.70X`，Base 为 `X`，Upside 为 `1.35X-1.75X`。
- 如果用户提供 FIT 4 Pro 同期 sell-through，可用它替代 `X` 做校准。

## 生命周期曲线

| 阶段 | 30/60/90 角色 | 销售占比假设 | 关键动作 |
|---|---|---:|---|
| Prelaunch / warmup | 上线前与上市前 1-2 周 | 0-10% | 评测、渠道 PDP、支付 FAQ、KOL 种草、Arukereso/Google 搜索铺底。 |
| Launch spike | 首发 1-2 周 | 25-35% | Huawei official、Alza、MediaMarkt、Yettel 同步开售，bundle 权益明确。 |
| Early ramp | D15-D45 | 30-40% | 评测内容发酵，搜索/retargeting/零售 media，用户评论积累。 |
| Sustain | D46-D90 | 20-30% | 价格机制优化、渠道补货、节日/工资周期促销。 |
| Plateau / decay | 90 天后 | 10-20% | 若证明不足或竞品促销加剧，需求转为价格驱动。 |

## 渠道分配种子

| 渠道 | 本地名称 | 角色 | 90 天份额假设 | 置信 | 备注 |
|---|---|---|---:|---|---|
| retailer_ecommerce/offline | Alza + MediaMarkt + Euronics | 主成交和证明渠道 | 35-50% | medium | 适合承接主动搜索和对比人群。 |
| operator_partner | Yettel | bundle/资费/分期线索 | 15-25% | medium | FIT 5 Pro + FreeBuds SE 4 已可见；可做低摩擦成交。 |
| brand_dtc | Huawei official store | 官方信任和新品锚点 | 10-20% | medium_low | 需要清楚呈现价格、赠品、支付和权益。 |
| price_comparison | Arukereso | 搜索比较和价格流量 | indirect | high | 不是最终渠道，但会决定价格心智和 merchant 选择。 |
| marketplace/other | KOKU、eMAG/其他商家 | 补充成交 | 5-15% | low | 需管控低价/错误 listing 对信任的伤害。 |
| operator_partner | Telekom / One | 待确认 | 0-15% | hypothesis_only | 当前未确认 FIT 5 Pro；如上线，份额和预算策略要重算。 |

## Budget Posture Model

| 预算姿态 | 预算范围 | 可做什么 | 对销量模型的影响 |
|---|---:|---|---|
| proof_minimum | `5k-10k USD` | 本地支付 FAQ、零售页内容、短视频素材、1-2 个评测/KOL | 提高证明成熟度，不足以显著放大需求。 |
| standard_growth | `20k-40k USD` | 搜索/社媒/retail media/KOL 小组合，覆盖 30-60 天 | 可用于 Base 场景，但仍需转化数据校准。 |
| aggressive_launch | `50k+ USD` | PR/KOL + paid social/search + retail media + bundle 联动 | 可测试 Upside，但要看库存、渠道和价格接受度。 |

当前 MKT 输入缺失，所以 budget posture 只作为预算建议，不进入单位销量计算。

## AARRR + ORB 渠道架构

| 阶段 | 本地渠道/触点 | ORB | 预算角色 | 衡量信号 |
|---|---|---|---|---|
| Acquisition | Google Search / Arukereso / paid social / local PR | rented/borrowed | primary_spend | 搜索量、CTR、PDP 访问、Arukereso 点击。 |
| Activation | Huawei official PDP、Alza/MediaMarkt/Euronics PDP、Yettel bundle page | owned/rented | proof_supply | FAQ 点击、支付设置页点击、零售跳转。 |
| Revenue | Yettel、Alza、MediaMarkt、Euronics、Huawei official | rented/owned | conversion | 加购、下单、分期选择、bundle 选择。 |
| Retention | Huawei Health、邮件/会员、保修/售后触点 | owned | support_spend | 激活率、退货、客服问题、App 设置失败。 |
| Referral | Arukereso reviews、Mobilarena、YouTube comments、retailer reviews | borrowed | proof_supply | 评论数量、正负主题、推荐语言、NSS proxy readiness。 |

## 敏感性排序

| 驱动 | 移动预测的能力 | 不确定性 | 为什么重要 |
|---|---:|---:|---|
| 渠道上线深度 | 88 | 62 | Telekom/One 或更多 operator 上线会明显改变可达需求。 |
| 价格接受度 | 84 | 70 | 99,990 Ft 高于多个锚点，证明不足会直接压转化。 |
| 支付/本地证明成熟度 | 82 | 65 | 评论已出现 OTP/支付疑问，影响首购信任。 |
| MKT 预算与响应 | 78 | 85 | 没有预算和历史响应，无法估算增量销量。 |
| Watch7 / GT 6 竞争促销 | 75 | 60 | 两者会分别从低价和内部长续航方向截流。 |
| 库存和补货 | 70 | 90 | 没有库存数据，无法判断缺货或压货。 |
| 上一代 FIT 4 Pro 降价 | 67 | 58 | 影响升级人群和渠道对比。 |

## 库存风险图

| 风险 | 当前状态 | 判断 |
|---|---|---|
| Stockout | unknown | 需要 launch inventory、渠道 allocation、补货周期。 |
| Overstock | unknown | 需要渠道 sell-in、30/60 天 sell-through 目标。 |
| Pull-forward | medium | bundle/赠品可能把早期需求提前，但 60-90 天回落。 |
| Cannibalization | high | FIT 4 Pro 和 GT 6 会在 Huawei 内部截流。 |
| Channel conflict | medium | 不同渠道价格/赠品若差异过大，会影响价格信任。 |

## 验证需求

如果要把 S08 从 `directional_only` 升级到可用于库存和预算决策，需要这些输入：

1. FIT 4 Pro 匈牙利首发 30/60/90 天 sell-through 或 sell-in。
2. FIT 5 Pro 计划库存、渠道分配、补货周期。
3. 各渠道上线状态：Huawei official、Alza、MediaMarkt、Euronics、Yettel、Telekom、One。
4. MKT 预算与阶段：paid social、search、retail media、KOL/PR、promo。
5. PDP 流量、加购、下单、retailer clickout。
6. 价格/赠品/分期测试结果。
7. 退货、客服、支付设置失败、App 激活数据。

## 决策门禁

当前状态：`directional_planning_ready`

可用于：

- 管理层看“哪里会拉动销量、哪里最危险”。
- S14 展示渠道优先级、敏感性和数据缺口。
- S13 规划价格/渠道/证明/MKT 验证。

不可用于：

- 采购库存数量。
- 承诺 30/60/90 天销量。
- 计算 ROAS。
- 决定渠道 PO 或 sell-in。

