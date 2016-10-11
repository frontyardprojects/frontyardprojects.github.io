# user workflow: python fy_cashflow.py > money.yml
# change key variables:
# 	balance: current bank balance (Westpac account)
# 	date: current date ('day/month/year')
#	debt: current debt(s) total
#	closure_fund: closure fund total	
#	to_archive_balance: last balance value [auto-added from previous]
#	to_archive_date: last date [auto-added from previous]
#	to_archive_debt: when debt is paid, last debt value 
#	to_archive_paid_date: when debt is paid, date of payment ('day/month/year')

balance =
date =
debt = 00.00 
closure_fund = 2000.00

to_archive_balance = 2475.01
to_archive_date = '11/10/2016'
to_archive_debt = None
to_archive_paid_date = None
to_archive_closure_fund = None
to_archive_closure_date = None

##### ###### ######
bf_preamble = ('#' + '\n' +
	'# top value shows (+ bank balance - closure fund - debts)' + '\n' + 
	'# archive shows bank balance' + '\n' +
	'# over time we show a graph of our finances' + '\n' +
	'# e.g.' + '\n' +
	'# - value: x' + '\n' +
	'#   date: Day/Month/Year' + '\n' +
	'#')

balance_archive =['- value: 2547.86', '  date: 02/10/2016', '- value: 2297.27', '  date: 21/09/2016', '- value: 2002.94', '  date: 14/09/2016', '- value: 2364.74', '  date: 15/08/2016', '- value: 2207.16', '  date: 29/07/2016', '- value: 2580.13', '  date: 17/07/2016', '- value: 2579.37', '  date: 27/06/2016', '- value: 2383.33', '  date: 07/06/2016']

debt_archive =['- debt: 422.97', '  date_paid: 29/07/2016']

closure_fund_archive =['- closure: 2000.00', '  necessary_as_of_date: 01/08/2016']

def update_balance():
	total_value = balance - closure_fund - debt
	print bf_preamble
	print '- value:', total_value
	print '  date:', date

def update_balance_archive():
	if to_archive_balance and to_archive_date: 
		balance_archive.insert(0, ('- value: ' + str(to_archive_balance)))		
		balance_archive.insert(1, ('  date: ' + to_archive_date))
	print '\n'.join(balance_archive)

def update_debt_archive(): 
	if to_archive_debt and to_archive_paid_date:
		debt_archive.insert(0, ('- debt: ' + str(to_archive_balance)))	
		debt_archive.insert(1, ('  date_paid: ' + to_archive_paid_date))
	print
	print '\n'.join(debt_archive)
	
def update_closure_fund_archive():
	if to_archive_closure_fund and to_archive_closure_date:
		closure_fund_archive.insert(0, ('- value: ' + str(to_archive_closure_fund)))		
		closure_fund_archive.insert(1, ('  necessary_as_of_date: ' + to_archive_closure_date))
	print
	print '\n'.join(closure_fund_archive)	

def update_cashfile(file, line, text):
	y = open(file, 'r').readlines()
	output = open(file, 'w')
	y[line] = text
	output.writelines(y)
	y = None
	output.close()		
	
###### ###### ######	

update_balance()

update_balance_archive()

update_debt_archive()

update_closure_fund_archive()

update_cashfile('fy_cashflow.py', 33, 'balance_archive =' +
	''.join('{0}'.format(balance_archive)) +
	'\n')
	
update_cashfile('fy_cashflow.py', 35, 'debt_archive =' +
	''.join('{0}'.format(debt_archive)) +
	'\n')

update_cashfile('fy_cashflow.py', 37, 'closure_fund_archive =' +
	''.join('{0}'.format(closure_fund_archive)) +
	'\n')

update_cashfile('fy_cashflow.py', 16, 'to_archive_balance = ' +
	str(balance) +
	'\n')
	
update_cashfile('fy_cashflow.py', 17, 'to_archive_date = \'' + 
	date + '\'' +
	'\n')

update_cashfile('fy_cashflow.py', 11, 'balance =' +
	'\n')

update_cashfile('fy_cashflow.py', 12, 'date =' +
	'\n')	
	

