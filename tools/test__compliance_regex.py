import unittest

import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

COMPLIANCE_REGEX = re.compile((SCRIPT_DIR / "compliance_regex.txt").read_text().strip())

MATCHING = [
    ". r rename variable",
    "^ r rename variable",
    "! r rename variable",
    "@ r clean up a bunch of stuff",
    "! F Add about page",
    "! B Fix crash on startup",
    ". a Format with prettier",
    ". n No-op commit",
    ". t Add missing tests",
    "@ @ Checkpoint: work in progress",
    ". e capture artifacts in CI",
]

NONMATCHING_EXAMPLES = [
    "r rename variable",
    ". rename variable",
    ".r rename variable",
    "!  B Fix crash on startup",
    ". rt rename variable in test",
    "- r rename variable",
    "Merge branch 'startup-crash'",
    "WIP: diagnosing crash on startup",
]


class Tess(unittest.TestCase):
    def test__matching(self):
        for example in MATCHING:
            self.assertTrue(COMPLIANCE_REGEX.match(example))

    def test__nonmatching(self):
        for example in NONMATCHING_EXAMPLES:
            self.assertFalse(COMPLIANCE_REGEX.match(example))
