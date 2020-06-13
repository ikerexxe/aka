import datetime

class User:

	def __init__(self, dni, cont, inst, dates, hours):		
		self.dni = dni
		self.cont = cont
		self.inst = inst
		self.date = self.calculate_date(dates)
		self.hour = self.calculate_hour(hours)

	#return day/month/year
	def calculate_date(self, dates):
		self.count = 0
		for date in dates:
			if(date == "Lunes"):
				day = 0
			elif(date == "Martes"):
				day = 1
			elif(date == "Miercoles"):
				day = 2
			elif(date == "Jueves"):
				day = 3
			elif(date == "Viernes"):
				day = 4
			elif(date == "Sabado"):
				day = 5
			elif(date == "Domingo"):
				day = 6

			if(datetime.datetime.now().weekday() + 1 == day):
				date = self.convert_date()
				break
			elif(datetime.datetime.now().weekday() == 6 and day == 0):
				date = self.convert_date()
				break
			else:
				date = -1
 
			self.count += 1

		return date

	def convert_date(self):
		formal_date = datetime.datetime.today() + datetime.timedelta(days=1)
		date = formal_date.strftime("%d/%m/%Y")
		return date

	#return 10
	def calculate_hour(self, hours):
		index = 0

		if(self.date != -1):
			if(hours[self.count] == "10:15 - 11:25"):
				index = 2
			elif(hours[self.count] == "11:30 - 12:40"):
				index = 3
			elif(hours[self.count] == "18:10 - 19:20"):
				index = 10

		return index
