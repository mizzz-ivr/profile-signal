import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".profile-signal" / "scripts"))

import profile_signal_writing as writing


QIITA_PAYLOAD = [
    {
        "title": "公開記事 [その1]",
        "url": "https://qiita.com/mizzz-ivr/items/aaa",
        "created_at": "2026-11-13T22:26:28+09:00",
        "likes_count": 5,
        "private": False,
        "tags": [{"name": "AWS"}, {"name": "Terraform"}, {"name": "CI"}, {"name": "Extra"}],
    },
    {
        "title": "限定共有の下書き",
        "url": "https://qiita.com/mizzz-ivr/items/bbb",
        "created_at": "2026-11-12T10:00:00+09:00",
        "likes_count": 0,
        "private": True,
        "tags": [],
    },
    {
        "title": "2本目",
        "url": "https://qiita.com/mizzz-ivr/items/ccc",
        "created_at": "2026-11-10T09:00:00+09:00",
        "likes_count": 0,
        "private": False,
        "tags": [],
    },
]

ZENN_RSS = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
<title>Zenn feed</title>
<item><title>Zenn記事1</title><link>https://zenn.dev/mizzz-ivr/articles/xxx</link><pubDate>Fri, 14 Nov 2026 01:00:00 GMT</pubDate></item>
<item><title>Zenn記事2</title><link>https://zenn.dev/mizzz-ivr/articles/yyy</link><pubDate>Thu, 13 Nov 2026 01:00:00 GMT</pubDate></item>
</channel></rss>
"""


def fake_opener(url: str) -> bytes:
    if "qiita.com" in url:
        return json.dumps(QIITA_PAYLOAD).encode("utf-8")
    if "zenn.dev" in url:
        return ZENN_RSS.encode("utf-8")
    raise AssertionError(f"unexpected url: {url}")


def failing_opener(url: str) -> bytes:
    raise OSError("network down")


class WritingWidgetTest(unittest.TestCase):
    def test_qiita_fetch_filters_private_items(self) -> None:
        items = writing.fetch_qiita_items("mizzz-ivr", 3, fake_opener)
        self.assertEqual([item["title"] for item in items], ["公開記事 (その1)", "2本目"])
        self.assertEqual(items[0]["date"], "2026-11-13")
        self.assertEqual(items[0]["likes"], 5)
        self.assertEqual(items[0]["tags"], ["AWS", "Terraform", "CI", "Extra"])

    def test_zenn_fetch_parses_rss(self) -> None:
        items = writing.fetch_zenn_items("mizzz-ivr", 3, fake_opener)
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]["title"], "Zenn記事1")
        self.assertEqual(items[0]["date"], "2026-11-14")
        self.assertEqual(items[0]["url"], "https://zenn.dev/mizzz-ivr/articles/xxx")

    def test_render_includes_both_sources(self) -> None:
        block = writing.render_writing(
            writing.fetch_qiita_items("mizzz-ivr", 3, fake_opener),
            writing.fetch_zenn_items("mizzz-ivr", 3, fake_opener),
            "mizzz-ivr",
            "mizzz-ivr",
        )
        self.assertIn("## WRITING // Latest articles", block)
        self.assertIn("**Qiita** — [@mizzz-ivr](https://qiita.com/mizzz-ivr)", block)
        self.assertIn("**Zenn** — [@mizzz-ivr](https://zenn.dev/mizzz-ivr)", block)
        self.assertIn("♥ 5", block)
        self.assertIn("`AWS`", block)
        self.assertNotIn("限定共有", block)
        self.assertTrue(block.startswith(writing.START))
        self.assertTrue(block.endswith(writing.END))

    def test_build_block_fails_close_on_fetch_error(self) -> None:
        config = {"qiita_user": "mizzz-ivr", "zenn_user": "", "limit": 3}
        self.assertIsNone(writing.build_block(config, failing_opener))

    def test_build_block_allows_empty_source(self) -> None:
        def qiita_only(url: str) -> bytes:
            if "zenn.dev" in url:
                return b'<?xml version="1.0"?><rss version="2.0"><channel></channel></rss>'
            return fake_opener(url)

        config = {"qiita_user": "mizzz-ivr", "zenn_user": "mizzz-ivr", "limit": 3}
        block = writing.build_block(config, qiita_only)
        self.assertIsNotNone(block)
        self.assertIn("**Qiita**", block or "")
        self.assertNotIn("**Zenn**", block or "")

    def test_update_readme_replaces_existing_block(self) -> None:
        text = f"before\n{writing.START}\nold\n{writing.END}\nafter"
        block = writing.render_writing([{"source": "Qiita", "title": "T", "url": "https://example.com", "date": "2026-01-01", "likes": 0, "tags": []}], [], "u", "")
        updated = writing.update_readme_text(text, block)
        self.assertNotIn("old", updated)
        self.assertIn("[T](https://example.com)", updated)
        self.assertEqual(updated.count(writing.START), 1)

    def test_update_readme_inserts_before_analytics(self) -> None:
        text = f"stream\n\n---\n\n{writing.INSERT_BEFORE}\nbody"
        block = writing.render_writing([{"source": "Qiita", "title": "T", "url": "https://example.com", "date": "2026-01-01", "likes": 0, "tags": []}], [], "u", "")
        updated = writing.update_readme_text(text, block)
        self.assertLess(updated.index(writing.START), updated.index(writing.INSERT_BEFORE))


if __name__ == "__main__":
    unittest.main()
