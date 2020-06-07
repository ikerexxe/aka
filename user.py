import datetime

class User:

	def __init__(self, dni, cont, inst, date, hour):		
		self.dni = dni
		self.cont = cont
		self.inst = inst
		self.date = self.calculate_date(date)
		self.hour = self.calculate_hour(hour)

	#return day/month/year
	def calculate_date(self, date):
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
		elif(datetime.datetime.now().weekday() == 6 and day == 0):
			date = self.convert_date()

		return date

	def convert_date(self):
		formal_date = datetime.datetime.today() + datetime.timedelta(days=1)
		date = formal_date.strftime("%d/%m/%Y")
		return date

	#return 10
	def calculate_hour(self, hour):
		if(hour == "18:10 - 19:20"):
			index = 10
		return index
