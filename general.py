import logging
import asyncio
import subprocess
from configparser import ConfigParser

def load_paths_and_urls_from_config(config_file):
    config = ConfigParser()
    config.read(config_file)
    paths = dict(config.items('PATHS'))
    return paths


paths = load_paths_and_urls_from_config('urls_config.ini')
adb_path = paths['adb_path']
ldplayer_path = paths['ldplayer_path']

def automate_open_bot(device_id, url):
    logging.info(f"Launching bot on device {device_id} with URL {url}")
    subprocess.run([adb_path, "-s", device_id, "shell", "am", "start", "-a", "android.intent.action.VIEW", "-d", url])

def run_ldplayer_command(ldplayer_path, command):
    try:
        logging.info(f"Executing command: {ldplayer_path} {command}")
        result = subprocess.run([ldplayer_path] + command.split(), capture_output=True, text=True)
        if result.returncode == 0:
            logging.info(f"Command executed successfully: {result.stdout}")
        else:
            logging.error(f"Error executing command: {result.stderr}")
    except Exception as e:
        logging.error(f"Exception occurred: {e}")

async def start_ld(ldplayer_path, index):
    logging.info(f"Starting LDPlayer instance with index {index}.")
    process = subprocess.Popen([ldplayer_path, "launch", "--index", str(index)],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        logging.error(f"Failed to start LDPlayer instance {index}. Error: {stderr.decode().strip()}")
    else:
        logging.info(f"LDPlayer instance {index} started successfully.")
    await asyncio.sleep(1)

async def close_ld(ldplayer_path, index):
    logging.info(f"Closing LDPlayer instance with index {index}.")
    process = subprocess.Popen([ldplayer_path, "quit", "--index", str(index)],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        logging.error(f"Failed to close LDPlayer instance {index}. Error: {stderr.decode().strip()}")
    else:
        logging.info(f"LDPlayer instance {index} closed successfully.")
    await asyncio.sleep(1)