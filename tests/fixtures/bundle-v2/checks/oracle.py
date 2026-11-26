from pathlib import Path
import runpy

module = runpy.run_path(str(Path(__file__).resolve().parents[1] / "src" / "add.py"))
add = module["add"]
assert [add(2, 3), add(0, 0), add(-4, 1)] == [5, 0, -3]
