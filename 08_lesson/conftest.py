import os
import pytest

from api_client import ProjectsAPI


@pytest.fixture(scope="session")
def token():
    t = os.getenv("YOUGILE_TOKEN")
    if not t:
        pytest.fail(
            "Не найден токен YOUGILE_TOKEN. "
            "Убедись, что в терминале задана переменная: \$env:YOUGILE_TOKEN=..."
        )
    return t


@pytest.fixture(scope="session")
def api_client(token):
    return ProjectsAPI(token)
