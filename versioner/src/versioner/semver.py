# Generate a semver from the current github hash
import subprocess
from math import log10, floor

def generate_version():
    """
    Generates a semver from the current commit count in git
    [major] - The number of 100 powers in the commit count
    [minor] - The number of 10 powers in the commit count
    [patch] - The commit count
    [short_hash] - The short commit hash

    Returns:
    tuple: (major, minor, patch, short_hash)
    """
    total_commits = get_commit_count()
    short_hash = short_commit_hash()
    major = floor(log10(int(total_commits)) / 2)
    minor = floor(log10(int(total_commits)))
    patch = int(total_commits)
    print(f"{major}.{minor}.{patch}")
    return (major, minor, patch, short_hash)

def get_commit_count():
    """Counts the lines in the .git/logs/refs/heads/main file"""
    return subprocess.run(["git", "rev-list", "HEAD", "--count"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()

def short_commit_hash():
    """Get the short commit hash"""
    return subprocess.run(["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()

if __name__ == "__main__":
    print(f"generated version: {generate_version()}")