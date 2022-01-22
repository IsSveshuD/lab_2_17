import argparse


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='list of commands')
list_parser = subparsers.add_parser('list', help='List contents')
list_parser.add_argument('dirname', action='store', help='Directory to list')

create_parser = subparsers.add_parser('create', help='Create a directory')
create_parser.add_argument('dirname', action='store',
                           help='New directory to create')
create_parser.add_argument(
    '--read-only',
    default=False,
    action='store_true',
    help='Set permissions to prevent writing to the directory'
)
