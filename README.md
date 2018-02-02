ParkingLot
    - ParkingLot class stores the parking information of the space along the vehicle information(foreign key)
      to it.It has following parameters:
            - lot_number : Identified uniquely the each parking lot
            - vehicle : Foreign key to vehicle class
            - is_occupied : specifies whether parking lot is empty or occupied by vehicle


Vehicle
    - Vehicle class stores information related to vehicle.It has following:
            - vehicle_no : Uniquely identifies the vehicle
            - vehicle_color : specifies the color of the vehicle
            - is_parked : specifies whether vehicle is parked in parking lot or not


TicketManager
    - TickerManager class manages the ticketing system for the parking lot.It has following:
            - parking_lots : Stores the information of parking lots
            - vehicles : Stores the vehicle information


Pre-Requisites:
    Should have python running in the system.
    Please run the requirements.txt if you don't have python


Running Procedure:
    Execute the following command for running the parking lot:

    1) For file input
            Python:
                python parking_lot.py [file_path]
                Ex: python parking_lot.py parking_test.txt
            Unix Shell:
                ./parking_lot.sh [file_path]
                Ex: parking_lot.sh parking_test.txt

    2) For command line input
            Python:
                python parking_lot.py
                Ex: python parking_lot.py
            Unix Shell:
                ./parking_lot.sh
                Ex: ./parking_lot.sh


Running Tests
    Execute the following command for running test cases:
        python test.py