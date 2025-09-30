# waitlib/core.py
import time
import random

def wait(seconds):
    """Pause the program for a set number of seconds"""
    time.sleep(seconds)

def wait_random(min_sec, max_sec):
    """Pause for a random time between min_sec and max_sec"""
    time.sleep(random.uniform(min_sec, max_sec))
