"""Holds logic for pipeline operations"""
import os
import sys
import subprocess
import json
import re
from datetime import datetime
from git import Repo

def get_diffs():
    """Gets the git diffs to determine which libraries to run operations on"""
    path = os.getcwd()
    repo = Repo(path)
    repo.remotes.origin.fetch()
    diffs = str(repo.git.diff('origin/main', name_only=True)).splitlines()

    updated_libraries = []

    for diff in diffs:
        if diff.startswith("projects"):
            path_parts = diff.split("/")
            updated_libraries.append(path_parts[1])

    return set(updated_libraries)


def append_snapshot_version(library):
    """Appends "-SNAPSHOT-" plus timestamp (down to the second) to library version"""
    package_json_path = f"./projects/{library}/package.json"
    with open(package_json_path, "r", encoding="UTF-8") as package_json:
        contents = json.load(package_json)

    version = contents["version"]
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    is_snapshot_version = re.match("\\s*([\\d.]+)-SNAPSHOT-([\\d-]+)", version)

    if is_snapshot_version:
        version = version.split("-")[0]

    contents["version"] = f"{version}-SNAPSHOT-{timestamp}"
    with open(package_json_path, "w", encoding="UTF-8") as package_json:
        package_json.write(json.dumps(contents, indent=2))


def npm_install():
    """Runs npm install"""
    subprocess.check_call("npm ci --cache .npm --prefer-offline", shell=True)


def handle_snapshot_publication(library):
    """Updates version with snapshot, builds, and publishes snapshot"""
    append_snapshot_version(library)
    subprocess.check_call(f"npm run build-{library}", shell=True)
    subprocess.check_call(f"npm publish --access=public ./dist/{library}", shell=True)


def npm_command(command):
    """Runs npm commands depending on input"""
    npm_install()
    diffs = get_diffs()

    for library in diffs:
        if command == "publish snapshots":
            handle_snapshot_publication(library)
        else:
            subprocess.check_call(f"npm run {command}-{library}", shell=True)


def eslint():
    """Runs eslint on libraries with changes"""
    npm_command("lint")


def unit_tests():
    """Runs unit tests on libraries with changes"""
    npm_command("test")


def publish_snapshots():
    """Publishes npm snapshots on libraries with changes"""
    npm_command("publish snapshots")


if len(sys.argv) < 2:
    print("You must call this script with an argument (e.g. `python scripts/ci.py eslint`)")
    sys.exit(1)

locals()[sys.argv[1]]()
