#! /usr/bin/env python

from __future__ import print_function

import argparse
import os

from ulog_parser import *

"""
Display logged messages from an ULog file
"""

parser = argparse.ArgumentParser(description='Display logged messages from an ULog file')
parser.add_argument('filename', metavar='file.ulg', help='ULog input file')


args = parser.parse_args()
ulog_file_name = args.filename

msg_filter = [] # we don't need the data messages
ulog = ULog(ulog_file_name, msg_filter)


for m in ulog.logged_messages:
    m1, s1 = divmod(int(m.timestamp/1e6), 60)
    h1, m1 = divmod(m1, 60)
    print("{:d}:{:02d}:{:02d} {:}: {:}".format(
        h1, m1, s1, m.log_level_str(), m.message))



