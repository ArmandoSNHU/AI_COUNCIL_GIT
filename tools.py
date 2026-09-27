import os


class SecurityTools:
    @staticmethod
    def read_scan_log(path):
        """Read a security scan log from the given path.

        main.py passes an already-joined path (e.g. ``logs/scan.txt``), so this
        opens it directly rather than prefixing ``logs/`` a second time.
        """
        try:
            with open(path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: Scan file not found at {path}."
