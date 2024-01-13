import unittest
import os
from unittest.mock import patch
from jinja2 import Environment, FileSystemLoader
from cli import jinja_handler


class TestPreprocessTemplates(unittest.TestCase):

    def test_preprocesses_templates_with_variables(self):
        # ARRANGE
        templates_directory = os.path.dirname(os.path.realpath(__file__)) + '/test_templates/'
        variables = {'injected_variable_value': 'wowowowow'}

        test_template_contents = 'this_is_a_variable = "{{ injected_variable_value }}"'
        # Assure file is always in fresh state before test
        with open(templates_directory + '/template.py', 'w') as file:
            file.write(test_template_contents)

        # ACT
        jinja_handler.preprocess_templates(templates_directory, variables)

        # ASSERT
        for filename in os.listdir(templates_directory):
            template_path = os.path.join(templates_directory, filename)
            with open(template_path, 'r') as file:
                rendered_content = file.read()
                self.assertEqual(rendered_content, 'this_is_a_variable = "wowowowow"')
