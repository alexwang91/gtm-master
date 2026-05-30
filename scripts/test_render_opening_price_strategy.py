from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RENDERER = ROOT / "scripts" / "render-gtm-dashboard-from-report-state.py"


class OpeningPriceStrategyRenderTest(unittest.TestCase):
    def test_dashboard_renders_opening_price_strategy_views(self) -> None:
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
            "开盘价格策略",
            "上市价格架构",
            "收入最大点",
            "利润最大点",
            "30/60/90 价格路径",
            "私密利润与收入优化器",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, html)


if __name__ == "__main__":
    unittest.main()
