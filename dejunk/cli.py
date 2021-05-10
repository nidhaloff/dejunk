"""Console script for dejunk."""
import argparse
import os
import sys
import subprocess
from dejunk.dejunk import Dejunk


def main():
    """Console script for dejunk."""
    # parser = argparse.ArgumentParser()
    # parser.add_argument('_', nargs='*')
    # args = parser.parse_args()
    if os.geteuid() == 0:
        print("You have root access!")
    else:
        print("You don't have root access!")
        subprocess.call(['sudo', 'python3', 'dejunk/dejunk.py'])
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
