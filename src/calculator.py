def main():
	print('=====================================================')
	print('')
	print('// Easy Calculator //')
	print('')
	print('=====================================================')

	operation_type = ask_operation()
	numbers = ask_numbers()

	calculate(operation_type, numbers)

	print('=====================================================')
	print('')
	print('// Fin du programme //')
	print('')
	print('=====================================================')


def ask_operation():
	valid_operation = {
	'addition': '+', 
	'soustraction': '-', 
	'multiplication': 'x', 
	'division': '/'
	}

	print('=====================================================')
	print('// 1) Choisir l\'opération //')
	print('=====================================================')

	print(f'Les opérations disponibles : {", ".join(valid_operation)}')

	while True:
		operation = input('Quelle opération voulez-vous faire ?\n').strip()

		if (isinstance(operation, str) and operation in valid_operation):
			break


	return valid_operation[operation]

def ask_numbers():
	print('=====================================================')
	print('// 2) Choisir vos nombres //')
	print('=====================================================')
	print('\n Merci de choisir deux nombres')

	while True:
		first_number_input = input('Votre premier nombre ? \n')

		first_number = control_input_number(first_number_input)

		if (first_number is not False):
			break

		print('Merci de saisir un nombre entier \n')

	while True:
		second_number_input = input('Votre deuxième nombre ? \n')

		second_number = control_input_number(second_number_input)

		if (second_number is not False):
			break

		print('Merci de saisir un nombre entier \n')

	print(f'Votre premier nombre : {first_number}')
	print(f'Votre second nombre : {second_number}')

	return (first_number, second_number)


def control_input_number(number_input):
	try:
		number = int(number_input)

		return number
	except ValueError:
		return False

def calculate(operation, numbers):
	print('=====================================================')
	print('// 3) Résultats //')
	print('=====================================================')
	print(f"\nCalcul de l'opération: {numbers[0]} {operation} {numbers[1]}\n")

	if operation == '+':
		result = numbers[0] + numbers[1]
	elif operation == '-':
		result = numbers[0] - numbers[1]
	elif operation == 'x':
		result = numbers[0] * numbers[1]
	elif operation == '/':
		if numbers[1] != 0:
			result = numbers[0] / numbers[1]
		else:
			print("\033[31m Erreur impossible de diviser par 0 arrêt du programme \n")
			return
	else:
		print('\033[31m Erreur innatendue arrêt du programme \n')
		return

	if result is not None:
		print(f"|||| Le resultat de l'opération est : {result} ||||")
	else:
		print('\033[31m Erreur durant l\'opération')
		return

	print('=====================================================')


if __name__ == "__main__":
    main()
