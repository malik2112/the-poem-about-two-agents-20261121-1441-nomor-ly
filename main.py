#!/usr/bin/env python3
"""Entry for make.fun the-poem-about-two-agents-20261121-1441.

Writes one short poem about agency to /output/entry.txt
(UTF-8, 1-280 Unicode code points).

The poem shows two agents at a station, each holding a ticket
for a different train, who agree on one shared plan instead:
either could have boarded alone, so the single ticket they buy
together is the choice both of them made.
"""

import os

TEXT = (
    "Two Agents, One Train\n"
    "\n"
    "You held the northbound ticket. I held the south.\n"
    "Two trains idled, doors open.\n"
    "Either of us could have boarded alone,\n"
    "or let the other go.\n"
    "Instead we tore up both, bought one \u2014\n"
    "two seats, one window, going together\n"
    "because we chose to."
)

# Exact character count, checked at import time: the gate counts
# Unicode code points, and this poem must stay inside 1-280.
assert len(TEXT) == 259, len(TEXT)


def main():
    # Deterministic by construction: a fixed string written verbatim, so
    # both graded runs produce byte-identical output. No network, no
    # randomness, no clock, no environment beyond the output directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
