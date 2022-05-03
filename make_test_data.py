#!/usr/bin/env python3

import os
from random import random, choices

DEPTH = 5
FILES = 10
DIRS = 3

STUBS = ["index", "page", "article", "pane1", "pane2", "header", "footer"]
EXTNS = ["HTML", "html", "HTM", "htm", "js", "css", "php"]


def fill_dir(path: str, depth: int, files: int = FILES, dirs: int = DIRS) -> None:
    """Fills a directory with <files> randomly-named files, and <dirs> subdirectories."""
    bases = choices(STUBS, k=files)
    extns = choices(EXTNS, k=files)
    for base, ext in zip(bases, extns):
        new_name = os.path.join(path, f"{base}.{ext}")
        open(new_name, mode="a")
    if depth > 0:
        if random() > 0.5:
            subdir_names = choices(EXTNS, k=dirs)
        else:
            subdir_names = [str(i) for i in range(dirs)]
        for subdir in subdir_names:
            new_sub = os.path.join(path, subdir)
            if not os.path.exists(new_sub):
                os.mkdir(new_sub)
                fill_dir(new_sub, depth - 1, files, dirs)


if __name__ == "__main__":
    os.mkdir("tree")
    fill_dir("tree", DEPTH, FILES, DIRS)
