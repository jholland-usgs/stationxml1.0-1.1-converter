import json

from setuptools import setup, find_packages

with open('code.json') as f:
    code_json = json.loads(f.read())[0]

setup(
    name=code_json['name'],
    version=code_json['version'],
    packages=find_packages(exclude=('tests', 'venv')),
    install_requires=['lxml'],
    author=code_json['contact']['name'],
    author_email=code_json['contact']['email'],
    description=code_json['description'],
    keywords=' '.join(code_json['tags']),
    url=code_json['homepageURL'],
    license=code_json['permissions']['licenses'][0]['name'],
    project_urls={
        "Source Code": code_json['homepageURL'],
    }
)
