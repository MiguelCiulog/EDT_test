# EDT techical test

How to run locally
1. Install requirements
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Populate database
```
python ./utils/import_csv.py ./utils/restaurantes.csv
```

2. Run the project
```
uvicorn main:app --app-dir ./src/edt/
```
