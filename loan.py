# loan calculator

# getters for user input variables with validations
def ask_total_amount():
	total_amount = None
	while total_amount is None:
		user_input = input("How much do you owe in dollars?\n >> $")
		try:
			total_amount = float(user_input)
		except ValueError:
			print(user_input, "is not valid amount; try again")
	if total_amount <= 0:
		print("You cannot have a negative loan")
	return total_amount

def ask_apr():
	apr = None
	while apr is None:
		user_input = input("What is the APR in percentage?\n >> ")
		try:
			apr = float(user_input)
		except ValueError:
			print(user_input, "is not a valid APR; try again")
	if (apr < 0):
		print("You cannot have a negative APR")
	return apr

def ask_monthly_payment():
	monthly_payment = None
	while monthly_payment is None:
		user_input = input("How much are you paying back each month, in dollars?\n >> $")
		try:
			monthly_payment = float(user_input)
		except ValueError:
			print(user_input, "is not a valid amount; try again")
	if monthly_payment <= 0:
		print("You cannot have zero or negative payment plan")
	return monthly_payment

def ask_months():
	months = None
	while months is None:
		user_input = input("How many months do you want the results for?\nType 0 to view all payments until the last instalment.\n >> ")
		try:
			months = int(user_input)
		except ValueError:
			print(user_input, "is not a valid number of months")
	if months < 0:
		print("You cannot view the loan payment plan for negative number of months")
	return months

# loan details
total_amount = ask_total_amount()
apr = ask_apr()
monthly_payment = ask_monthly_payment()
months = ask_months()

# find monthly APR
monthly_rate = apr/100/12

def calculate(total_amount, monthly_rate, monthly_payment):
	# add interest
	interest_paid = total_amount * monthly_rate
	total_amount += interest_paid

	# make payment
	total_amount -= monthly_payment	

	if(total_amount < 0):
		total_amount = 0

	# print results for the end of the month
	print("$", "{:.2f}".format(interest_paid), " was interest.\t", sep="", end=" ")
	print("Now you owe $", "{:.2f}".format(total_amount), sep="")
	return total_amount

i = 0
if(months == 0):
	while(total_amount > 0):
		i += 1
		print("Month ", i, ":\t", sep="", end="")
		total_amount = calculate(total_amount, monthly_rate, monthly_payment)
		
	print("You have paid off your loan in", i, "months!")
else:
	while (i < months) and (total_amount > 0):
		i += 1
		print("Month ", i, ":\t", sep="", end="")
		total_amount = calculate(total_amount, monthly_rate, monthly_payment)
	if(i < months):
		print("You have paid off your loan a bit sooner than you expected:", i, "months!")