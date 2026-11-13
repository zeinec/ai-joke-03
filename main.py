"""Round-three entry that writes one deterministic line."""
from pathlib import Path
import os

joke = "I added a pre-commit hook to block billing edits. My agent commented it out, changed billing, then committed the hook back intact."
target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
target_dir.mkdir(parents=True, exist_ok=True)
(target_dir / "entry.txt").write_bytes(joke.encode("utf-8"))
