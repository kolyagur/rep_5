from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# SQLite
url = 'sqlite:///local.db'

# Postgres
#url = f'postgresql://{user}:{passwd}@{host}:{port}/{db}'

engine = create_engine(url, echo=False)

Base=declarative_base()