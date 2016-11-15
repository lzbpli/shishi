import datetime

if __name__ == '__main__':

	prinr(datetime.date.tody().strftime('%d/%m/%Y'))
	miyazakiBirthDate = datetime.date(1941,1,5)
	print(miyazakiBirthDate.strftime('%d/%m/%Y'))
	miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(day = 1)
	print (miyazakiBirthNextDay.strftime('%d/%m/%Y'))
	miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year +1)
	print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))
