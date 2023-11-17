import os
from zipfile import ZipFile
import inquirer

TEMPLATES_LOCATION = './templates.zip'

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
def main():
    print("Servicising!")
    service_name = input("Please enter your new service name: ")
    

    print("Servicised!")
    with ZipFile(TEMPLATES_LOCATION, 'r') as zip:
        zip.extractall('.')

    generate_questions()

    


if __name__ == "__main__":
    main()
