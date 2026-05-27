from pathlib import Path
import base64
import hashlib

EXPECTED_SHA256 = "5cd29fe2dd4a9de784627a88d7e24ae8b7480f0924800066b8bf6c8389fb9ee5"
OUTPUT_NAME = "prospectus_verification_app_v0.1.0.zip"
PART_PREFIX = "prospectus_verification_app_v0.1.0.zip.b64.part"

here = Path(__file__).resolve().parent
output = here / OUTPUT_NAME
chunks = sorted(here.glob(f"{PART_PREFIX}*"))

if not chunks:
    raise SystemExit("未找到 base64 分块文件。")

data = "".join(chunk.read_text(encoding="utf-8").strip() for chunk in chunks)
output.write_bytes(base64.b64decode(data))

sha256 = hashlib.sha256(output.read_bytes()).hexdigest()
if sha256 != EXPECTED_SHA256:
    raise SystemExit(f"校验失败：{sha256}")

print(f"已还原：{output}")
print(f"SHA-256 校验通过：{sha256}")
