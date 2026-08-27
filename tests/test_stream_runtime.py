from __future__ import annotations

import importlib.util
import unittest
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / ".profile-signal" / "src" / "stream_runtime.py"
SPEC = importlib.util.spec_from_file_location("profile_signal_stream_runtime_test", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
stream = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(stream)


class StreamRuntimeTests(unittest.TestCase):
    def test_merge_dynamic_state_preserves_heavy_analytics(self) -> None:
        existing = {
            "schema_version": 4,
            "status": {"label": "OFFLINE"},
            "activity_stream": [{"title": "old"}],
            "ci_signal": {"label": "PASSING"},
            "dev_recap": {"tracked_days": 4},
            "now_building": [{"repo": "example/repo", "health": {"label": "HEALTHY"}}],
        }
        fresh = {
            "schema_version": 2,
            "status": {"label": "BUILDING"},
            "activity_stream": [{"title": "new"}],
            "current_focus": {"repo": "example/new"},
        }

        merged = stream.merge_dynamic_state(existing, fresh)

        self.assertEqual(merged["schema_version"], 4)
        self.assertEqual(merged["status"]["label"], "BUILDING")
        self.assertEqual(merged["activity_stream"][0]["title"], "new")
        self.assertEqual(merged["ci_signal"]["label"], "PASSING")
        self.assertEqual(merged["dev_recap"]["tracked_days"], 4)
        self.assertEqual(merged["now_building"][0]["health"]["label"], "HEALTHY")

    def test_replace_marker_updates_only_target_block(self) -> None:
        start = "<!-- START -->"
        end = "<!-- END -->"
        text = f"before\n{start}\nold\n{end}\nafter\n"
        updated = stream.replace_marker(text, start, end, f"{start}\nnew\n{end}")
        self.assertEqual(updated, f"before\n{start}\nnew\n{end}\nafter\n")

    def test_updated_at_note_is_inserted_before_end_marker(self) -> None:
        end = "<!-- END -->"
        block = f"<!-- START -->\nbody\n{end}"
        now = datetime(2026, 8, 27, 12, 34, tzinfo=ZoneInfo("Asia/Tokyo"))
        updated = stream.with_updated_at(block, end, now)
        self.assertIn("latest public signal refresh · 12:34 JST", updated)
        self.assertTrue(updated.endswith(end))


if __name__ == "__main__":
    unittest.main()
