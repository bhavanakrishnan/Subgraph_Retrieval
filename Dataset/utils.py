import json
from typing import Dict, List, Any

def load_jsonl(path: str):
    data_list = []
    with open(path, "r") as f:
        for line in f.readlines():
            data_list.append(json.loads(line))
    return data_list

def dump_jsonl(data_list: List[Any], path: str):
    with open(path, "w") as f:
        for json_obj in data_list:
            f.write(json.dumps(json_obj) + "\n")

def load_json(path: str):
    with open(path, "r") as f:
        return json.loads(f.read())

def dump_json(data: Dict[Any, Any], path: str):
    with open(path, "w") as f:
        f.write(json.dumps(data))
