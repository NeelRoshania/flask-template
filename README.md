# flask-template

- Flask implementation to OpenAPI specification

### References

### Installation guide

**Module setup**
1. `python -m venv flask/.flask` and `pip3 install --upgrade pip` 
2. Activate enviroment
3. Modify `setup.cfg` and `src`
4. Run configuration test at root, `pytest -v`

**Development - Running the app**
1. `export FLASK_ENV=development`
2. cd `flask`
2. `python -m app

**Development - Running the app**
TBD (`uvicorn app:app --host 0.0.0.0 --port 8000`)

**Jupyter kernel setup**
1. `jupyter kernelspec uninstall .example_env` - remove existing kernels called .example_env
2. `python -m ipykernel install --user --name=.example_env`- install new kernel

### Usage

1. Script implementations here
