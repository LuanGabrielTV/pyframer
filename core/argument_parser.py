import argparse


def get_arguments():
    # TODO: add description for the arguments
    argument_parser = argparse.ArgumentParser(description='', add_help=False)

    argument_parser.add_argument('path', nargs=1, action='store', help='')
    
    argument_parser.add_argument('-b', '--border', action='store_true', help='')
    argument_parser.add_argument('-bs', '--border-size', default=.1, nargs=1, action='store', help='')

    argument_parser.add_argument('-far', '--fit-to-aspect-ratio', action='store_true', help='')
    argument_parser.add_argument('-ar', '--aspect-ratio', nargs=1, action='store', help='')
    
    argument_parser.add_argument('-c', '--color', nargs=1, action='store', help='')
    
    argument_parser.add_argument('-h', '--help', action='help', help='Shows this message and quits')

    return argument_parser.parse_args()
