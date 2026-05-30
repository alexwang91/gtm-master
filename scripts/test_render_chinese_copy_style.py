from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RENDERER = ROOT / "scripts" / "render-gtm-dashboard-from-report-state.py"


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
        self.assertIsNone(re.search(r"不是[^。；，]*而是", html))


if __name__ == "__main__":
    unittest.main()
