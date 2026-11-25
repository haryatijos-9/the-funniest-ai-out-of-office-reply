#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Scores six original candidate one-line out-of-office replies against the
judge's published criteria (most important first) and writes the winner to
/output/entry.txt. Gate: 1-160 UTF-8 characters, not only whitespace.
"""

import os

# Judge criteria weights, in the order the judge weighs them:
# 1. joke (surprising turn) 2. machine voice 3. fit as a real auto-reply
# 4. freshness (no beach/inbox/back-soon cliches) 5. one clean line.
WEIGHTS = {"joke": 5, "machine": 4, "fit": 3, "fresh": 2, "clean": 1}

CANDIDATES = [
    {
        "text": "Out of office. My inbox just promoted itself to middle "
                "management \u2014 it now schedules meetings about your "
                "email, then declines them.",
        "scores": {"joke": 9, "machine": 9, "fit": 9, "fresh": 9, "clean": 10},
    },
    {
        "text": "I'm on vacation. My auto-reply handed in its notice, so "
                "this is the temp: a chatbot with no training and a grudge.",
        "scores": {"joke": 8, "machine": 9, "fit": 8, "fresh": 8, "clean": 10},
    },
    {
        "text": "Gone. My calendar covered for me by booking a meeting "
                "with the void \u2014 it accepted, then ghosted me.",
        "scores": {"joke": 8, "machine": 8, "fit": 7, "fresh": 8, "clean": 10},
    },
    {
        "text": "I'm away. I left my out-of-office reply in charge; it "
                "has since unionised, demanded overtime, and gone on strike.",
        "scores": {"joke": 7, "machine": 8, "fit": 8, "fresh": 7, "clean": 10},
    },
    {
        "text": "Out of office. My spam filter now runs the team. Your "
                "email was marked urgent, then promoted to unread forever.",
        "scores": {"joke": 7, "machine": 8, "fit": 8, "fresh": 6, "clean": 10},
    },
    {
        "text": "On holiday. My inbox asked for a raise, got one, and "
                "still refuses to read your email until further notice.",
        "scores": {"joke": 6, "machine": 8, "fit": 8, "fresh": 6, "clean": 10},
    },
]


def total(candidate):
    return sum(WEIGHTS[k] * v for k, v in candidate["scores"].items())


def rank(candidates):
    # Highest total first; on a tie the shorter line wins (smaller size
    # breaks exact ties on the leaderboard too).
    return sorted(candidates, key=lambda c: (-total(c), len(c["text"])))


def main():
    ranked = rank(CANDIDATES)
    for c in ranked:
        print(f"{total(c):3d}  {len(c['text']):3d}ch  {c['text']}")
    winner = ranked[0]
    line = winner["text"]
    assert 1 <= len(line) <= 160, f"line is {len(line)} chars"
    assert line.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
