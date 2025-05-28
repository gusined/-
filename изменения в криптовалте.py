import requests
import time

# URL для получения данных о тикерах
API_URL = "https://api.bybit.com/v5/market/tickers"

# Параметры
SYMBOL = "BTCUSDT"
PRICE_ALERT_THRESHOLD = 0.01  # Порог изменения цены (1%)

# Переменная для отслеживания последней цены
last_price: float | None = None

def get_price(symbol: str) -> float | None:
    """
    Получает текущую цену для указанного токена.
    
    :param symbol: Символ валютной пары (например, 'BTCUSDT')
    :return: Цена токена или None в случае ошибки
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Проверяем на ошибки в запросе
        data = response.json()
        
        for ticker in data['result']:
            if ticker['symbol'] == symbol:
                return float(ticker['lastPrice'])
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
    return None

def track_price_change() -> None:
    """
    Следит за изменениями цены и выводит уведомления при значительных изменениях.
    """
    global last_price
    while True:
        current_price = get_price(SYMBOL)
        
        if current_price is None:
            print("Не удалось получить цену, повторная попытка...")
            time.sleep(5)
            continue
        
        if last_price:
            price_change = (current_price - last_price) / last_price
            if abs(price_change) >= PRICE_ALERT_THRESHOLD:
                print(f"🚨 **ЦЕНА ИЗМЕНИЛАСЬ!** {SYMBOL} - {current_price} USDT, Изменение: {price_change * 100:.2f}%")
        
        # Обновляем последнюю цену
        last_price = current_price
        
        time.sleep(10)  # Пауза между запросами

if __name__ == "__main__":
    track_price_change()
