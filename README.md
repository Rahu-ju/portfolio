Its my personal portfolio site, I used Django for some background and dynamic purposes.

Installation :

1. clone the repo

'''bash
git clone 

2. cd to repo and create venv and activate it

'''bash
py -3.13 -m venv venv
venv\scripts\activate

3. Then install package from requirements.txt

''bash
pip install -r requirements.txt

4. Create .env file and inside it create those variable according to .env_example file.

5. To generate django secret key the the command.

'''bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

6. run the server when .env file is ready as same as .env_example

'''bash
python manage.py runserver

yeh hoo.. you are ready..






