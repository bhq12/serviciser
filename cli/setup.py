from setuptools import setup, find_packages

setup(
    name='serviciser',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'inquirer==3.1.4',
    ],
    entry_points={
        'console_scripts': [
            'serviciser = cli:main',
        ],
    }
)
