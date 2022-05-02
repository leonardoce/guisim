"""
Guitar simulation engine
"""

import argparse
from guisim import harmonics, strings


def __simulator():
    parser = argparse.ArgumentParser(description="Guitar simulation package")
    commands = parser.add_subparsers(dest="commands")

    harmonics_cmd = commands.add_parser("harmonics", description="Harmonic resonance calculator")
    strings_cmd = commands.add_parser("strings", description="String tension calculator")

    args = parser.parse_args()
    if args.commands == 'harmonics':
        harmonics.main()
    elif args.commands == 'strings':
        strings.main()


if __name__ == '__main__':
    __simulator()
