from Bike import Bike
from Customer import *
from Rental_Agent import Rental_Agent as RA

def main():
	pass	

if __name__ == "__main__":
	populate_inventory = Bike(10)

	RA.display_inventory()

	customer1 = Customer("Akash")

	try:
		customer1.rent_bike(1, "hourly")
	except RentTypeerror:
		print("Cannot rent due to invalid rent type")
	
	RA.display_inventory()

	total_bill = customer1.return_bike(2.5)
	if total_bill == None:
		pass
	else:
		print("Total bill value is:",total_bill)

	RA.display_inventory()

	try:
		customer1.rent_bike(1, "daily")
	except RentTypeerror:
		print("Cannot rent due to invalid rent type")

	RA.display_inventory()

	total_bill = customer1.return_bike(2.5)
	if total_bill == None:
		pass
	else:
		print("Total bill value is:",total_bill)

	RA.display_inventory()