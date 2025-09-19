import json
import os

def load_json(file_path):
    """
    Load JSON file safely with absolute path resolution.
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
    abs_path = os.path.join(base_dir, file_path)
    with open(abs_path, "r", encoding="utf-8") as f:
        return json.load(f)
