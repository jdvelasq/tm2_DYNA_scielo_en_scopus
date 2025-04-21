python3 -m venv .venv
source .venv/bin/activate
pip3 install --quiet --upgrade pip
pip3 install --quiet -e /Volumes/GitHub/techminer2
pip3 install --quiet black isort ipykernel
python3 -m spacy download en_core_web_sm