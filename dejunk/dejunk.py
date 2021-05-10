"""Main module."""
import platform
import os
import subprocess
import sys
from pathlib import Path


class Dejunk(object):
    def __init__(self, src='dejunk/configs/hosts.txt', dst=None):
        self.src = Path.cwd() / src
        self.dst = dst
        self._os = self._get_os()
        if self._os == 'windows':
            self.dst = Path('C:/windows/system32/drivers/etc/hosts')
        else:
            self.dst = Path('/etc/hosts')

        print(f"src file: {self.src}")
        print(f"openning destination hosts file: {self.dst}")
        with open(self.src, 'r') as src, open(self.dst, 'a+') as dst:
            dst.write(src.read())

    def is_root(self):
        if os.geteuid() == 0:
            return True
        else:
            return False

    def _get_os(self):
        return platform.system().lower()


if __name__ == '__main__':
    Dejunk()
