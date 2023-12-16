cd ../cli
echo 'Building installer'
poetry install
poetry run pyinstaller cli.spec
cd ../pipeline
