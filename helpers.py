"""helpers.py
Functions and global variables of regular use."""

from pathlib import Path

DATA_DIR = Path("./data")
DATA_DIR.mkdir(exist_ok=True)


def normalize_column_name(col_name: str) -> str:
    """MISC. Normalize column names by:
    - converting to lowercase
    - adding an underscore between words
    - removing () symbols"""
    return "_".join(
        col_name.lower().replace(".", "").replace("(", "").replace(")", "").split()
    )


if __name__ == "__main__":
    pass
