import speedtest

def test_download_speed() -> float:
    """Проверяет скорость загрузки в Mbps"""
    test = speedtest.Speedtest()
    speed = test.download() / 10**6  # Перевод из бит/с в Мбит/с
    return round(speed, 2)

def test_upload_speed() -> float:
    """Проверяет скорость выгрузки в Mbps"""
    test = speedtest.Speedtest()
    speed = test.upload() / 10**6
    return round(speed, 2)

def test_ping() -> float:
    """Проверяет пинг в мс"""
    test = speedtest.Speedtest()
    test.get_best_server()
    return round(test.results.ping, 2)

def speed_test() -> None:
    """Основная функция для вывода результатов теста скорости интернета"""
    try:
        print("🔍 Запуск теста скорости интернета...")
        down_speed = test_download_speed()
        up_speed = test_upload_speed()
        ping = test_ping()

        print(f"📥 Download Speed: {down_speed} Mbps")
        print(f"📤 Upload Speed: {up_speed} Mbps")
        print(f"📡 Ping: {ping} ms")
    except Exception as e:
        print(f"⚠️ Ошибка при проверке скорости: {e}")

if __name__ == "__main__":
    speed_test()
