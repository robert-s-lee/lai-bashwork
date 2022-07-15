A LightingWork that uses subprocess.Popen()

- uses shell=True to allow arbitrary commands to be run
- Drive is use to pull and push data before and after the run
- flag to just pull and push data if a background process is running

# Update PyPi

## Test
python -m pip install twine
python -m pip install setuptools wheel


```
python setup.py sdist bdist_wheel
python -m twine upload dist/*
```
twine upload --repository testpypi dist/*



python -m pip install -i https://test.pypi.org/quicksample/ lai-bashwork

## Prod

# Learn from My Mistakes (LFMM)

## pip install . creates only the dist-info not the package

- The `py_modules=["bashwork"]` in `setup.py` has to match the filename [bashwork.py](lai_bashwork/src/bashwork.py)

- This was very helpful in debugging https://stackoverflow.com/questions/50585246/pip-install-creates-only-the-dist-info-not-the-package

- remove 
```
pip freeze
python -m pip uninstall -y lai-bashwork
```
- look for any error messages
```
pip install -v .
```




