# cookiecutter-uagents-utility

Minimal [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for authoring [uagents](https://github.com/fetchai/uAgents) utility that help
you to write better programs.

![alt text](https://github.com/Harsh-2811/cookiecutter_uagents_utility/blob/main/cookie_cutter.png?raw=true)

## Getting Started

Install [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and generate a new uagents utility project:

```no-highlight
$ pip install cookiecutter
$ cookiecutter https://github.com/fetchai/cookiecutter-uagents-utility
```

Cookiecutter prompts you for information regarding your utility:

```no-highlight
utility_name [My Awesome Utility]: Google Calendar
utility_slug [uagents_google_calendar]:
pypi_plugin_name [uagents-google-calendar]:
protocol_module_name [awesome_module]:
author_name [User A]:
domain_name [example.com]:
email [user-a@example.com]:
version [0.1.0]:
Select open_source_license:
1 - MIT
2 - BSD
3 - GPLv3
4 - Apache Software License 2.0
Choose from 1, 2, 3, 4 [1]: 1
github_username [Github User]: GitUser
github_url [https://github.com/GitUser/uagents-google-calendar]:
add_docs [y]:
use_linting [y]:
```

There you go - you just created a minimal uagents utility:

```no-highlight
uagents_google_calendar/
├── docs
│   └── index.md
├── LICENSE
├── mkdocs.yml
├── pyproject.toml
├── README.md
├── README.rst
├── setup.cfg
├── tests
│   ├── conftest.py
│   └── test_awesome_module.py
└── uagents_google_calendar
    ├── __init__.py
    ├── models.py
    ├── protocols
    │   ├── awesome_module.py
    │   └── __init__.py
    └── wrappers
        ├── awesome_moduleWrapper.py
        └── __init__.py
```
