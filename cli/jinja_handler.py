from jinja2 import Environment, FileSystemLoader
import glob
import os

def preprocess_templates(templates_directory: str, variables: dict):
    environment = Environment(loader=FileSystemLoader(templates_directory))
    for filename in glob.iglob(templates_directory + '**/**', recursive=True):
        if os.path.isdir(filename):
            continue
        base_filename = os.path.basename(filename)
        template = environment.get_template(base_filename)

        rendered_template = template.render(variables)

        with open(filename, 'w') as file_w:
            file_w.write(rendered_template)

