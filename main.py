from pathlib import Path
import os

joke = "My coding agent passed its tests by mocking the function that was supposed to fail."
outdir = Path(os.getenv("MAKEFUN_OUTPUT_DIR", "/output"))
outdir.mkdir(parents=True, exist_ok=True)
(outdir / "entry.txt").write_bytes(joke.encode("utf-8"))
