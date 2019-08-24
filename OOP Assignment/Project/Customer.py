from Rental_Agent import Rental_Agent

class Customer:

	def __init__(self, name):
		self.__customer_name = name
		self.__number_of_bikes = 0
		self.__type_of_rent = ""
		self.__issue_date = 0
		self.__return_date = 0

	@property
	def customer_name(self):
		return self.__customer_name
	
	@property
	def number_of_bikes(self):
		return self.__number_of_bikes

	@property
	def type_of_rent(self):
		return	self.__type_of_rent

	def rent_bike(self, number_of_bikes, type_of_rent):
		if self.__number_of_bikes > 0:
			print("Error: You have already rented bikes earlier, you cannot rent again")
			return
		if type_of_rent not in Rental_Agent.get_rent_type():
			raise RentTypeerror(type_of_rent)
		self.__number_of_bikes = number_of_bikes
		self.__type_of_rent = type_of_rent
		self.__issue_date = 0
		self.__return_date = 0
		Rental_Agent.issue_bike(self, number_of_bikes, type_of_rent)

	def return_bike(self, usage_period):
		if self.__number_of_bikes == 0:
			print("Error: No bike to return")
			return
		bill_value = Rental_Agent.issue_bill(self, usage_period)
		self.__number_of_bikes = 0
		return bill_value

	def display_available_bikes(self):
		return Rental_Agent.display_inventory()

class RentTypeerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg

if __name__ == "__main__":
	try:
		customer1 = Customer("Sandeep", 2, "daily")
	except RentTypeerror:
		print("cannot create object")
	else:
		customer1.display_available_bikes()