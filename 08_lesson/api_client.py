import requests

BASE_URL = "https://yougile.com/api-v2"


class ProjectsAPI:
    """Клиент для работы с проектами в YouGile API."""

    def __init__(self, token: str) -> None:
        """Инициализация клиента с токеном авторизации."""
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def create_project(self, name: str) -> requests.Response:
        """Создаёт новый проект с указанным названием."""
        url = f"{BASE_URL}/projects"
        payload = {"title": name}

        print("\n" + "=" * 60)
        print("🔧 ОТЛАДКА: Создание проекта")
        print(f"📍 URL: {url}")
        print(f"📤 Тело запроса: {payload}")
        print(f"📡 Заголовки: {self.headers}")

        try:
            resp = requests.post(url, json=payload, headers=self.headers)
            print(f"✅ Статус ответа: {resp.status_code}")
            print(f"📝 Тело ответа: {resp.text}")
            return resp
        except Exception as e:
            print(f"❌ ОШИБКА: {e}")
            raise

    def get_project(self, project_id: str) -> requests.Response:
        """Получает информацию о проекте по ID."""
        url = f"{BASE_URL}/projects/{project_id}"

        print(f"\n🔍 Получение проекта: {url}")
        try:
            resp = requests.get(url, headers=self.headers)
            print(f"✅ Статус: {resp.status_code}")
            print(f"📝 Ответ: {resp.text}")
            return resp
        except Exception as e:
            print(f"❌ ОШИБКА: {e}")
            raise

    def update_project(self, project_id: str, **kwargs) -> requests.Response:
        """Обновляет проект. Поддерживает передачу 'name' → преобразуется в 'title'."""
        url = f"{BASE_URL}/projects/{project_id}"

        if "name" in kwargs:
            kwargs["title"] = kwargs.pop("name")

        print(f"\n✏️ Обновление проекта: {url}")
        print(f"📤 Данные: {kwargs}")

        try:
            resp = requests.put(url, json=kwargs, headers=self.headers)
            print(f"✅ Статус: {resp.status_code}")
            print(f"📝 Ответ: {resp.text}")
            return resp
        except Exception as e:
            print(f"❌ ОШИБКА: {e}")
            raise
