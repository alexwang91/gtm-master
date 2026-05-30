from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RENDERER = ROOT / "scripts" / "render-gtm-dashboard-from-report-state.py"


class S01SearchCompetitorDiscoveryRenderTest(unittest.TestCase):
    def test_market_context_renders_local_search_and_competitor_discovery(self) -> None:
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
            "本地搜索词与需求语言地图",
            "竞品发现与初排候选",
            "本地搜索词与竞品发现方法",
            "示例搜索词一",
            "示例比较词二",
            "示例直接竞品 A",
            "示例高价锚点 B",
            "价格带重叠",
            "用户校准",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, html)
        self.assertGreaterEqual(html.count("visual-card visual-card-wide"), 2)


if __name__ == "__main__":
    unittest.main()
