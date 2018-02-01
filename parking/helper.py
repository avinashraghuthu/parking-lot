from core import *


def parse_n_execute_command(ticket_mgr_obj, command_str):
	splitted_commd_str = command_str.split()
	try:
		if splitted_commd_str[0] == CREATE_PARKING_LOT:
			lot_number = int(splitted_commd_str[1])
			ticket_mgr_obj.create_parking_lot(lot_number)
		elif splitted_commd_str[0] == PARK_VEHICLE:
			ticket_mgr_obj.park_vehicle(splitted_commd_str[1], splitted_commd_str[2])
		elif splitted_commd_str[0] == LEAVE_PARKING:
			lot_number = int(splitted_commd_str[1])
			ticket_mgr_obj.leave_parking_lot(lot_number)
		elif splitted_commd_str[0] == GET_PARKING_STATUS:
			ticket_mgr_obj.get_current_parking_status()
		elif splitted_commd_str[0] == GET_REGISTRATION_NO_WITH_COLOR:
			ticket_mgr_obj.get_vehicle_no_with_color(splitted_commd_str[1])
		elif splitted_commd_str[0] == GET_SLOT_NO_WITH_COLOR:
			ticket_mgr_obj.get_car_slot_no_with_color(splitted_commd_str[1])
		elif splitted_commd_str[0] == GET_SLOT_NO_WITH_REG_NO:
			ticket_mgr_obj.get_car_slot_no_with_vehicle_no(splitted_commd_str[1])
	except IndexError, e:
		print STR_INSUFFICIENT_PARAMETERS


def read_file(ticket_mgr_obj, file_path):
	try:
		f = open(file_path)
		for line in f.readlines():
			line = line.strip()
			parse_n_execute_command(ticket_mgr_obj, line)
	except IOError, e:
		print STR_NO_SUCH_FILE_FOUND


