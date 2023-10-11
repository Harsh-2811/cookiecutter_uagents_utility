# {{ cookiecutter.pypi_plugin_name }}

{{ cookiecutter.short_description }}

# Setup guideline

- Create poetry environment `poetry shell`
- Install the requirements `poetry install`
{% if cookiecutter.use_linting == "y" %}
- Initialize a Git `git init`
- Install pre-commit `pre-commit install`
{% endif %}
- Start utility development under directory named `protocols/`

# Use environment variables

- Create .env file under project root folder
- Add env variables for ex. `TOKEN=`
- Use it overall project : 
    ```
        from decouple import config

        TOKEN = config('TOKEN')
    ```
- If you do not want to use env variables you can remove library `python-decouple` from `requirements.txt`
- Make sure you add .env file in gitignore for security purpose.

# PyPi publish guideline

- Set Github action secret `PYPI_API_TOKEN` in your github project repository.
- Update your main branch with latest code.
- Run command `git tag <package_version>`.
- Publish package by running command `git push --tags`.