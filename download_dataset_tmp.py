#!/usr/bin/env python
import argparse
from  manager.download import ManageData

def run(filename, loc_dir):
    manager = ManageData(filename)

    manager.download(loc_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename', nargs='?', help='dataset json file')
    parser.add_argument('-D', '--dir', default='.', help='directory to create local dataset')
    args = parser.parse_args()

    filename = args.filename
    loc_dir = args.dir

    run(filename, loc_dir)

