Its my personal portfolio site, I used Django for some background and dynamic purposes.

Installation :

#clone the repo

```git clone https://github.com/Rahu-ju/portfolio.git```

#cd to repo and create venv and activate it

```py -3.13 -m venv venv```

```venv\scripts\activate```

#Then install package from requirements.txt

```pip install -r requirements.txt```

#Create .env file and inside it create those variable according to .env_example file.

#To generate django secret key run the command.

```python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key()'  ```

#Run the server when .env file is ready as same as .env_example

```python manage.py runserver```

yeh hoo.. you are ready..






