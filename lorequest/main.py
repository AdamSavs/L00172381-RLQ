import sys
from argparse import ArgumentParser
from lorequest.metadata import version
from lorequest.data import data_dir
from lorequest.interactive import InteractiveSystem


def setup_argparse() -> ArgumentParser:
    """
    Sets up and returns the argument parser for the CLI.

    Returns:
        ArgumentParser: Configured argument parser with interactive flag.
    """
    parser = ArgumentParser(description=f"Regional Lore Quest v{version}")
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Launch the interactive LoreQuest system.",
    )
    return parser


def main(args: list[str]) -> None:
    """
    Entry point for the Lore Quest system.

    Args:
        args (list[str]): Command-line arguments passed to the script.

    Behavior:
        - Displays application metadata.
        - Launches the interactive LoreQuest system if the `--interactive` flag is set.
    """
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
    """
    Wrapper for the `main` function that automatically parses `sys.argv`.

    Calls:
        main(sys.argv[1:])
    """
    return main(sys.argv[1:])


if __name__ == "__main__":
    """
    Entry point of the script. Calls `main_with_args`.
    """
    main_with_args()
