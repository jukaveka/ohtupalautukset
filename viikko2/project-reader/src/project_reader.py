from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        parsed_toml = toml.loads(content)
        parsed_toml_tool = parsed_toml["tool"]
        parsed_toml_poetry = parsed_toml_tool["poetry"]
        parsed_toml_poetry_group = parsed_toml_poetry["group"]
        parsed_toml_poetry_group_dev = parsed_toml_poetry_group["dev"]

        dependency_dict = parsed_toml_poetry["dependencies"]
        dev_dependency_dict = parsed_toml_poetry_group_dev["dependencies"]

        name = parsed_toml_poetry["name"]
        desc = parsed_toml_poetry["description"]
        authors = parsed_toml_poetry["authors"]
        license = parsed_toml_poetry["license"]

        dependencies = []
        for dependency, version in dependency_dict.items():
            dependencies.append(dependency)

        dev_dependencies = []
        for dependency, version in dev_dependency_dict.items():
            dev_dependencies.append(dependency)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, license, authors, dependencies, dev_dependencies)
