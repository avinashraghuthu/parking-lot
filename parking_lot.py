import sys
from parking.helper import *


def run_parking_lot():
	try:
		cmd_arguments = sys.argv
		ticket_mgr_obj = TicketManager()
		if len(cmd_arguments) == 2:
			read_file(ticket_mgr_obj, cmd_arguments[1])
		elif len(cmd_arguments) == 1:
			print "Please enter your commands:\n"
			while True:
				print 'Input:\n'
				input_cmd = (raw_input()).strip()
				print '\n'
				print 'Output:\n'
				parse_n_execute_command(ticket_mgr_obj, input_cmd)
				print '\n'
		else:
			print STR_INVALID_ARG
	except Exception, e:
		print STR_UNHANDLED_EXCEPTION


run_parking_lot()
