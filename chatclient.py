#!/usr/bin python3

import sys
import re
import select
import socket

if len(sys.argv) != 3:
    print("Usage: ./chat-client <server-ip>:<portnum> nick")
    sys.exit(1)
else:
    print("All arguments given correct!")