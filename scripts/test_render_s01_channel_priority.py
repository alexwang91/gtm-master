from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RENDERER = ROOT / "scripts" / "render-gtm-dashboard-from-report-state.py"


class S01ChannelPriorityRenderTest(unittest.TestCase):
    def test_market_context_renders_named_local_channel_priority(self) -> None:
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
            "本地渠道发现与优先级",
            "渠道发现评分逻辑",
            "示例电商一号",
            "示例电器零售二号",
            "示例运营商三号",
            "价格同屏、竞品比较、转化测试",
            "证据状态",
            "正式运行需联网确认",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, html)


if __name__ == "__main__":
    unittest.main()
