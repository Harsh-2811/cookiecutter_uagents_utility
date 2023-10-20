utility_slug = "{{ cookiecutter.utility_slug }}"
if hasattr(utility_slug, "isidentifier"):
    assert (
        utility_slug.isidentifier()
    ), "'{}' utility slug is not a valid Python identifier.".format(utility_slug)

assert (
    utility_slug == utility_slug.lower()
), "'{}' utility slug should be all lowercase".format(utility_slug)

assert (
    "\\" not in "{{ cookiecutter.author_name }}"
), "Don't include backslashes in author name."

open_source_license = "{{ cookiecutter.open_source_license }}"

add_docs = "{{ cookiecutter.add_docs }}"
use_linting = "{{ cookiecutter.use_linting }}"

assert add_docs in ["y", "n"], "Value of add_docs should be either y or n"

assert use_linting in ["y", "n"], "Value of use_linting should be either 'y' or 'n'"
