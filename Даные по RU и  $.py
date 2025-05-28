import requests
from typing import Optional

def get_exchange_rate(base_currency: str, target_currency: str) -> Optional[float]:
    """
    Получает курс обмена из base_currency в target_currency.

    :param base_currency: Базовая валюта (например, 'USD').
    :param target_currency: Целевая валюта (например, 'RUB').
    :return: Курс обмена или None в случае ошибки.
    """
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        rate = data["rates"].get(target_currency)
        if rate is None:
            print(f"Курс для {target_currency} не найден.")
            return None
        return rate
    except requests.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None

if __name__ == "__main__":
    base = "USD"
    target = "RUB"
    rate = get_exchange_rate(base, target)
    if rate:
        print(f"Курс {base} к {target}: {rate}")
    else:
        print("Не удалось получить курс обмена.")


# Курс USD к RUB: 80.926191
