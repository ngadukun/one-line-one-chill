"""One Line, One Chill.

One line of pure chill, printed to stdout.
Deterministic, standard library only, writes no files.
"""

LINE = (
    "Somewhere between the second sip and the sunset, my phone died, "
    "my worries followed — and I finally felt rested."
)


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
