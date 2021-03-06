#! /usr/bin/env python3


# pylint: disable=C0103
# pylint: disable=C0330

"""Translate a file from ptg format to paint instruction format.

arguments:

"""

import sys

import planner

DefaultInputFileName = "../../ptg_pictures/lisa.ptg"
DefaultOutputFileName = "lisa.txt"


def USAGE_STATEMENT():
    """ Print a usage statement. """
    message = """
    Usage:\t\tpython path_planner.py [options]
    Options:
    -h \t\tPrint this message and exit
    -ci\t\tWill ask for input file other than default
    -co\t\tWill ask for output file other than default
    -d \t\tWill turn on debug mode
    """
    print(message)


def set_flags(args):
    """ Parse command line arguments. """
    changeOFileName = False
    debug = False
    iFileName = DefaultInputFileName
    oFileName = DefaultOutputFileName
    # drop script name from arguments
    args = args[1:]
    for arg in args:
        if arg == "-h":
            USAGE_STATEMENT()
            exit()
        elif arg[0:3] == "-ci":
            iFileName = arg[4:]
            if not changeOFileName:
                # make input file have same encoding as output file,
                # but replace ptg with txt
                # assert iFileName[-4:] == ".ptg"
                oFileName = iFileName[:-4] + ".txt"
        elif arg[0:3] == "-co":
            changeOFileName = True
            oFileName = arg[4:]
        elif arg == "-d":
            debug = True
        else:
            print("ERROR: UNKNOWN ARGUMENT: %s" % arg)
            USAGE_STATEMENT()
            exit(10)
    return (iFileName, oFileName, debug)


def try_to_open(filename, mode):
    """ Open a file with filename and mode, or, if opening fails,
    exit and print an error message. """
    try:
        result = open(filename, mode)
    except IOError:
                print("error: could not open file %s" % filename)
    exit(10)
    return result


def read_numbers(file):
    """ Take an open ptg file and transform it into a 2D integer array. """
    return [list(map(int, line.split())) for line in file]


def try_to_read_numbers(file):
    try:
        return read_numbers(file)
    except ValueError as e:
        print("invalid ptg file:")
        print(e)
        exit(10)


def main(iFileName, oFileName):
    oFile = open(oFileName, 'w')
    iFile = open(iFileName, 'r')
    matrix = try_to_read_numbers(iFile)
    print("matrix made\n")
    # Error-checking is done. We know the user input was valid.
    planner.left_right_output(matrix, oFile)
    oFile.close()
    iFile.close()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description='generate brushstroke instructions')
    parser.add_argument('file_in', help='input ptg file')
    parser.add_argument('file_out', help='output txt file')
    args = parser.parse_args()

    main(args.file_in, args.file_out)
