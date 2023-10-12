# Helper script for importing csv data into postgresql database

## How to use:
```
pip install -r requirements.txt
python import_csv.py {path_to_csv}
```

## example:
```
pip install -r requirements.txt
python import_csv.py ./restaurantes.csv
```

### Note
Uses the SQLALCHEMY_DATABASE_URI or creates it from POSTGRES_SERVER, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB from the .env
