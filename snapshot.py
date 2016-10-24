# snapshot.py

from my_debugger import *
from my_debugger_defines import *

import threading
import time
import sys


class snapshotter(object):

	def __init__(self, exe_path):

		self.exe_path = exe_path
		self.pid = None
		self.dbg = None
		self.running = True

		# start a debugger thread and loop until setting PID of the target process
		pydbg_thread = threading.Thread(target=self.start_debugger)
		pydbg_thread.setDaemon(0)
		pydbg_thread.start()

		while self.pid == None:
			time.sleep(1)

		# now PID was set and target process is running
		# run the second thread for snapshot
		monitor_thread = threading.Thread(target=self.monitor_debugger)
		monitor_thread.setDaemon(0)
		monitor_thread.start()

	def monitor_debugger(self):

		while self.running == True:

			input = raw_input("Enter: 'snap','restore' or 'quit'")
			input = input.lower().strip()

			if input == "quit":
				
				print "[*] Exiting the snapshotter."
				self.running = False
				self.dbg.terminate_process()

			elif input == "snap":

				print "[*] Suspending all threads."
				self.dbg.suspend_all_threads()

				print "[*] Obtaining snapshot"
				self.dbg.process_snapshot()			# wtf process_snapshot() is already existing

				print "[*] Resuming operation."
				self.dbg.resume_all_threads()

			elif input == "restore":

				print "[*] Suspending all threads."
				self.dbg.suspend_all_threads()

				print "[*] Restoring snapshot."
				self.dbg.process_restore()

				print "[*] Resuming operation."
				self.dbg.resume_all_threads()

	def start_debugger(self):

		self.dbg = my_debugger()	# no pydbg but my_debugger this time
		pid = self.dbg.load(self.exe_path)
		self.pid = self.dbg.pid

		self.dbg.run()

	exe_path = "C:\\WINDOWS\\System32\\calc.exe"
	snapshotter(exe_path)