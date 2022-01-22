import argparse

parser = argparse.ArgumentParser()


parser.add_argument('--LifetheUniverseandEverything', action='store_const',
                    const=42)
print(parser.parse_args(['--LifetheUniverseandEverything']))
parser.add_argument('--l', action='append')
print(parser.parse_args('--l a --l b --l Y'.split()))

parser.add_argument('--verbose', '-v', action='count')
print(parser.parse_args('-vvv'.split()))
