
# New contact book 

# copyright of this code have Abdirizak abdullahi hussein 


contact = {}

con = False
while con == False:
	print('Simple contact book ')
	print()
	print('1.Add contact')
	print('2.Search contact')
	print('3.Edit  existing contact')
	print('4.Delete contact')
	print('0.Exit')
	User = input()
	if User == '1':
		print()
		print('Add new contact')
		Name = input('Enter contact name: ')
		Phone = input('Enter contact phone: ')
		contact[Name] = Phone
		print()
		print('Saved successfully!')
		print('Name = ' + Name)
		print('Phone = ' + Phone)
		print()
	elif User == '2':
			print()
			print('Search contact .........')
			search = input('Enter contact name : ')
			
			if search  in contact:
				print()
				print('View ...')
				print(search, ':' , contact[search])
				print()
			elif not contact:
				print('Empty contact!')
			else:
				print()
				print('No contact found yet ! ')
				print()
	if User == '0':
		con = True
	if User == '3':
		print()
		Ed = input('Enter the contact name you want to edit: ')
		if Ed in contact:
			Ch = input('Enter the new_number: ')
			contact[Ed] = Ch
			print()
			print('Contact updated ! ')

	if User == '4':
		print()
		del_name = input('Enter the name of the contact: ')
		if del_name in contact:
			confirm = input('You want to delete ? [yes/no]')
			if confirm == 'yes' or confirm == 'Yes':
				del contact[del_name]
				print()
				print('deleted ! ')
			else:
				print()
				print('Canceled ! ')