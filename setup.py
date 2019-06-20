import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='c4model',
     version='0.1',
     author="Jostein Solaas",
     author_email="josas@equinor.com",
     description="C4models using python",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/equinor/c4model-python",
     install_requires=['pydot'],
     py_modules=['c4model'],
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
     ],
 )
