A LightingWork that uses subprocess.Popen()

- uses shell=True to allow arbitrary commands to be run
- Drive is use to pull and push data before and after the run
- flag to just pull and push data if a background process is running

# Update PyPi

pip install twine
twine upload dist/*