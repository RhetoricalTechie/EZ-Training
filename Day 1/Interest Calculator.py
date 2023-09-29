balance = 100000
roi = 12
months = 12
count = 0
for i in range(months):
	final = (roi/100 * balance)/12
	balance = final + balance
	count = count + 1
	if count == 5:
		balance = balance - 25000
	elif count == 9:
		balance = balance + 10000
	else :
		print(balance)