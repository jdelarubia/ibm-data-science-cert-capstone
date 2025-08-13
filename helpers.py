"""helpers.py
Functions and global variables of regular use."""

from pathlib import Path

DATA_DIR = Path("./data")
DATA_DIR.mkdir(exist_ok=True)


def normalize_column_name(col_name: str) -> str:
    """MISC.
    Given a string (column names), normalize it by:
    - converting it to lowercase
    - adding an underscore between words
    - removing symbols such as: ['(', ')', '.']"""

    def remove_symbols(col_name: str) -> str:
        symbols = ["(", ")", "."]
        col_name = col_name.strip().lower()

        for symbol in symbols:
            col_name = col_name.replace(symbol, "")
        return "_".join(col_name.split())

    return remove_symbols(col_name)


if __name__ == "__main__":
    pass
