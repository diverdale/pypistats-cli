import httpx
from .config import BASE_URL, API_KEY


def _params(**kwargs: str) -> dict:
    params = {k: v for k, v in kwargs.items() if v}
    if API_KEY:
        params["apikey"] = API_KEY
    return params


def fetch_package(name: str, days: int = 30) -> dict:
    url = f"{BASE_URL}/api/packages/{name}"
    resp = httpx.get(url, params=_params(days=str(days)), timeout=15)
    if resp.status_code == 404:
        raise PackageNotFoundError(name)
    if resp.status_code == 401:
        raise InvalidApiKeyError()
    resp.raise_for_status()
    data = resp.json()
    if not data.get("metadata"):
        raise PackageNotFoundError(name)
    return data


def fetch_health(name: str) -> dict:
    url = f"{BASE_URL}/api/health-score"
    resp = httpx.get(url, params=_params(package=name), timeout=15)
    resp.raise_for_status()
    return resp.json()


def fetch_summary(name: str) -> dict | None:
    """Fetch AI summary. Returns dict with 'summary' key, or None if unavailable."""
    url = f"{BASE_URL}/api/packages/{name}/summary"
    try:
        resp = httpx.get(url, params=_params(), timeout=30)
        if resp.status_code == 403:
            return None  # Free tier
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return None


class PackageNotFoundError(Exception):
    def __init__(self, name: str):
        self.name = name
        super().__init__(f"Package '{name}' not found")


class InvalidApiKeyError(Exception):
    def __init__(self):
        super().__init__("Invalid API key. Check your PYPISTATS_API_KEY.")
