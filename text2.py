hours=int(input('Enter Hours: '))
rate=int(input('Enter Rate: '))
if hours>40:
    pay=hours*rate*1.5
else:
    pay=hours*rate
print('Pay: ', pay)

