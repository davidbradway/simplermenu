# Setup

```bash
sudo apt-get install python3-pip -y
pip3 install virtualenv
python3 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
python -m spacy download en
```