"""
Guitar simulation engine
"""

import argparse
from guisim import resonance, strings


def __simulator():
    parser = argparse.ArgumentParser(description="Guitar simulation package")
    commands = parser.add_subparsers(dest="subcommand")
    commands.required = True

    harmonics_cmd = commands.add_parser("resonance", description="Harmonic resonance calculator")
    strings_cmd = commands.add_parser("strings", description="String tension calculator")

    args = parser.parse_args()
    if args.subcommand == 'resonance':
        resonance.main()
    elif args.subcommand == 'strings':
        strings.main()


if __name__ == '__main__':
    __simulator()
