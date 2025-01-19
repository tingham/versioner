# Generate a semver from the current github hash
import subprocess

def generate_version():
    return "0.0.0+{}".format(get_current_hash())

def get_current_hash():
    return subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode("utf-8")

if __name__ == "__main__":
    print(generate_version())