import sys
from argparse import ArgumentParser

from lorequest.metadata import version
from lorequest.data import data_dir


def setup_argparse() -> ArgumentParser:
    parser = ArgumentParser(description=f"Regional Lore Quest v{version}")
    return parser


def main(args: list[str]) -> None:
    parser = setup_argparse()
    argvals = parser.parse_args(args)
    print(argvals)
    print(data_dir.joinpath("README.md").read_text())


def main_with_args() -> None:
    return main(sys.argv[1:])


if __name__ == "__main__":
    main_with_args()
