from pathlib import Path

BASE_DIR = Path.home() / "data"

INPUT_DIR = BASE_DIR / "in"
OUTPUT_DIR = BASE_DIR / "out"

INPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

