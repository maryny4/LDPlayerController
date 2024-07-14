import subprocess
import logging
import asyncio
import tkinter as tk
from tkinter import ttk
from configparser import ConfigParser
from concurrent.futures import ThreadPoolExecutor
from general import close_ld, start_ld, run_ldplayer_command, automate_open_bot, load_paths_and_urls_from_config
import time
import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui

logging.basicConfig(level=logging.INFO)

paths = load_paths_and_urls_from_config('urls_config.ini')
adb_path = paths['adb_path']
ldplayer_path = paths['ldplayer_path']


async def start_ld_async(index):
    await start_ld(ldplayer_path, index)


async def close_ld_async(index):
    await close_ld(ldplayer_path, index)


async def run_command_async():
    await asyncio.to_thread(run_ldplayer_command, ldplayer_path, "sortWnd")


async def click_on_templates_in_first_window():
    templates = ["icon/template1.png", "icon/template2.png", "icon/template3.png"]
    # Define the region of the first LDPlayer window (left, top, right, bottom)
    region = (0, 0, 1024, 768)  # Update this region based on the actual window size and position

    for template in templates:
        await click_on_template_in_region(template, region)
        await asyncio.sleep(2)


async def click_on_template_in_region(template_path, region, timeout=60, interval=5):
    start_time = time.time()
    template = cv2.imread(template_path, 0)
    w, h = template.shape[::-1]

    while time.time() - start_time < timeout:
        screen = np.array(ImageGrab.grab(bbox=region))
        gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(gray_screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)

        for pt in zip(*loc[::-1]):
            pyautogui.click(region[0] + pt[0] + w / 2, region[1] + pt[1] + h / 2)
            logging.info(f"Clicked on template at location: {pt} in region: {region}")
            return

        await asyncio.sleep(interval)


async def automate_openbot_async(device_id, url):
    await asyncio.to_thread(automate_open_bot, device_id, url)


def start_ld_callback():
    indices_str = index_entry.get()
    indices = indices_str.split()
    for index in indices:
        if index.isdigit():
            asyncio.run_coroutine_threadsafe(start_ld_async(int(index)), loop)


def close_ld_callback():
    indices_str = index_entry.get()
    indices = indices_str.split()
    for index in indices:
        if index.isdigit():
            asyncio.run_coroutine_threadsafe(close_ld_async(int(index)), loop)


def run_command_callback():
    asyncio.run_coroutine_threadsafe(run_command_async(), loop)


def click_on_templates_callback():
    asyncio.run_coroutine_threadsafe(click_on_templates_in_first_window(), loop)


def load_adb_devices():
    result = subprocess.run([adb_path, "devices"], capture_output=True, text=True)
    devices = []
    for line in result.stdout.splitlines():
        if "\tdevice" in line:
            devices.append(line.split()[0])
    return devices


def load_urls_from_config(config_file):
    config = ConfigParser()
    config.read(config_file)
    return dict(config.items('URLS'))


async def monitor_and_automate_bot():
    while True:
        devices = load_adb_devices()
        indices_str = index_entry.get()
        indices = [index for index in indices_str.split() if index.isdigit()]
        if len(devices) == len(indices):
            logging.info("Number of ADB devices matches the number of LDPlayer instances.")
            url = url_combo.get()
            tasks = [automate_openbot_async(device, url) for device in devices]
            await asyncio.gather(*tasks)
            break
        await asyncio.sleep(2)


def automate_bot_callback():
    asyncio.run_coroutine_threadsafe(monitor_and_automate_bot(), loop)


# Setup Tkinter
root = tk.Tk()
root.title("LDPlayer Controller")

# LDPlayer Index Input
index_label = ttk.Label(root, text="LDPlayer Indices (space-separated):")
index_label.grid(column=0, row=0, padx=10, pady=10)
index_entry = ttk.Entry(root)
index_entry.grid(column=1, row=0, padx=10, pady=10)

# Start Button
start_button = ttk.Button(root, text="Start LDPlayer", command=start_ld_callback)
start_button.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

# Run Command Button
command_button = ttk.Button(root, text="Sort Windows", command=run_command_callback)
command_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Click Templates Button
click_templates_button = ttk.Button(root, text="Click Syn", command=click_on_templates_callback)
click_templates_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Quit Button
quit_button = ttk.Button(root, text="Quit LDPlayer", command=close_ld_callback)
quit_button.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Load URLs from Config
urls = load_urls_from_config('urls_config.ini')
url_label = ttk.Label(root, text="Bot URLs:")
url_label.grid(column=0, row=5, padx=10, pady=10)
url_combo = ttk.Combobox(root, values=list(urls.values()))
url_combo.grid(column=1, row=5, padx=10, pady=10)

# Automate Bot Button
automate_button = ttk.Button(root, text="Automate Bot", command=automate_bot_callback)
automate_button.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

# Asyncio Event Loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
executor = ThreadPoolExecutor()


def run_tk(root):
    try:
        while True:
            root.update()
            loop.run_until_complete(asyncio.sleep(0.1))
    except tk.TclError as e:
        if "application has been destroyed" not in str(e):
            raise


# Run the Tkinter main loop
executor.submit(run_tk, root)
root.mainloop()
