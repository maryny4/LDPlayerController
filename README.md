# LDPlayer Controller

LDPlayer Controller - это графический интерфейс пользователя (GUI), созданный с использованием Python и библиотеки Tkinter для управления эмулятором Android LDPlayer. Скрипт поддерживает запуск, остановку и автоматизацию LDPlayer, а также взаимодействие с шаблонами на экране эмулятора.

## Функции

- **Запуск LDPlayer**: Ввод индексов эмуляторов и запуск соответствующих экземпляров LDPlayer.
- **Закрытие LDPlayer**: Завершение работы экземпляров LDPlayer по индексам.
- **Команда сортировки окон**: Выполнение команды `sortWnd` для упорядочивания окон LDPlayer.
- **Клик по шаблонам**: Поиск и клик по заданным шаблонам на первом окне LDPlayer.
- **Автоматизация бота**: Автоматизация запуска бота на устройствах, подключенных через ADB.

## Используемые библиотеки и зависимости

- `asyncio`: Для асинхронного выполнения задач.
- `tkinter`: Для создания графического интерфейса.
- `subprocess`: Для выполнения системных команд.
- `cv2` (OpenCV): Для обработки изображений и поиска шаблонов.
- `numpy`: Для работы с массивами изображений.
- `PIL` (Pillow): Для захвата скриншотов.
- `pyautogui`: Для выполнения кликов мыши.
- `concurrent.futures`: Для многопоточного выполнения задач.
- `configparser`: Для чтения конфигурационных файлов.

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/yourusername/ldplayer-controller.git
    cd ldplayer-controller
    ```

2. Установите необходимые зависимости:
    ```sh
    pip install -r requirements.txt
    ```

3. Настройте конфигурационный файл `urls_config.ini`:
    ```ini
    [PATHS]
    adb_path = path/to/adb
    ldplayer_path = path/to/ldplayer

    [URLS]
    bot1 = http://example.com/bot1
    bot2 = http://example.com/bot2
    ```

## Использование

1. Запустите скрипт:
    ```sh
    python ldplayer_controller.py
    ```

2. Введите индексы LDPlayer, которые вы хотите запустить, в поле "LDPlayer Indices (space-separated)" и нажмите "Start LDPlayer".

3. Используйте кнопки "Sort Windows", "Click Syn", и "Quit LDPlayer" для выполнения соответствующих действий.

4. Выберите URL бота из выпадающего списка и нажмите "Automate Bot" для автоматического запуска бота на подключенных устройствах.

## Пример конфигурационного файла `urls_config.ini`

```ini
[PATHS]
adb_path = C:/path/to/adb
ldplayer_path = C:/path/to/ldplayer

[URLS]
bot1 = http://example.com/bot1
bot2 = http://example.com/bot2
