from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RENDERER = ROOT / "scripts" / "render-gtm-dashboard-from-report-state.py"


class ManagementSummaryRenderTest(unittest.TestCase):
    def test_dashboard_renders_compact_gtm_summary(self) -> None:
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
            "GTM判断",
            "期望周均销量",
            "MKT 投放建议",
            "渠道优先级",
            "核心竞品攻防",
            "下一步验证动作",
            "示例电商一号",
            "示例电器零售二号",
            "示例运营商三号",
            "渠道名与角色",
            "会改变结论的问题",
            "来源治理",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, html)

        self.assertNotIn("完整链路试跑", html)
        self.assertNotIn("管理层摘要", html)
        self.assertNotIn("方法论行动方向", html)
        self.assertNotIn("已确认输入", html)
        self.assertNotIn("本地电商 > 零售 > 自营", html)


if __name__ == "__main__":
    unittest.main()
