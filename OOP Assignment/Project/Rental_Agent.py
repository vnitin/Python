from Bike import Bike

class Rental_Agent:

	__customer_who_rented = []

	@classmethod
	def issue_bill(cls, customer_obj, usage_period):
		if len(cls.__customer_who_rented) == 0:
			return "nil"
		bill_value = 0
		if customer_obj.number_of_bikes >= 3 and customer_obj.number_of_bikes <= 5:
			if customer_obj.type_of_rent == "hourly":
				bill_value = customer_obj.number_of_bikes * usage_period * Bike.rent_per_hour() * 0.3
			elif customer_obj.type_of_rent == "daily":
				bill_value = customer_obj.number_of_bikes * usage_period * Bike.rent_per_day() * 0.3
			elif customer_obj.type_of_rent == "weekly":
				bill_value = customer_obj.number_of_bikes * usage_period * Bike.rent_per_week() * 0.3				
		else:
			if customer_obj.type_of_rent == "hourly":
				bill_value = customer_obj.number_of_bikes * usage_period * Bike.rent_per_hour() 
			elif customer_obj.type_of_rent == "daily":
				bill_value = customer_obj.number_of_bikes * usage_period * Bike.rent_per_day()
			elif customer_obj.type_of_rent == "weekly":
				bill_value = customer_obj.number_of_bikes * usage_period * Bike.rent_per_week()
		Bike.return_bike(customer_obj.number_of_bikes)
		cls.__customer_who_rented.remove(customer_obj)
		return bill_value

	@classmethod
	def issue_bike(cls, customer_obj, number_of_bikes, type_of_rent):
		if number_of_bikes > Bike.list_of_available_bikes():
			print("Error: Sufficient bikes are not available for rent")
			return
		Bike.rent_bike(number_of_bikes, type_of_rent)
		cls.__customer_who_rented.append(customer_obj)

	@classmethod
	def display_inventory(cls):
		print("-----List of available bikes-----")
		print(Bike.list_of_available_bikes())
		print("-----List of customers who rented the bike-----")
		if len(cls.__customer_who_rented) == 0:
			print("No bikes in rent")
		for m in cls.__customer_who_rented:
			print("customer name:",m.customer_name, "| number of bikes:", m.number_of_bikes, "| type of rent:", m.type_of_rent)

	@classmethod
	def get_rent_type(cls):
		return Bike.get_rent_type()