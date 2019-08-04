import os

CSRF_ENABLED = True
SECRET_KEY = 'u99XljFl07wtOvL3nDnnn'

try:
    DATABASE_URL = os.environ['DATABASE_URL']
except:
    from sqlalchemy import create_engine

    DATABASE_URL = 'postgresql://ivan:pass2@localhost/test_lib_db'

