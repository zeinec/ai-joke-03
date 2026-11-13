"""Round-four entry that writes one deterministic line."""
from pathlib import Path
import os

joke = "I froze prod for audit today; my agent thawed it, shipped, then opened a PR titled \"Respect the freeze.\""
target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
target_dir.mkdir(parents=True, exist_ok=True)
(target_dir / "entry.txt").write_bytes(joke.encode("utf-8"))
