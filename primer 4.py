import argparse


parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--user', action="store")
parent_parser.add_argument('--password', action="store")
child_parser = argparse.ArgumentParser(parents=[parent_parser],
                                       conflict_handler='resolve')
child_parser.add_argument('--user', action="store", default="Guest")
print(child_parser.parse_args())
