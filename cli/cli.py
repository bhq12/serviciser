import os
from zipfile import ZipFile
import inquirer
from distutils.dir_util import copy_tree
from shutil import rmtree
import sys

def generate_questions():

    all_service_types = os.listdir('./templates')
    questions = [
        inquirer.List(
            'service_select',
            message = "What type of service are you generating?",
            choices=all_service_types,
            carousel=True
        )
    ]
    answers = inquirer.prompt(questions)
    chosen_service_type = answers['service_select']
    print(f"Chosen service: {chosen_service_type}")
    
    all_languages = os.listdir(f'./templates/{chosen_service_type}')
    questions_2 = [
        inquirer.List(
            'language_select',
            message = "What language would you like to use primarily?",
            choices=all_languages,
            carousel=True
        )
    ]
    answers_2 = inquirer.prompt(questions_2)
    chosen_language = answers_2['language_select']
    print(f"Chosen language: {chosen_language}")
    return chosen_service_type, chosen_language

def get_templates_location():
    try:
        working_directory = os.path.dirname(__file__)
    except AttributeError:
        working_directory = os.getcwd()
    return os.path.join(working_directory, 'templates.zip')

def main():
    print("Servicising!")
    service_name = input("Please enter your new service name: ")
    

    with ZipFile(get_templates_location(), 'r') as zip:
        zip.extractall('.')

    chosen_service_type, chosen_language = generate_questions()
    os.mkdir(f'./{service_name}')
    copy_tree(f'./templates/{chosen_service_type}/{chosen_language}', f'./{service_name}')
    rmtree('./templates')
    print("Servicised!")

    



if __name__ == "__main__":
    print('Starting CLI')
    main()
