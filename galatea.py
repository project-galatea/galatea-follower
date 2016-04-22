#! /usr/bin/python2.7

import argparse
from slave import Slave
from galatea.utils.logger import Logger as L

def main():
    parser = argparse.ArgumentParser(description='Galatea slave servers that manage the chats and the AI')
    parser.add_argument("-p", "--port", help="sets port of slave", default=24833)
    args = parser.parse_args()
    Slave(args.port, L("logger.log", 1))


if __name__ == "__main__":
    main()
