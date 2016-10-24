# access_violation_handler.py

from my_debugger import *
from my_debugger_defines import *

# Utility libraries included with PyDbg(my_debugger at this time)
import utils

# access violation handler
def check_accessv(dbg):

	# pass the first exception
	if dbg.dbg.u.Exception.dwFirstChance:
		return DBG_EXCEPTION_NOT_HANDLED

	crash_bin = utils.crash_binning.crash_binning() 	# check this and add 'crash_binning' etc..
	crash_bin.record_crash(dbg)
	print crash_bin.crash_synopsis()

	dbg.terminate_process()

	return DBG_EXCEPTION_NOT_HANDLED


pid = raw_input("Enter the Process ID: ")

dbg = pydbg()
dbg.attach(int(pid))
dbg.set_callback(EXCEPTION_ACCESS_viOLATION, check_accessv)
dbg.run()