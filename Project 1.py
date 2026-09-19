
employee_name = input('Employee: ')
hours_worked = float(input('Hours worked: '))
hourly_rate = float(input('Hourly rate pay: '))
tax_rate = float(input('Tax Rate as (%): '))

gross_pay = hours_worked * hourly_rate
tax_witheld = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_witheld
print(f'Employee: {employee_name}')
print(f'Gross pay: ${gross_pay: .2f}')
print(f'Tax witheld: ${tax_witheld: .2f}')
print(f'Net pay: ${net_pay: .2f}')

Program =  'paycheck.py'
