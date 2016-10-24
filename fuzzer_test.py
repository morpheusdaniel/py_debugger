# fuzzer_test.py

from file_fuzzer import *

import getopt
import sys


def print_usage():

	print "[*]"
	print "[*] file_fuzzer.py -e <Executable Path> -x <File Extension>"
	print "[*]"

	sys.exit(0)

# application's file path & file extension to parse the document
if __name__ == "__main__":
	print "[*] Generic File Fuzzer."

try:
	opts, argo = getopt.getopt(sys.argv[1:], "e:x:n")
except getopt.GetoptError:
	print_usage()

exe_path = None
ext = None
notify = False

for o, a in opts:
	if o == "-e":
		exe_path = a
	elif o == "-x":
		ext = a 
	elif o == "-n":
		notify = True

if exe_path is not None and ext is not None:
	fuzzer = file_fuzzer(exe_path, ext, notify)
	fuzzer.fuzz()
else:
	print_usage()
