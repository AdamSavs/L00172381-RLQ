from pathlib import Path

version = (Path(__file__).parent / "version.txt").read_text().strip()
