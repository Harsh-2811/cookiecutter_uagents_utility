"""
test_create_template
--------------------
"""
import os

from tests.utils import build_files_list, check_paths


class TestCreateTemplate:
    def test_create_initial_template(self, cookies, context):
        """Create a new utility via cookiecutter and run its tests."""
        result = cookies.bake(extra_context={**context})

        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == context["utility_slug"]
        assert result.project_path.is_dir()
        paths = build_files_list(str(result.project_path))
        assert paths
        check_paths(paths)

    def test_create_template_without_docs(self, cookies, context):
        """Create a new utility via cookiecutter without docs and linting and run its tests."""

        result = cookies.bake(
            extra_context={**context, "use_linting": "n", "add_docs": "n"}
        )
        assert result.exit_code == 0
        assert result.exception is None
        assert not os.path.exists(os.path.join(result.project_path, "docs"))
        assert not os.path.exists(
            os.path.join(
                result.project_path, ".github", "workflows", "check-linting.yml"
            )
        )
