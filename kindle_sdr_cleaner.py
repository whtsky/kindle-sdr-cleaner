#!/usr/bin/env python3
import shutil
import sys

from pathlib import Path


def handle_path(path: Path):
    subfolders = []
    seen_sdrs = set()
    seen_files = set()
    try:
        for entry in path.iterdir():
            if entry.is_dir():
                if entry.suffix == ".sdr":
                    seen_sdrs.add(entry.stem)
                else:
                    subfolders.append(entry)
            else:
                # is file
                seen_files.add(entry.stem)
        diff = seen_sdrs - seen_files
        for sdr_to_remove in diff:
            sdr_path = path / f"{sdr_to_remove}.sdr"
            print("Remove: ", sdr_path)
            shutil.rmtree(sdr_path)
        for folder in subfolders:
            handle_path(folder)
    except PermissionError:
        print("PermissionError: ", path, ", skip")


def main():
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
        handle_path(path)
    else:
        handle_path(Path.cwd())


if __name__ == "__main__":
    main()
