from setuptools import setup, find_namespace_packages, find_packages

setup(
    name='clean_folder',
    version='1.0',
    description='sort,delete,rename files and folders',
    url='http://github.com/',
    entry_points = {
        'console_scripts':['clean=clean_folder.clean:garbage'],
    },
    author='Andrii Mastykash',
    author_email='mastykash87@gmail.com',
    license='MIT',
    packages=find_packages()
)