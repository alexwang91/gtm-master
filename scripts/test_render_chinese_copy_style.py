from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import unittest
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RENDERER = ROOT / "scripts" / "render-gtm-dashboard-from-report-state.py"
DEFAULT_INPUT = ROOT / "artifacts" / "dry-runs" / "generic-hardware-s00-s08-s13-s14-report-state.json"


class ChineseCopyStyleRenderTest(unittest.TestCase):
    def test_dashboard_avoids_contrastive_not_but_frames(self) -> None:
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

        self.assertNotIn("而不是", html)
        self.assertIsNone(re.search(r"不是[^。；\n]{0,80}?而是", html))

    def test_renderer_softens_upstream_contrastive_frames(self) -> None:
        report_state = json.loads(DEFAULT_INPUT.read_text(encoding="utf-8"))
        report_state["management_summary"] = {
            "headline": "这不是市场结论，而是一次链路试跑",
            "confidence_note": "建议锁定购买场景，而不是泛泛地卖功能",
            "judgment_cards": [
                {"label": "价格", "value": "当前不是重新定价，而是证明价格接受度", "note": "测试口径"}
            ],
        }

        with tempfile.TemporaryDirectory() as tmp:
            input_path = Path(tmp) / "report-state.json"
            output = Path(tmp) / "dashboard.html"
            input_path.write_text(json.dumps(report_state, ensure_ascii=False), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(RENDERER), "--input", str(input_path), "--output", str(output)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            html = output.read_text(encoding="utf-8")

        self.assertNotIn("而不是", html)
        self.assertIsNone(re.search(r"不是[^。；\n]{0,80}?而是", html))
        self.assertIn("不宜理解为市场结论", html)
        self.assertIn("避免仅停留在泛泛地卖功能", html)


if __name__ == "__main__":
    unittest.main()
