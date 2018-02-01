ParkingLot
    - ParkingLot class stores the parking information of the space along the vehicle information(foreign key)
      to it.It has following parameters:
            -lot_number : Identified uniquely the each parking lot
            -vehicle : Foreign key to vehicle class
            -is_occupied : specifies whether parking lot is empty or occupied by vehicle


Vehicle
    - Vehicle class stores information related to vehicle.It has following:
            -vehicle_no : Uniquely identifies the vehicle
            -vehicle_color : specifies the color of the vehicle
            -is_parked : specifies whether vehicle is parked in parking lot or not
