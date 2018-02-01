import unittest
from core import TicketManager


class TestParkingLot(unittest.TestCase):
	ticket_mgr = TicketManager()

	def test_1_create_parking_lot(self):
		output_str = self.ticket_mgr.create_parking_lot(6)
		self.assertEqual('Created a parking lot with 6 slots', output_str)

	def test_2_park_vehicle(self):
		output_str = self.ticket_mgr.park_vehicle('KA-01-HH-1234', 'White')
		self.assertEqual(self.ticket_mgr.vehicles[0].vehicle_no, 'KA-01-HH-1234')
		self.assertEqual('Allocated slot number: 1', output_str)

		output_str = self.ticket_mgr.park_vehicle('KA-01-HH-9999', 'White')
		self.assertEqual('Allocated slot number: 2', output_str)

		output_str = self.ticket_mgr.park_vehicle('KA-01-BB-0001', 'Black')
		self.assertEqual('Allocated slot number: 3', output_str)

		output_str = self.ticket_mgr.park_vehicle('KA-01-HH-7777', 'Red')
		self.assertEqual('Allocated slot number: 4', output_str)

		output_str = self.ticket_mgr.park_vehicle('KA-01-HH-2701', 'Blue')
		self.assertEqual('Allocated slot number: 5', output_str)

		output_str = self.ticket_mgr.park_vehicle('KA-01-HH-3141', 'Black')
		self.assertEqual('Allocated slot number: 6', output_str)

	def test_3_leave_parking_lot(self):
		output_str = self.ticket_mgr.leave_parking_lot(4)
		self.assertEqual('Slot number 4 is free', output_str)

	def test_4_park_vehicle_in_empty_slot(self):
		output_str = self.ticket_mgr.park_vehicle('KA-01-P-333', 'White')
		self.assertEqual('Allocated slot number: 4', output_str)

	def test_5_parking_full(self):
		output_str = self.ticket_mgr.park_vehicle('KA-01-P-333', 'White')
		self.assertEqual('Sorry, parking lot is full', output_str)

	def test_6_get_vehicle_no_with_color(self):
		output_str = self.ticket_mgr.get_vehicle_no_with_color('White')
		self.assertEqual('KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333', output_str)

	def test_7_get_car_slot_no_with_color(self):
		output_str = self.ticket_mgr.get_car_slot_no_with_color('White')
		self.assertEqual('1, 2, 4', output_str)

if __name__ == '__main__':
	unittest.main()
