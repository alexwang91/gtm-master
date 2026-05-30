from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RENDERER = ROOT / "scripts" / "render-gtm-dashboard-from-report-state.py"


class S01VoiceSourceMapRenderTest(unittest.TestCase):
    def test_market_context_renders_voice_source_map_and_storage_strategy(self) -> None:
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
            "本地消费者声音来源地图",
            "示例本地论坛一号",
            "示例视频评论入口",
            "示例零售评论入口",
            "访问状态",
            "采集角色",
            "本地 MD 原文库",
            "原始声音保存与压缩策略",
            "只传压缩主题簇",
            "NSS/NPS 种子适用性",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, html)

        self.assertGreaterEqual(html.count("visual-card visual-card-wide"), 3)


if __name__ == "__main__":
    unittest.main()
