from setuptools import setup, find_packages

with open('README.md') as readme:
    long_description = readme.read().strip()

setup(
    name='crtsearch',
    version='1.0.1',
    description='A Tool written in Python3 for scraping data from crt.sh',
    author='Gaurav Raj',
    url='https://github.com/thehackersbrain/crtsearch',
    author_email='techw803@gmail.com',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['crt.sh', 'subdomains',
              'thehackersbrain', 'gauravraj', 'python3'],
    packages=find_packages(),
    install_requires=['requests', 'rich'],
    entry_points={'console_scripts': ['crtsearch = crtsearch.crtsearch:main']},
    zip_safe=False,
)
