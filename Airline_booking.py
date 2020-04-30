class Flight:
    """An aircraft system that has a make, registration, sitting capacity,luggage capcity and manifest. 
    """
    def __init__(self, make, registration, sitting,luggage):
        """Declare flight properties
        - make, str
        - registration no, str
        - sitting capacity,int
        - luggage capacity,int
        - manifest,dict
        """
        self.make = make
        self.registration = registration
        self.sitting = sitting
        self.luggage = luggage
        self.manifest= {}
    
    def _passenger_list(self):
        """
        return a list of booked passengers in lowercase"""
        passengers = [line.lower() for line in list(self.manifest.keys())]
        return passengers
    
    def declare_manifest(self):
        if len(self.manifest) == 0:
            print(f"No Bookings Yet\nThis is our status>")
            self.status()
        else:
            print(f"This is the manifest for {self.make}\n")
            print(f"Passenger | Checked-In | Luggage")
            for i, line in self.manifest.items():
                print(f"{i} | {line['checked_in']} | {str(line['luggage']) + 'kg'}")
                print('*' * (len(i) + len(str(line['checked_in']))+ 5))
    
    def status(self):
        """print details of Flight object showing: Flight no, reg, with sitting and luggage capacity available
        """
        print(f"Flight name => {self.make}\nFlight No. => {self.registration}\nSitting Capacity Available => {self.sitting}\nLuggage Capacity Available => {self.luggage}kg")
        
    def booking(self, passenger,seat,luggage):
        """passenger:name of passenger, str
        seat: numberof seats to book, int
        luggage: weight of luggage,int
        
        Checks sitting and luggage availability and books a passenger(s) in the flight by getting their name and reducing the seats and luggage capacity if the ane by number of seats and luggage passed.
        
        If more than one seat is requested, get othername from passenger.
        Initial booking has status passenger(s) as not checked in.
        """
        if (self.sitting >= 1) and (luggage < self.luggage):
            if seat == 1:
                self.manifest[passenger]= {
                    'checked_in': False,
                    'luggage': luggage
                } 
                self.sitting -= seat
                self.luggage -=luggage
            else:
                self.manifest[passenger] = {'checked_in':False, 'luggage':luggage}
                self.sitting -= 1
                
                print(f'we need the names and luggage capacity of the other {seat-1} passengers')
                for item in range(seat-1):
                    print('Type name of next passenger:')
                    name1 = input(">>> ")
                    print(f"What is {name1}'s luggage capacity:")
                    lug1 = int(input(">>> "))
                    self.manifest[name1] = {'checked_in':False, 'luggage':lug1}
                    self.sitting -= 1
                    self.luggage -= lug1
                    print(f"{name1} with {lug1}kg of luggage booked!")
        else:
            print("We are fully booked")

    def check_in(self, passenger):
        passengers = self._passenger_list()
        if passenger.lower() in passengers:
            self.manifest[passenger]['checked_in'] = True
            print(f"{passenger} checked in")
        else:
            print(f"{passenger} not on the manifest")
            
    def is_checked_in(self, passenger):
        passengers = self._passenger_list()
        if passenger.lower() in passengers:
            print(self.manifest.get(passenger).get('checked_in'))
        else:
            print(f"{passenger} not on the manifest")
            
#Make a flight and print out details
plane = Flight("Airbus100", "AB12",50,200)
#Get status
plane.status()
print('\n')
#Declare Manifest
plane.declare_manifest()
print('\n')
plane.is_checked_in('Paschal')
print('\n')
plane.booking('Paschal', 1, 20)
plane.is_checked_in('Paschal')
print('\n')
plane.check_in('Paschal')
plane.is_checked_in('Paschal')
print('\n')
plane.status()
