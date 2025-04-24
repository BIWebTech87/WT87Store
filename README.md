# WT87Store

WebTech87 Store online

Create virtualenv

    python(3) -m venv venv

Activate virtualenv

    source venv/bin/activate - Linux
    venv\Scripts\activate - Windows

Install requirement. requirements.txt is in server folder.

    pip install -r requirements.txt

## Backend

### .env

File witch stores all environment variables. To get a variable, use library dotenv.
An example of how to get a variable from .env:

    from dotenv import load_dotenv
    
    load_dotenv()  

    var = os.getenv('VAR_NAME')

### DB-PostgreSQL

Connection DB-PostgreSQL.
Insert into settings.py:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'wt87',
            'USER': 'postgres',
            'PASSWORD': '<PASSWORD>',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

