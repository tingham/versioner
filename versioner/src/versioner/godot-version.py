from semver import generate_version
from os import path

def read_godot_version():
    """
    Reads the version from the project.godot file
    Returns:
    tuple: (major, minor, patch, short_hash)
    """
    project_file_path = path.abspath("./examples/project.godot")

    # If the example file is unreachable (we are running this as a pre-commit hook), try the root directory
    if not path.exists(project_file_path):
        project_file_path = path.abspath("./project.godot")

    print(f"Reading godot version from {project_file_path}")
    with open(project_file_path, "r") as f:
        for line in f:
            if "config/version=" in line:
                # Remove the newline at the end of the line
                print(f"Found version line: {line}")
                print(line.split("="))
                version_string = line.split("=")[1].strip().strip("\"")
                break
    if version_string is not None:
        if "+" in version_string:
            (version, hash) = version_string.split("+")
        else:
            version = version_string
            hash = ""
        major, minor, patch = version.split(".")
        return (int(major), int(minor), int(patch), hash)

def generate_godot_version():
    """
    Attempts to reconcile the semver and godot versions using the following rules:
    - If the existing version major is greater than the generated major, use the existing major and add a one to the minor
    - If the existing version minor is greater than the generated minor, use the existing minor and add a one to the patch
    """
    existing_version = read_godot_version()
    major, minor, patch, short_hash = generate_version()
    if existing_version is not None:
        existing_major, existing_minor, existing_patch, existing_hash = existing_version
        if existing_major > major:
            major = existing_major
            minor = existing_minor + 1
            patch = 0
        if existing_minor > minor:
            minor = existing_minor
            patch = existing_patch + 1
    return (major, minor, patch, short_hash)


def format_godot_version():
    """
    Formats the godot version into a string
    """
    major, minor, patch, short_hash = generate_godot_version()
    return f"{major}.{minor}.{patch}+{short_hash}"

if __name__ == "__main__":
    print(f"generated version: {format_godot_version()}")
