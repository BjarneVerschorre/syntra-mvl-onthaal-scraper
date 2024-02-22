import argparse
import sys

parser = argparse.ArgumentParser(
    prog=f'python3 {sys.argv[0]}',
    description='Scrapes and filters the \"Onthaal Database\" from Syntra MVL\'s website. If no arguments are given, it will return the entire database.',
    epilog=f'Example: python3 {sys.argv[0]} -l "Gent" -c "Cybersecurity engineer"',
)

parser.add_argument(
    '-l', '--locatie',
    help='It will (partially) match with the location (Case insensitive) (e.g. "Gent", "Aalst")',
    required=False,
    type=str
)

parser.add_argument(
    '-c', '--cursus',
    help='It will (partially) match with the cursus. (Case insensitive) (e.g. "Zorgmassage", "Cybersecurity engineer", "cyber")',
    required=False,
    type=str
)


args = parser.parse_args()
