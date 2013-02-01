# Badsanta#
## Prerequisites ##

- python >= 2.5
- pip
- virtualenv/wrapper (optional)

## Installation ##
### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --no-site-packages badsanta-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages --disctribute badsanta-env
cd badsanta-env
source bin/activate
```

### Clone the code ###
Obtain the url to your git repository.

```bash
git clone <URL_TO_GIT_RESPOSITORY> badsanta
```

### Install requirements ###
```bash
cd badsanta
pip install -r requirements.txt
```

### Configure project ###
```bash
cp badsanta/__local_settings.py badsanta/local_settings.py
vi badsanta/local_settings.py
```

### Sync database ###
```bash
python manage.py syncdb
```

### Apply database migrations ###
```bash
python manage.py migrate
```

## Running ##
```bash
python manage.py runserver
```
or 
```
make run
```

Open browser to http://127.0.0.1:8000
