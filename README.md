# flask-template

- Flask implementation to OpenAPI specification

### References

### Installation guide

**Module setup**
1. `python -m venv flask/.dev` and `python -m pip install --upgrade pip` 
2. Modify `setup.cfg` and `src`
3. Activate enviroment and install for either dev or prod
    - dev: `pip install .[dev]`
        - `pip install connexion[flask]`
        - `pip install connexion[uvicorn]`
    - prod: `pip install .[dev]`

**Development - Running the app**
1. `export FLASK_ENV=development`
2. start the server
    - cd `flask_app` then `python -m app` 
3. `pytest -v tests`

**Production - Running the app**
1. `export FLASK_ENV=production`
2. start the server
    - cd `flask_app` then `hypercorn app.__main__:app --bind 0.0.0.0:8000` 
3. `pytest -v tests`

**Jupyter kernel setup**
1. `jupyter kernelspec uninstall .example_env` - remove existing kernels called .example_env
2. `python -m ipykernel install --user --name=.example_env`- install new kernel

### Usage

1. Script implementations here
