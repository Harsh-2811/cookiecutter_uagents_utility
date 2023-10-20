import pytest

pytest_plugins = "pytester"


@pytest.fixture
def context():
    return {
        "utility_name": "Whatsapp Utility",
        "utility_slug": "uagents_whatsapp_utility",
        "protocol_module_name": "chat",
    }
