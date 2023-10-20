import os
import shutil


def remove_docs():
    shutil.rmtree("docs")
    os.remove("mkdocs.yml")


def remove_linting():
    file_names = [".pre-commit-config.yaml", ".flake8"]
    for file_name in file_names:
        os.remove(file_name)
    os.remove(os.path.join(".github", "workflows", "check-linting.yml"))


def main():
    if "{{ cookiecutter.add_docs }}" == "n":
        remove_docs()
    if "{{ cookiecutter.use_linting }}" == "n":
        remove_linting()
    shutil.rmtree("macros")


if __name__ == "__main__":
    main()
