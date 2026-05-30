from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RENDERER = ROOT / "scripts" / "render-gtm-dashboard-from-report-state.py"


class S01Top1PreviousGenBainVoiceRenderTest(unittest.TestCase):
    def test_market_context_renders_top1_previous_gen_full_voice_bain_panel(self) -> None:
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

        required_phrases = [
            "TOP1竞品与上一代产品声音深挖范围",
            "示例TOP1竞品",
            "示例上一代产品",
            "观点全量采集覆盖报告",
            "一条不漏",
            "贝恩NSS/NPS与硬件旅程评分种子面板",
            "痛点",
            "赞美点",
            "购买触发",
            "购买",
            "开箱",
            "使用",
            "Driver Impact Score",
            "推广者型",
            "贬损者型",
            "硬件适配",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, html)

        internal_codes = [
            "promoter_like",
            "detractor_like",
            "product.accuracy_or_reliability",
            "product.design_or_comfort",
            "price.value_for_money",
            "service.return_or_warranty",
        ]
        for code in internal_codes:
            self.assertNotIn(code, html)

        self.assertGreaterEqual(html.count("visual-card visual-card-wide"), 5)


if __name__ == "__main__":
    unittest.main()
