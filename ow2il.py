import subprocess

# Define a list of required libraries
required_libraries = ["pyautogui", "pytesseract", "Pillow", "psutil"]

# Install or update required libraries
for library in required_libraries:
    try:
        subprocess.check_call(["pip", "install", "--upgrade", library])
    except subprocess.CalledProcessError:
        print(f"Failed to install/update {library}. Please install it manually.")
        exit(1)

# Import the required libraries after installation/update
import pyautogui
import time
import pytesseract
from PIL import Image
import psutil

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Screen resolution (1920x1080)
screen_width = 1920
screen_height = 1080

# Define the region where the hero selection screen is located (adjust these values)
x = screen_width * 0.4  # X-coordinate of the top-left corner
y = screen_height * 0.2   # Y-coordinate of the top-left corner
width = screen_width * 0.2  # Width of the region
height = screen_height * 0.6  # Height of the region

# Moira's hero coordinates (sample values, adjust as needed)
moira_x = x + width * 0.5  # X-coordinate of Moira's slot center
moira_y = y + height * 0.2  # Y-coordinate of Moira's slot center

# Function to check if Overwatch 2 is running
def is_overwatch_running():
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] == 'Overwatch.exe':
            return True
    return False

# Delay to allow you to focus on the game
time.sleep(5)

# Check if Overwatch 2 is running
if not is_overwatch_running():
    print("Overwatch 2 is not running. Please start the game.")
else:
    # Function to select Moira using image recognition
    def select_moira():
        try:
            while True:
                # Capture a screenshot of the hero selection area
                screenshot = pyautogui.screenshot(region=(x, y, width, height))  # Define the region
                screenshot.save('hero_selection.png')

                # Use OCR to read the hero names from the screenshot
                hero_names = pytesseract.image_to_string(Image.open('hero_selection.png')).split('\n')

                # Find the position of Moira's name in the list
                if "Moira" in hero_names:
                    moira_position = hero_names.index("Moira")

                    # Calculate the slot number based on Moira's position
                    slot_number = moira_position + 1  # Overwatch slots are 1-indexed

                    # Simulate moving the mouse to Moira's slot and clicking
                    pyautogui.moveTo(moira_x, moira_y, duration=0.5)
                    pyautogui.click()

                    # Optionally, add a delay to ensure Moira is selected
                    time.sleep(1)

                    # Click the "Confirm" button at the bottom
                    confirm_x = x + width * 0.5
                    confirm_y = y + height * 0.9
                    pyautogui.moveTo(confirm_x, confirm_y, duration=0.5)
                    pyautogui.click()

                    # Turn off the script after selecting Moira
                    break
                else:
                    # Add a delay before checking again (adjust as needed)
                    time.sleep(2)

        except Exception as e:
            print(f"An error occurred: {e}")

    # Call the function to select Moira
    select_moira()
