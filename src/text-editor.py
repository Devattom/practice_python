import os
import sys

def main():
	greetings()
	available_options = get_available_options()
	option = choose_option(available_options)

	if option == 0:
		print("Fermeture du programme bye bye 👋🏻👨‍")
		sys.exit(0)
	if (option == 1):
		create_file()
	elif (option == 2):
		read_file()


def greetings():
	print(
		f"--------------------------------------------------------\n"
		f"\t\t\tTEXT EDITOR\n"
		f"--------------------------------------------------------\n"
		)


def choose_option(available_options):
	print('Ce que vous pouvez faire :')
	for code, option in available_options.items():
		print(f"\t {code} - {option}")
	print('')
	while True:
		chosen_option_input = input("Que voulez-vous faire (saisissez le chiffre lié à l'option) ")
		try:
			chosen_option = int(chosen_option_input)

			if chosen_option in available_options:
				break
			
			print("/!\\ l'option choisie n'existe pas  /!\\ \n")
		except:
			print("/!\\ Merci de saisir le chiffre lié à l'option choisie /!\\ \n")

	print(f"Vous avez choisi l'option : {available_options[chosen_option]} \n")

	return chosen_option

def create_file():
	default_dir = 'text_editor'
	default_path = os.path.expanduser(os.path.join("~", default_dir))
	want_new_dir = input("voulez-vous créer un nouveau dossier ? (Oui / Non)\n")

	dir_name = ''
	if want_new_dir.upper() == "OUI":
		while dir_name == '':
			dir_name = input("\nDonnez un nom à votre dossier : ").strip()

	file_name = ''
	while file_name == '':
		file_name = input("\nDonnez un nom pour votre fichier texte : ").strip()

	file_name = file_name + '.txt'

	dir_path = default_path if dir_name == '' else os.path.join(default_path, dir_name)
	file_path = os.path.join(dir_path, file_name)

	os.makedirs(dir_path, exist_ok=True)

	with open(file_path, 'w') as file:
		pass

	print(f"Fichier créé avec le chemin : {file_path}")

def read_file():
	default_dir = 'text_editor'
	default_path = os.path.expanduser(os.path.join("~", default_dir))
	file_to_find = input("Quel fichier voulez-vous lire ? ")
	editor_files = []
	
	for root, dirs, files in os.walk(default_path):
		for file in files:
			editor_files.append((root, file))
		

	if len(editor_files) == 0:
		print("Il n'existe aucun fichier généré par ce programme actuellement vous devez d'abord en créer un pour le retrouver ensuite.\n")
		return

	founded_files = []
	for file in editor_files:
		if file[1] == file_to_find:
			founded_files.append(os.path.join(file[0], file[1]))


	for file in founded_files:
		print(file)

def get_available_options():
	return {
		0 : 'Quitter le programme',
		1 : 'Créer un fichier',
		2 :'Lire un fichier',
	}

if __name__ == "__main__":
	main()
