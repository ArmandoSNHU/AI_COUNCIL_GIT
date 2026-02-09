import os
#
class SecurityTools:
    @staticmethod
    def read_scan_log(filename):
        """Reads a security scan file from the D:\\AI_COUNCIL\\logs folder."""
        # We use a relative path to make it professional
        path = os.path.join("logs", filename)
        try:
            with open(path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Error: Scan file not found in the logs directory."
