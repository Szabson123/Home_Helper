from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from facebook_open import *
from conf_file import *
import os

def check_if_file():
    script_path = os.path.abspath(__file__)
    directory_path = os.path.dirname(script_path)
    config_file_name = "config.txt"
    config_file_path = os.path.join(directory_path, config_file_name)
    return os.path.exists(config_file_path)
    
def main_func():
    if not check_if_file():
        conf_def()
        user_choice = input("Podaj co chcesz otworzyć facebook czy google: ")
        if user_choice == "f":
            open_facebook()
        else:
            print("You choice nothink")
    else:
        print("Siemano")

if __name__ == "__main__":
    main_func()