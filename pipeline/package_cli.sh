cd ../cli
sh zip_templates.sh
poetry install
sh build_cli.sh
gzip -r -N . > ./cli.gz
cd ../pipeline
