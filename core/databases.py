import os
import json

file_path = os.path.dirname(__file__)
config_file = os.path.join(file_path, "config.json")
with open(config_file, "r", encoding="utf-8") as f:
    config = json.load(f)  # 用json.load直接读成dict

databases_config = config.get("DATABASES_CONFIG")
