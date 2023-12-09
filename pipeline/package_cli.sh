cd ../cli
sh zip_templates.sh
poetry install
sh build_cli.sh
cd ..
tar -czf cli.tar.gz cli/
cd pipeline
