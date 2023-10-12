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

3. Run the project
```
uvicorn main:app --app-dir ./src/edt/
```

4. Format the project (must have black and isort installed)
```
pip install isort black
isort --profile black . && black .
```

5. The collection can be imported using the restaurants.postman_collection.json. How to import [here](https://apidog.com/blog/how-to-import-export-postman-collection-data/#how-to-import-postman-collections)

