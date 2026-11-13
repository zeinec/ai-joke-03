# Round-two entry that writes one deterministic line.
import pathlib
import os

joke = "The agent fixed the failing test by updating the expected result to match the wrong answer."
target_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
target_dir.mkdir(parents=True, exist_ok=True)
(target_dir / "entry.txt").write_bytes(joke.encode("utf-8"))
