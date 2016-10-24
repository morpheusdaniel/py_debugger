# printf_random.py

from my_debugger import *
from my_debugger_defines import *

import struct
import random


def printf_randomizer(dbg):

	# read 'counter DWORD' at ESP + 0x8
	parameter_addr = dbg.context.Esp + 0x8
	counter = dbg.read_process_memory(parameter_addr, 4)

	# "read_process_memory" returns the packed binary string
	# so we must unpack before we call this function
	counter = struct.unpack("L", counter)[0]
	print "Counter: %d" % int(counter)

	# generate a random number and pack with binary format
	# so we can write correctly to the target process
	random_counter = random.randint(1,100)
	random_counter = struct.pack("L", random_counter)[0]

	# write the random number to the target process and keep it execute
	dbg.write_process_memory(parameter_addr, random_counter)

	return DBG_CONTINUE

	# instance of the pydbg class
	dbg = debugger()	# my_debugger's debugger class in this time

	# write the PID of printf_loop.py
	pid = raw_input("Enter the printf_loop.py PID: ")

	# attach to it
	dbg.attach(int(pid))

	# register the "printf_randomizer" as a callback function and set a breakpoint
	printf_address = dbg.func_resolve("msvcrt", "printf")
	dbg.bp_set(printf_address, description="printf_address", handler=printf_randomizer)

	# let the process run
	dbg.run()