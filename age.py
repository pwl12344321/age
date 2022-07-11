driving = input('Have you ever driven a car? ')
if driving != 'yes' and driving != 'no':
	print('please enter "yes" or "no"')
	raise SystemExit

age = input('What is your age: ')
age = int(age)

if driving == 'yes':
	if age >= 18:
		print('you pass the test')
	else:
		print('you should not have driven!')
elif driving == 'no':
	if age >= 18:
		print('you can get a driver license')
	else:
		print('you can get a driver license when you are passed 18')
else:
	print('please enter "yes" or "no"')
	