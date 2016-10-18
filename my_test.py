#!/usr/bin/python
# my_test.py

import my_debugger

debugger = my_debugger.debugger()
pid = raw_input("Enter the PID of the process to attach to: ")
debugger.attach(int(pid))

list = debugger.enumerate_threads()

for thread in list:
	thread_context = debugger.get_thread_context(thread)
	
	print "[*] Dumping registers for thread ID: 0x%08x" % thread
	print "[**] EIP: 0x%08x" % thread_context.Eip
	print "[**] ESP: x0%08x" % thread_context.Esp
	print "[**] EBP: 0x%08x" % thread_context.Ebp
	print "[**] EAX: x0%08x" % thread_context.Eax
	print "[**] EBX: x0%08x" % thread_context.Ebx
	print "[**] ECX: x0%08x" % thread_context.Ecx
	print "[**] EDX: x0%08x" % thread_context.Edx
	print "[*] END DUMP"
	print ""

print ""
print ""
print ""
debugger.run()

debugger.detach()

#debugger.load("C:\\WINDOWS\\system32\\calc.exe")