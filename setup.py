from setuptools import setup, find_packages

version = None

setup(name='lai_bashwork',
      version='0.1',
      description='Use subprocess.Popen(bash=/bin/bash) to run scripts',
      url='https://github.com/robert-s-lee/lai-bashwork',
      author='Robert S Lee',
      author_email='sangkyulee@gmail.com',
      license='Apache License 2.0',
      packages=find_packages(),
      )