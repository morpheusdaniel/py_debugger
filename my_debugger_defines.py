#!/usr/bin/python
# my_debugger_defines.py
# referenced by https://github.com/dave5623/GrayHatPython/blob/master/my_debugger_defines.py

from ctypes import *

# Mapping the MS types to ctypes for clarity
BYTE = c_ubyte
WORD = c_ushort
DWORD = c_ulong
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
LPSTR = POINTER(c_char)
HANDLE = c_void_p
PVOID = c_void_p
LPVOID = c_void_p
UINT_PTR = c_ulong
SIZE_T = c_ulong
LPTHREAD_START_ROUTINE = POINTER(c_ulong)

# Constants
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010
PROCESS_ALL_ACCESS = 0x001F0FFF
THREAD_ALL_ACCESS = 0x001F03FF
MAXIMUM_ALLOWED = 0x02000000
INFINITE = 0xFFFFFFFF
DBG_CONTINUE = 0x00010002
DBG_EXCEPTION_NOT_HANDLED = 0x80010001

# Debug event constants
EXCEPTION_DEBUG_EVENT = 0x1
CREATE_THREAD_DEBUG_EVENT = 0x2
CREATE_PROCESS_DEBUG_EVENT = 0x3
EXIT_THREAD_DEBUG_EVENT = 0x4
EXIT_PROCESS_DEBUG_EVENT = 0x5
LOAD_DLL_DEBUG_EVENT = 0x6
UNLOAD_DLL_DEBUG_EVENT = 0x7
OUTPUT_DEBUG_STRING_EVENT = 0x8
RIP_EVENT = 0x9

# Debug exception codes
EXCEPTION_ACCESS_VIOLATION = 0xC0000005
EXCEPTION_BREAKPOINT = 0x80000003
EXCEPTION_GUARD_PAGE = 0x80000001
EXCEPTION_SINGLE_STEP = 0x80000004

# Thread constants for CreateToolhelp32Snapshot()
TH32CS_SNAPHEAPLIST = 0x00000001
TH32CS_SNAPPROCESS = 0x00000002
TH32CS_SNAPTHREAD = 0x00000004
TH32CS_SNAPMODULE = 0x00000008
TH32CS_INHERIT = 0x80000000
TH32CS_SNAPALL = (TH32CS_SNAPHEAPLIST|TH32CS_SNAPPROCESS|TH32CS_SNAPTHREAD|TH32CS_SNAPMODULE)

# Context flags for GetThreadContext()
CONTEXT_FULL = 0x00010007
CONTEXT_DEBUG_REGISTERS = 0x00010010

# Memory permissions
PAGE_EXECUTE_READWRITE = 0x00000040

# Hardware breakpoint conditions
HW_ACCESS = 0x00000003
HW_EXECUTE = 0x00000000
HW_WRITE = 0x00000001

# Memory page permissions, used by VirtualProtect()
PAGE_NOACCESS = 0x00000001
PAGE_READONLY = 0x00000002
PAGE_READWRITE = 0x00000004
PAGE_WRITECOPY = 0x00000008
PAGE_EXECUTE = 0x00000010
PAGE_EXECUTE_READ = 0x00000020
PAGE_EXECUTE_READWRITE = 0x00000040
PAGE_EXECUTE_WRITECOPY = 0x00000080
PAGE_GUARD = 0x00000100
PAGE_NOCACHE = 0x00000200
PAGE_WRITECOMBINE = 0x00000400


# Structures for CreateProcessA() function
class STARTUPINFO(Structure):
	_fields_ = [
		("cb", DWORD),
		("lpReserved", LPTSTR),
		("lpDesktop", LPTSTR),
		("lpTitle", LPTSTR),
		("dwX", DWORD),
		("dwY", DWORD),
		("dwXSize", DWORD),
		("dwYSize", DWORD),
		("dwXCountChars", DWORD),
		("dwYCountChars", DWORD),
		("dwFillAttribute", DWORD),
		("dwFlags", DWORD),
		("wShowWindow", WORD),
		("cbReserved2", WORD),
		("lpReserved2", LPBYTE),
		("hStdInput", HANDLE),
		("hStdOutput", HANDLE),
		("hStdError", HANDLE),
	]

class PROCESS_INFORMATION(Structure):
	_fields_ = [
		("hProcess", HANDLE),
		("hThread", HANDLE),
		("dwProcessId", DWORD),
		("dwThreadId", DWORD),
	]

	
# DEBUG_EVENT
# referenced by http://niggasin.space/forum/technophiliacs-technophiles/27455-plz-help-with-python-debugger

class EXCEPTION_RECORD(Structure):
    pass
    
EXCEPTION_RECORD._fields_ = [
        ("ExceptionCode",        DWORD),
        ("ExceptionFlags",       DWORD),
        ("ExceptionRecord",      POINTER(EXCEPTION_RECORD)),
        ("ExceptionAddress",     PVOID),
        ("NumberParameters",     DWORD),
        ("ExceptionInformation", UINT_PTR*15),
        ]
		
class EXCEPTION_RECORD(Structure):
	_fields_ = [
		("ExceptionCode", DWORD),
		("ExceptionFlags", DWORD),
		("ExceptionRecord", POINTER(EXCEPTION_RECORD)),
		("ExceptionAddress", PVOID),
		("NumberParameters", DWORD),
		("ExceptionInformation", UINT_PTR*15),
	]
	
class EXCEPTION_DEBUG_INFO(Structure):
	_fields_ = [
		("ExceptionRecord", EXCEPTION_RECORD),
		("dwFirstChance", DWORD),
	]

class CREATE_THREAD_DEBUG_INFO(Structure):
	_fields_ = [
		("hThread", HANDLE),
		("lpThreadLocalBase", LPVOID),
		("lpStartAddress", LPTHREAD_START_ROUTINE),
	]
	
