#!/bin/sh
set -eu

STRICT_METADATA=1
if [ "${1:-}" = "--no-strict-metadata" ]; then
  STRICT_METADATA=0
fi

examples_dir=$(CDPATH= cd -- "$(dirname "$0")" && pwd)

python3 - "$examples_dir" "$STRICT_METADATA" <<'PY'
import json
import pathlib
import sys

examples_dir = pathlib.Path(sys.argv[1])
strict = sys.argv[2] == "1"
json_files = sorted(examples_dir.glob("*.json"))

if not json_files:
    print(f"未找到示例 JSON（跳过）：{examples_dir}")
    raise SystemExit(0)

failed = []
required_common = ["config_version", "description"]
strict_required = ["summary"]

for path in json_files:
    print(f"校验：{path.name}")
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as exc:
        failed.append(f"{path.name}: JSON 解析失败: {exc}")
        continue

    for key in required_common:
        if key not in data:
            failed.append(f"{path.name}: 缺少字段 {key}")

    if "host" not in data and "servers" not in data:
        failed.append(f"{path.name}: 缺少 host 或 servers")

    if strict:
        for key in strict_required:
            if key not in data:
                failed.append(f"{path.name}: 缺少字段 {key}")

if failed:
    print(f"示例冒烟测试失败：{len(failed)} 项")
    for item in failed:
        print(f"  - {item}")
    raise SystemExit(1)

print(f"示例冒烟测试通过：{len(json_files)} 个文件")
PY
