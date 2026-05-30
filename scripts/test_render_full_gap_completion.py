from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RENDERER = ROOT / "scripts" / "render-gtm-dashboard-from-report-state.py"


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = False
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style"}:
            self.skip = True

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"}:
            self.skip = False

    def handle_data(self, data: str) -> None:
        if not self.skip and data.strip():
            self.parts.append(" ".join(data.split()))


class FullGapCompletionRenderTest(unittest.TestCase):
    def test_dashboard_renders_current_review_scope_without_s10_s13_or_visible_s14_module(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "dashboard.html"
            result = subprocess.run(
                [sys.executable, str(RENDERER), "--output", str(output)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            html = output.read_text(encoding="utf-8")
            parser = VisibleTextParser()
            parser.feed(html)
            visible_text = "\n".join(parser.parts)

        required_phrases = [
            "文案资产",
            "文案输入覆盖门禁",
            "文案评分与修订需求",
            "KOL 与创作者策略",
            "创作者输入覆盖门禁",
            "KOL预算与预期结果",
            "DTC 转化与落地页诊断",
            "转化输入覆盖门禁",
            "竞品/上一代页面基准",
            "激活、退货与上手风险",
            "激活与退货触发检查",
            "上手旅程风险图",
            "数据缺口与置信度面板",
            "引用与证据索引",
            "可视块：49",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, visible_text)

        forbidden_phrases = [
            "S09 not implemented",
            "S10 not implemented",
            "S11 not implemented",
            "S12 not implemented",
            "Future Omitted",
            "未实现",
            "洞察、健康、安全或高风险主张护栏",
            "主张风险护栏矩阵",
            "订阅、留存与流失",
            "订阅留存触发检查",
            "评论、售后与质量反馈闭环",
            "反馈闭环触发检查",
            "验证路线图与实验优先级",
            "S10",
            "S11",
            "S12",
            "S13",
            "S14",
        ]
        for phrase in forbidden_phrases:
            self.assertNotIn(phrase, visible_text)


if __name__ == "__main__":
    unittest.main()
