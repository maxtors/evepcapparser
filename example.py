#!/usr/bin/python

"""Example file for running the EvePcapParser.

Andreas Moe <moe.andreas@gmail.com>
"""

from evePcap import EvePcapParser, EvePcapError

if __name__ == '__main__':
    app = EvePcapParser()
    app.parseFile('events.json')