class CREATE_PROCESS_DEBUG_INFO(Structure):
	_fields_ = [
		("hFile", HANDLE),
		("hProcess", HANDLE),
		("hThread", HANDLE),
		("lpBaseOfImage", LPVOID),
		("dwDebugInfoFileOffset", DWORD),
		("nDebugInfoSize", DWORD),
		("lpThreadLocalBase", LPVOID),
		("lpStartAddress", LPTHREAD_START_ROUTINE),
		("lpImageName", LPVOID),
		("fUnicode", WORD),
	]
	
class EXIT_THREAD_DEBUG_INFO(Structure):
	_fields_ = [
		("dwExitCode", DWORD),
	]
	
class EXIT_PROCESS_DEBUG_INFO(Structure):
	_fields_ = [
		("dwExitCode", DWORD),
	]

class LOAD_DLL_DEBUG_INFO(Structure):
	_fields_ = [
		("hFile", HANDLE),
		("lpBaseOfDll", LPVOID),
		("dwDebugInfoFileOffset", DWORD),
		("nDebugInfoSize", DWORD),
		("lpImageName", LPVOID),
		("fUnicode", WORD),
	]
	
class UNLOAD_DLL_DEBUG_INFO(Structure):
	_fields_ = [
		("lpBaseOfDll", LPVOID),
	]
	
class OUTPUT_DEBUG_STRING_INFO(Structure):
	_fields_ = [
		("lpDebugStringData", LPSTR),
		("fUnicode", WORD),
		("nDebugStringLength", WORD),
	]
	
class RIP_INFO(Structure):
	_fields_ = [
		("dwError", DWORD),
		("dwType", DWORD),
	]
	
class DEBUG_EVENT_UNION(Union):
	_fields_ = [
		("Exception", EXCEPTION_DEBUG_INFO),
		("CreateThread", CREATE_THREAD_DEBUG_INFO),
		("CreateProcessInfo", CREATE_PROCESS_DEBUG_INFO),
		("ExitThread", EXIT_THREAD_DEBUG_INFO),
		("ExitProcess", EXIT_PROCESS_DEBUG_INFO),
		("LoadDll", LOAD_DLL_DEBUG_INFO),
		("UnloadDll", UNLOAD_DLL_DEBUG_INFO),
		("DebugString", OUTPUT_DEBUG_STRING_INFO),
		("RipInfo", RIP_INFO),
	]
	
class DEBUG_EVENT(Structure):
	_fields_ = [
		("dwDebugEventCode", DWORD),
		("dwProcessId", DWORD),
		("dwThreadId", DWORD),
		("u", DEBUG_EVENT_UNION),
	]

	
# Used by the CONTEXT structure
class FLOATING_SAVE_AREA(Structure):
	_fields_ = [
		("ControlWord", DWORD),
		("StatusWord", DWORD),
		("TagWord", DWORD),
		("ErrorOffset", DWORD),
		("ErrorSelector", DWORD),
		("DataOffset", DWORD),
		("DataSelector", DWORD),
		("RegisterArea", BYTE*80),
		("Cr0NpxState", DWORD),
	]

# for GetThreadContext() call	
class CONTEXT(Structure):
	_fields_ = [
		("ContextFlags", DWORD),
		("Dr0", DWORD),
		("Dr1", DWORD),
		("Dr2", DWORD),
		("Dr3", DWORD),
		("Dr6", DWORD),
		("Dr7", DWORD),
		("FloatSave", FLOATING_SAVE_AREA),
		("SegGs", DWORD),
		("SegFs", DWORD),
		("SegEs", DWORD),
		("SegDs", DWORD),
		("Edi", DWORD),
		("Esi", DWORD),
		("Ebx", DWORD),
		("Edx", DWORD),
		("Ecx", DWORD),
		("Eax", DWORD),
		("Ebp", DWORD),
		("Eip", DWORD),
		("SegCs", DWORD),
		("EFlags", DWORD),
		("Esp", DWORD),
		("SegSs", DWORD),
		("ExtendedRegisters", BYTE*512),
	
	]
	
# for enumerating all of the system threads
class THREADENTRY32(Structure):
	_fields_ = [
		("dwSize", DWORD),
		("cntUsage", DWORD),
		("th32ThreadID", DWORD),
		("th32OwnerProcessID", DWORD),
		("tpBasePri", DWORD),
		("tpDeltaPri", DWORD),
		("dwFlags", DWORD),
	]
	

# SYSTEM_INFO
# for GetSystemInfo()

class PROC_STRUCT(Structure):
	_fields_ = [
		("wProcessorArchitecture", WORD),
		("wReserved", WORD),
	]
	
class SYSTEM_INFO_UNION(Union):
	_fields_ = [
		("dwOemId", DWORD),
		("sProcStruc", PROC_STRUCT),
	]

class SYSTEM_INFO(Structure):
	_fields_ = [
		("uSysInfo", SYSTEM_INFO_UNION),
		("dwPageSize", DWORD),
		("lpMinimumApplicationAddress", LPVOID),
		("lpMaximumApplicationAddress", LPVOID),
		("dwActiveProcessorMask", DWORD),
		("dwNumberOfProcessors", DWORD),
		("dwProcessorType", DWORD),
		("dwAllocationGranularity", DWORD),
		("wProcessorLevel", WORD),
		("wProcessorRevision", WORD),
	]

# for VirtualQuery()
class MEMORY_BASIC_INFORMATION(Structure):
	_fields_ = [
		("BaseAddress", PVOID),
		("AllocationBase", PVOID),
		("AllocationProtect", DWORD),
		("RegionSize", SIZE_T),
		("State", DWORD),
		("Protect", DWORD),
		("Type", DWORD),
	]