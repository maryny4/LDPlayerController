# LDPlayer Controller

LDPlayer Controller is a graphical user interface (GUI) built with Python and the Tkinter library to manage the LDPlayer Android emulator. This script supports launching, closing, and automating LDPlayer instances, as well as interacting with on-screen templates.

## Features

- **Start LDPlayer**: Input indices of the emulators and launch the corresponding LDPlayer instances.
- **Close LDPlayer**: Terminate LDPlayer instances by their indices.
- **Sort Windows Command**: Execute the `sortWnd` command to organize LDPlayer windows.
- **Click on Templates**: Search for and click on specified templates within the first LDPlayer window.
- **Automate Bot**: Automate the bot's launch on devices connected via ADB.

## Libraries and Dependencies

- `asyncio`: For asynchronous task execution.
- `tkinter`: For creating the graphical user interface.
- `subprocess`: For executing system commands.
- `cv2` (OpenCV): For image processing and template matching.
- `numpy`: For handling image arrays.
- `PIL` (Pillow): For capturing screenshots.
- `pyautogui`: For performing mouse clicks.
- `concurrent.futures`: For multithreaded task execution.
- `configparser`: For reading configuration files.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ldplayer-controller.git
    cd ldplayer-controller
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Configure the `urls_config.ini` file:
    ```ini
    [PATHS]
    adb_path = path/to/adb
    ldplayer_path = path/to/ldplayer

    [URLS]
    bot1 = http://example.com/bot1
    bot2 = http://example.com/bot2
    ```

## Usage

1. Run the script:
    ```sh
    python ldplayer_controller.py
    ```

2. Enter the indices of the LDPlayer instances you want to start in the "LDPlayer Indices (space-separated)" field and click "Start LDPlayer".

3. Use the "Sort Windows", "Click Syn", and "Quit LDPlayer" buttons to perform the corresponding actions.

4. Select a bot URL from the dropdown menu and click "Automate Bot" to automatically launch the bot on connected devices.

## Example Configuration File `urls_config.ini`

```ini
[PATHS]
adb_path = C:/path/to/adb
ldplayer_path = C:/path/to/ldplayer

[URLS]
bot1 = http://example.com/bot1
bot2 = http://example.com/bot2
