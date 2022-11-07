"""Holds logic for pipeline operations"""
import os
import sys
from git import Repo

def get_diffs():
    """Gets the git diffs to determine which libraries to run operations on"""
    path = os.getcwd()
    repo = Repo(path)
    repo.remotes.origin.fetch()
    diff = str(repo.git.diff('origin/main', name_only=True)).splitlines()

    if len(diff) != 0:
        print(diff)


def eslint():
    """Runs eslint on libraries with changes"""
    print("running eslint...")


def unit_tests():
    """Runs unit tests on libraries with changes"""
    print("running unit tests...")


def publish_snapshots():
    """Publishes npm snapshots on libraries with changes"""
    print("Publishes npm snapshots...")


if len(sys.argv) < 2:
    print("You must call this script with an argument (e.g. `python scripts/ci.py eslint`)")
    sys.exit(1)

locals()[sys.argv[1]]()
