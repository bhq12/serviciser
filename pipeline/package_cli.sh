cd ../cli
sh zip_templates.sh
poetry install
sh build_cli.sh
gzip -r -N ./dist/cli > ./cli.gz
cd ../pipeline
