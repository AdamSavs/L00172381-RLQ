import sys
from argparse import ArgumentParser
from lorequest.metadata import version
from lorequest.data import data_dir
from lorequest.interactive import InteractiveSystem


def setup_argparse() -> ArgumentParser:
    parser = ArgumentParser(description=f"Regional Lore Quest v{version}")
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Launch the interactive LoreQuest system.",
    )
    return parser


def main(args: list[str]) -> None:
    parser = setup_argparse()
    argvals = parser.parse_args(args)

    # Display application metadata
    print(f"Regional Lore Quest v{version}")
    print(data_dir.joinpath("README.md").read_text())

    # Launch the interactive system if the flag is set
    if argvals.interactive:
        system = InteractiveSystem()
        system.interact()
    else:
        print("Use the --interactive flag to start the interactive system.")


def main_with_args() -> None:
    return main(sys.argv[1:])


if __name__ == "__main__":
    main_with_args()
