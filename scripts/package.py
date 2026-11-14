#!/usr/bin/env python3
"""Build an immutable, self-contained Office plugin ZIP and SHA256SUMS."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
if manifest["id"] != "office" or manifest["main"] != "index.js":
    raise SystemExit("Unexpected package identity")
if len(sys.argv) != 2:
    raise SystemExit("Usage: package.py OUTPUT_DIRECTORY")
subprocess.run(["node", "test.js"], cwd=root, check=True)
out = Path(sys.argv[1]).expanduser().resolve()
out.mkdir(parents=True, exist_ok=True)
bundle = out / ("aide-pkg-office-v" + manifest["version"] + ".zip")
if bundle.exists():
    raise SystemExit("Refusing to overwrite an existing package")
with zipfile.ZipFile(bundle, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for name in ["LICENSE", "README.md", "index.js", "manifest.json", "test.js", "docs/reviews/2026-11-14-common-workflow.md"]:
        item = zipfile.ZipInfo(name, (2026, 11, 14, 0, 0, 0))
        item.compress_type = zipfile.ZIP_DEFLATED
        item.external_attr = 0o100644 << 16
        archive.writestr(item, (root / name).read_bytes())
with zipfile.ZipFile(bundle) as archive:
    if archive.testzip():
        raise SystemExit("Package verification failed")
digest = hashlib.sha256(bundle.read_bytes()).hexdigest()
(out / "SHA256SUMS").write_text(digest + "  " + bundle.name + "\n", encoding="ascii")
print(json.dumps({"file": str(bundle), "sha256": digest}))
