from jinja2 import Environment, FileSystemLoader


def preprocess_templates(templates_directory: str, variables: dict):
    environment = Environment(loader=FileSystemLoader(templates_directory))
    for filename in glob.iglob(templates_directory + '**/**', recursive=True):
        template = environment.get_template(filename)

        rendered_template = template.render(variables)

        with open(filename, 'w') as file:
            file.write(rendered_template)

