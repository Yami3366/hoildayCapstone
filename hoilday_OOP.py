from tabulate import tabulate
# SY23120012457
# Skills Bootcamp in Software Engineering (Fundamentals)
# Task 16 - Programming with User-defined Functions
# 10-023 Programming with User-defined Functions 
# Practical Task 1
# holiday.py
# 13-Feb-2024 V1
# 15-Mar-2024 V2
# holiday_OOP.py

#text color 
class Color:
    COLORS = {
        'PURPLE': '\033[95m',
        'CYAN': '\033[96m',
        'DARKCYAN': '\033[36m',
        'BLUE': '\033[94m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'RED': '\033[91m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m',
        'END': '\033[0m'
    }

    @classmethod
    def decorate(cls, text, color):
        color_code = cls.COLORS.get(color.upper())
        if color_code:
            return f"{color_code}{text}{cls.COLORS['END']}"
        else:
            return text
    # calling functon
    # print(Color.decorate('Hello, World!', 'BLUE'))





class HolidayCostCalculator:
    def __init__(self):
        self.city_costs = {
            "1": 198,    # Iceland
            "2": 476,    # Norway
            "3": 178,    # Sweden
            "4": 240     # Finland
        }
        self.hotel_costs = {
            "1": 178,    # Iceland
            "2": 149,    # Norway
            "3": 148,    # Sweden
            "4": 154     # Finland
        }
        self.car_rental_costs = {
            "1": 79,    # Iceland
            "2": 87,    # Norway
            "3": 148,   # Sweden
            "4": 154    # Finland
        }
        
    # Define function of welcome pages
    def welcomepage(self):
        print(Color.decorate(r"     x      \\                |   x                                        ", 'GREEN'))
        print(Color.decorate(r"     x .    x              \\.x.\\ x                                       ", 'GREEN'))
        print(Color.decorate(r"     x  .   x   .x.    .x.   |   x .x.    .x.    .x.     .xx.                 ", 'GREEN'))
        print(Color.decorate(r"     x   \\ x  x   \\ x   \\ |   x    x  \\   \\ x   \\ x   \\         ", 'GREEN'))
        print(Color.decorate(r"     x    . x  x   x  x      |   x    x  x...x x x      x    x                ", 'GREEN'))
        print(Color.decorate(r"     x     .x  x   x  x      |   x    x  \\      x      x    x               ", 'GREEN'))
        print(Color.decorate(r"     x      x   .x.   x      x   x    x   .x./   x      x    x               ", 'GREEN'))
        print(Color.decorate(r"                 |             |     |                                     ", 'CYAN'))
        print(Color.decorate(r"                  |      *  __  |__  -|- .--.                               ", 'CYAN'))
        print(Color.decorate(r"                 |      | |  | |  |  |  |                                  ", 'CYAN')) 
        print(Color.decorate(r"                 .__.   | |__| |  |  |  .--.                               ", 'CYAN'))
        print(Color.decorate(r"                             |             |                               ", 'CYAN'))
        print(Color.decorate(r"                          |__.          .--.   Tours                       ", 'CYAN'))
        print(Color.decorate(r" . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", 'CYAN'))

    def validate_city_flight(self, city_flight):
        return city_flight in self.city_costs.keys()

    def validate_num_nights(self, num_nights):
        return num_nights.isdigit() and int(num_nights) <= 90

    def validate_rental_days(self, rental_days, num_nights):
        return rental_days.isdigit() and int(rental_days) <= num_nights

    def calculate_costs(self, city_flight, num_nights, rental_days):
        if not self.validate_city_flight(city_flight):
            raise ValueError("Invalid city flight")
        if not self.validate_num_nights(num_nights):
            raise ValueError("Invalid number of nights")
        if not self.validate_rental_days(rental_days, int(num_nights)):
            raise ValueError("Invalid number of rental days")

        hotel_total = self.hotel_costs[city_flight] * int(num_nights)
        plane_total = self.city_costs[city_flight]
        car_total = self.car_rental_costs[city_flight] * int(rental_days)
        total_cost = hotel_total + plane_total + car_total

        return {
            "hotel_total": hotel_total,
            "plane_total": plane_total,
            "car_total": car_total,
            "total_cost": total_cost
        }

    def print_holiday_details(self, city_flight, num_nights, rental_days, costs):
        
        table = [
                    ["Destination City:", city_flight],
                    ["Number of Nights at Hotel:", num_nights],
                    ["Number of Days for Car Rental:", rental_days],
                    ["Flight Cost:", "£" + str(costs["plane_total"])],  
                    ["Hotel Cost:", "£" + str(costs["hotel_total"])],  
                    ["Car Rental Cost:", "£" + str(costs["car_total"])],  
                    ["Total Holiday Cost", "£" + str(costs["total_cost"])]  
                ]

        print(tabulate(table, headers=["Items List", "Details"], tablefmt="fancy_outline"))



# Create an instance of HolidayCostCalculator
calculator = HolidayCostCalculator()
calculator.welcomepage()
print()

# Display the flight options to the user
print('''Northern Line Night Tour ✈️ 
1. Iceland - Keflavík International Airport (KEF)
2. Norway - Tromsø Airport, Langnes (TOS)
3. Sweden - Kiruna Airport (KRN)
4. Finland - Rovaniemi Airport (RVN)''')
print()
# Get user inputs
city_flight = input("Enter the number corresponding to the city you will be flying to: ")
num_nights = input("Enter the number of nights you will be staying at a hotel: ")
rental_days = input("Enter the number of days for which you will be hiring a 4x4 car: ")

# Calculate costs
try:
    costs = calculator.calculate_costs(city_flight, num_nights, rental_days)
    print(Color.decorate("\nHoliday Fee Details:" ,'BLUE'))
    print(Color.decorate("---------------------" ,'BLUE'))

    # Print holiday details
    calculator.print_holiday_details(city_flight, num_nights, rental_days, costs)
except ValueError as e:
    print("Error:", e)
