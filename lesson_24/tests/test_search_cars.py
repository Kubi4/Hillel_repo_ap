import pytest
import requests
import logging

from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger("cars_tests")
logger.setLevel(logging.INFO)

if not logger.handlers:

    file_handler = logging.FileHandler("test_search.log", mode="w", encoding="utf-8")
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()

    logger.info("Авторизація юзера")

    response = session.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )

    assert response.status_code == 200

    access_token = response.json()["access_token"]

    session.headers.update({
        "Authorization": f"Bearer {access_token}"
    })

    logger.info("Авторизація успішна")

    yield session

    session.close()

@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 7),
        ("brand", 4),
        ("price", 10),
        ("year", 2),
        ("engine_volume", 6)
    ]
)
class TestSearchCars:

    def test_search(self, auth_session, sort_by, limit):
        logger.info("===================================")
        logger.info(f"Запуск тесту sort_by={sort_by}, limit={limit}")

        response = auth_session.get(
            f"{BASE_URL}/cars",
            params={
                "sort_by": sort_by,
                "limit": limit
            }
        )

        logger.info(f"Status code: {response.status_code}")

        assert response.status_code == 200

        data = response.json()

        logger.info(f"Кількість машин: {len(data)}")
        logger.info(f"Відповідь API: {data}")

        assert isinstance(data, list)
        assert len(data) <= limit

        logger.info("Тест успішно завершений")