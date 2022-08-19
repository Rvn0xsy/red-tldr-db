import json
import os
from pathlib import Path

PAYLOAD_ENV = os.getenv("PAYLOAD")
PAYLOAD = json.loads(PAYLOAD_ENV)
issue = PAYLOAD.get("issue", {})
ISSUE_BODY = issue.get("body", "")
LABEL = PAYLOAD.get("label", {}).get("name")
SENDER = PAYLOAD.get("sender", {}).get("login", "")
ISSUE_TITLE = issue.get("title", "")

def get_string_between(o_string, start, end):
    if start in o_string and end in o_string:
        s = o_string.index(start) + len(start)
        e = o_string.index(end, s)
        return o_string[s:e]
    exit(1)

def create_file(name):
    yaml_data = get_string_between(ISSUE_BODY, "```yaml", "```").strip()
    base_path = Path("files/New").resolve()
    n = Path("web_fingerprint/").joinpath(name).with_suffix(".yaml").resolve()
    if n.parent == base_path:
        with open(n, "w") as y:
            y.write(yaml_data)
        print("Create Success :) ")

def runner():
    # 打标签，已经测试，已经审核,判断发起人，不是管理员取消标签
    if ACTION == "labeled" and LABEL == "Reviewed" and SENDER == "rvn0xsy":
        doc_name = get_string_between(ISSUE_TITLE, "[", "]")
        create_file(doc_name)