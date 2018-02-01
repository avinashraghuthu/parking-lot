from constants import *


class ParkingLot(object):

	def __init__(self, lot_number, vehicle, is_occupied):
		self.lot_number = str(lot_number)
		self.vehicle = vehicle
		self.is_occupied = is_occupied


class Vehicle(object):

	def __init__(self, vehicle_no, vehicle_color, is_parked):
		self.vehicle_no = str(vehicle_no)
		self.vehicle_color = vehicle_color
		self.is_parked = is_parked


class TicketManager(object):

	def __init__(self):
		self.parking_lots = []
		self.vehicles = []

	def create_parking_lot(self, lot_size):
		for i in xrange(1, lot_size+1):
			parking_lot = ParkingLot(i, None, False)
			self.parking_lots.append(parking_lot)
		print STR_PARKING_CREATION_SUCCESS % str(lot_size)

	def get_vehicle_for_parking(self, vehicle_no, vehicle_color):
		vehicle = Vehicle(vehicle_no, vehicle_color, True)
		self.vehicles.append(vehicle)
		return vehicle

	def get_empty_slot(self):
		for parking_lot in self.parking_lots:
			if not parking_lot.is_occupied:
				return parking_lot
		return None

	def park_vehicle(self, vehicle_no, vehicle_color):
		parking_lot = self.get_empty_slot()
		if parking_lot:
			parking_lot.is_occupied = True
			parking_lot.vehicle = self.get_vehicle_for_parking(vehicle_no, vehicle_color)
			print STR_VEHICLE_PARKING_SUCCESS % parking_lot.lot_number
		else:
			print STR_PARKING_LOT_FULL

	def leave_parking_lot(self, lot_number):
		if lot_number <= len(self.parking_lots):
			parking_lot = self.parking_lots[lot_number-1]
			parking_lot.vehicle.is_parked = False
			parking_lot.is_occupied = False
			parking_lot.vehicle = None
			print STR_LEAVE_PARKING_SUCCESS % parking_lot.lot_number
		else:
			print STR_WRONG_LOT_NO

	def get_current_parking_status(self):
		if self.parking_lots:
			print 'SlotNo.     Registration No         Color'
			for parking_lot in self.parking_lots:
				if parking_lot.is_occupied:
					vehicle = parking_lot.vehicle
					print str(parking_lot.lot_number) + '      ' + vehicle.vehicle_no+\
							'      ' + vehicle.vehicle_color
		else:
			print STR_PARKING_LOT_EMPTY

	def get_vehicle_no_with_color(self, color):
		registration_numbers = []
		for parking_lot in self.parking_lots:
			vehicle = parking_lot.vehicle
			if parking_lot.is_occupied and vehicle.vehicle_color == color:
				registration_numbers.append(vehicle.vehicle_no)
		if registration_numbers:
			print ", ".join(registration_numbers)
		else:
			print STR_NO_VEHICLES_FOUND

	def get_car_slot_no_with_color(self, color):
		slot_numbers = []
		for parking_lot in self.parking_lots:
			vehicle = parking_lot.vehicle
			if parking_lot.is_occupied and vehicle.vehicle_color == color:
				slot_numbers.append(parking_lot.lot_number)
		if slot_numbers:
			print ", ".join(slot_numbers)
		else:
			print STR_NO_VEHICLES_FOUND

	def get_car_slot_no_with_vehicle_no(self, vehicle_no):
		slot_numbers = []
		for parking_lot in self.parking_lots:
			vehicle = parking_lot.vehicle
			if parking_lot.is_occupied and vehicle.vehicle_no == vehicle_no:
				slot_numbers.append(parking_lot.lot_number)
		if slot_numbers:
			print ", ".join(slot_numbers)
		else:
			print STR_NO_VEHICLES_FOUND

