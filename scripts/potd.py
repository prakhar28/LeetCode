"""Log LeetCode's Problem of the Day into daily/ and keep a tracker table in daily/README.md.

Each problem gets a note file with the link, difficulty and topics, plus a checklist
to fill in once solved.
"""
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DAILY = ROOT / "daily"
QUERY = """
query questionOfToday {
  activeDailyCodingChallengeQuestion {
    date
    link
    question { questionFrontendId title titleSlug difficulty topicTags { name } }
  }
}"""


def fetch() -> dict:
    req = urllib.request.Request(
        "https://leetcode.com/graphql",
        data=json.dumps({"query": QUERY, "operationName": "questionOfToday"}).encode(),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (potd-tracker)",
            "Referer": "https://leetcode.com/problemset/",
        },
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)["data"]["activeDailyCodingChallengeQuestion"]


def main() -> None:
    potd = fetch()
    q = potd["question"]
    date = potd["date"]
    tags = ", ".join(t["name"] for t in q["topicTags"]) or "—"
    url = f"https://leetcode.com{potd['link']}"
    DAILY.mkdir(exist_ok=True)

    note = DAILY / f"{date}-{q['titleSlug']}.md"
    if note.exists():
        print("already logged today")
        return
    note.write_text(
        f"# {q['questionFrontendId']}. {q['title']}\n\n"
        f"- **Date:** {date} (LeetCode Problem of the Day)\n"
        f"- **Difficulty:** {q['difficulty']}\n"
        f"- **Topics:** {tags}\n"
        f"- **Link:** {url}\n\n"
        "## Status\n\n- [ ] Solved\n\n"
        "## Approach\n\n_TODO_\n\n## Complexity\n\n- Time: \n- Space: \n",
        encoding="utf-8",
    )

    tracker = DAILY / "README.md"
    header = (
        "# 📅 LeetCode Problem of the Day\n\n"
        "This log fills itself in automatically. A GitHub Action records each day's problem, "
        "and I tick it off once it's solved.\n\n"
        "| Date | # | Problem | Difficulty | Topics |\n|---|---|---|---|---|\n"
    )
    body = tracker.read_text(encoding="utf-8") if tracker.exists() else header
    row = f"| {date} | {q['questionFrontendId']} | [{q['title']}]({note.name}) | {q['difficulty']} | {tags} |\n"
    # newest first: insert right after the table header
    body = re.sub(r"(\|---\|---\|---\|---\|---\|\n)", r"\1" + row.replace("\\", "\\\\"), body, count=1)
    tracker.write_text(body, encoding="utf-8")
    print(f"logged {q['title']}")


if __name__ == "__main__":
    main()
