
class Bike:
	
	__total_number_of_bikes = 0
	__rent_per_hour = 5
	__rent_daily = 20
	__rent_per_week = 60
	__rent_types = ["hourly", "daily", "weekly"]

	@classmethod
	def add_bike_to_inventory(cls, number_of_bikes):
		cls.__total_number_of_bikes = number_of_bikes

	@classmethod
	def list_of_available_bikes(cls):
		return cls.__total_number_of_bikes

	@classmethod
	def calculate_rent(cls, number_of_bikes, type_of_rent):
		pass

	@classmethod
	def rent_bike(cls, number_of_bikes, type_of_rent):
		cls.__total_number_of_bikes -= number_of_bikes

	@classmethod
	def return_bike(cls, number_of_bikes):
		cls.__total_number_of_bikes += number_of_bikes

	@classmethod
	def rent_per_hour(cls):
		return cls.__rent_per_hour

	@classmethod
	def rent_per_day(cls):
		return cls.__rent_daily

	@classmethod
	def rent_per_week(cls):
		return cls.__rent_per_week

	def __init__(self, number_of_bikes):
		Bike.add_bike_to_inventory(number_of_bikes)

	@classmethod
	def get_rent_type(cls):
		return cls.__rent_types

