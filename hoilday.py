from tabulate import tabulate
# SY23120012457
# Skills Bootcamp in Software Engineering (Fundamentals)
# Task 16 - Programming with User-defined Functions
# 10-023 Programming with User-defined Functions 
# Practical Task 1
# holiday.py
# 13-Feb-2024 V1

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

# Define function of welcome pages
def welcomepage():
    print(Color.decorate(r"     x      \\               |   x                                         ", 'GREEN'))
    print(Color.decorate(r"     x .    x              -.x.- x                                         ", 'GREEN'))
    print(Color.decorate(r"     x  .   x   .x.    .x.   |   x .x.    .x.    .x.   .xx.                ", 'GREEN'))
    print(Color.decorate(r"     x   \\  x  x  x  x  \\  |   x    x  ||  \\ x   \\ x  \\               ", 'GREEN'))
    print(Color.decorate(r"     x    . x  x   x  x      |   x    x  x...x  x      x   x               ", 'GREEN'))
    print(Color.decorate(r"     x     .x  x   x  x      |   x    x  \\     x      x   x               ", 'GREEN'))
    print(Color.decorate(r"     x      x   .x.   x      x   x    x   .x./  x      x   x               ", 'GREEN'))
    print(Color.decorate(r"                 |             |     |                                     ", 'CYAN'))
    print(Color.decorate(r"                 |      *  __  |__  -|- .--.                               ", 'CYAN'))
    print(Color.decorate(r"                 |      | |  | |  |  |  |                                  ", 'CYAN')) 
    print(Color.decorate(r"                 .__.   | |__| |  |  |  .--.                               ", 'CYAN'))
    print(Color.decorate(r"                             |       |     |                               ", 'CYAN'))
    print(Color.decorate(r"                          |__.          .--.   Tours                       ", 'CYAN'))
    print(Color.decorate(r" . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ", 'CYAN'))

# Define flight_name for print
def flight_name(city_flight):
    # Define flight_name 
    flightname= {
        "1" : "Iceland - Keflavík International Airport (KEF)",
        "2" : "Norway - Tromsø Airport, Langnes (TOS)",
        "3" : "Sweden - Kiruna Airport (KRN)",
        "4" : "Finland - Rovaniemi Airport (RVN)"
    }
    # Get the cost per night based on the selected city
    strflightname = flightname.get(city_flight, 0)
    return strflightname

# Define function to calculate flight cost based on destination city
def plane_cost(city_flight):
    # Define flight costs for different cities
    city_costs = {
        "1": 198,    # Iceland
        "2": 476,    # Norway
        "3": 178,    # Sweden
        "4": 240     # Finland
    }

    # Check if the city is in the dictionary, if not, return a default value of 0
    return city_costs.get(city_flight, 0)

# Define function to calculate hotel cost based on destination city and number of nights
def hotel_cost(city_flight, num_nights):
    # Define hotel costs for different cities
    hotel_costs = {
        "1": 178,    # Iceland
        "2": 149,    # Norway
        "3": 148,    # Sweden
        "4": 154     # Finland
    }
    # Get the cost per night based on the selected city
    cost_per_night = hotel_costs.get(city_flight, 0)
    return num_nights * cost_per_night

# Define function to calculate car rental cost based on destination city and number of days
def car_rental(city_flight, rental_days):
    # Define car rental costs for different cities
    car_rental_costs = {
        "1": 79,    # Iceland
        "2": 87,    # Norway
        "3": 104,   # Sweden
        "4": 124    # Finland
    }
    # Get the cost per rental 4x4 car based on the selected city
    cost_car_rental = car_rental_costs.get(city_flight, 0)
    return rental_days * cost_car_rental

# Define function to calculate total holiday cost
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

# Define function to validate city_flight input
def validate_city_flight(city_flight):
    return city_flight in ["1", "2", "3", "4"]

# Define function to validate num_nights input
def validate_num_nights(num_nights):
    return num_nights.isdigit() and int(num_nights) <= 90     


def validate_rental_days(rental_days, num_nights):
    return rental_days.isdigit()  and int(rental_days) <= num_nights

# call welcomepage
print()
welcomepage()

# Display the flight options to the user
print('''Northern Line Night Tour ✈️ 
1. Iceland - Keflavík International Airport (KEF)
2. Norway - Tromsø Airport, Langnes (TOS)
3. Sweden - Kiruna Airport (KRN)
4. Finland - Rovaniemi Airport (RVN)''')

# Get user inputs for city_flight and validate
city_flight = input("Enter the number corresponding to the city you will be flying to: ")
while not validate_city_flight(city_flight):
#    print(color.PURPLE + "Error: Please enter a valid city number." + color.END)
    print(Color.decorate("Error: Please enter a valid city number."  ,'PURPLE'))
    city_flight = input("Enter the number corresponding to the city you will be flying to: ")

# Get user input for num_nights and validate
num_nights = input("Enter the number of nights you will be staying at a hotel: ")
while not validate_num_nights(num_nights):
    print(Color.decorate("Error: Please enter a valid number of nights not exceeding 90 days." ,'PURPLE'))
    num_nights = input("Enter the number of nights you will be staying at a hotel: ")
num_nights = int(num_nights)

# Get user input for rental_days and validate
rental_days = input("Enter the number of days for which you will be hiring a 4x4 car: ")
while not rental_days.isdigit():
    print(Color.decorate("Error: Please enter a valid number for rental days." ,'PURPLE'))
    rental_days = input("Enter the number of days for which you will be hiring a 4x4 car: ")

while not validate_rental_days(rental_days, num_nights):
    emsg = Color.decorate(
        f"Error: Rental days cannot exceed the number of nights at the hotel."
        " Please enter a valid value.",
        'PURPLE'
    )
    print(emsg)
    rental_days = input("Enter the number of days for which you will be hiring a 4x4 car: ")
rental_days = int(rental_days)  # Convert validated input to integer

# Calculate costs
hotel_total = hotel_cost(city_flight, num_nights)
plane_total = plane_cost(city_flight)
car_total = car_rental(city_flight, rental_days)
total_cost = holiday_cost(hotel_total, plane_total, car_total)

print(Color.decorate("\nHoliday Details:" ,'BLUE'))
print(Color.decorate("----------------" ,'BLUE'))

table = [
    ["Destination City:", flight_name(city_flight)],
    ["Number of Nights at Hotel:", num_nights],
    ["Number of Days for Car Rental:", rental_days],
    ["Flight Cost:", "£" + str(plane_total)],  # Need to concatenate strings
    ["Hotel Cost:", "£" + str(hotel_total)],   # Need to concatenate strings
    ["Car Rental Cost:", "£" + str(car_total)],  # Need to concatenate strings
    ["Total Holiday Cost", "£" + str(total_cost)]  # Need to concatenate strings
]

print(tabulate(table, headers=["Items List", "Details"], tablefmt="fancy_outline"))
