import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# List of sample search terms
search_terms = [
    "how to create virtual environment in python", "python install requests module", "difference between python list and tuple",
    "how to read a file in python", "how to write to a file in python", "python json load and dump",
    "how to parse json in python", "python convert string to datetime", "how to format datetime in python",
    "python list comprehension examples", "how to use lambda function in python", "what is a python decorator",
    "how to use map function in python", "python class inheritance example", "python super() explanation",
    "how to use logging in python", "python logging to file", "python try except block",
    "how to raise exception in python", "python custom exception", "how to import module in python",
    "python relative vs absolute imports", "python __init__.py purpose", "how to use requests to call api in python", "python send post request",
    "python download file from url", "how to scrape website using python", "beautifulsoup find vs find_all", "how to install beautifulsoup4",
    "python selenium tutorial", "how to click button with selenium python", "python webdriver chrome setup", "python multithreading example",
    "python multiprocessing vs multithreading", "python subprocess run example", "how to create gui in python", "python tkinter basic app",
    "python flask tutorial", "python flask vs django", "how to send json response in flask", "python flask render template",
    "how to use jinja2 templates", "python flask rest api example", "python sqlalchemy tutorial", "python sqlite example",
    "python connect to mysql", "python pandas tutorial", "how to read csv in pandas", "pandas dataframe filter rows",
    "pandas groupby example", "matplotlib plot line chart", "python seaborn heatmap", "how to save matplotlib plot",
    "python unit test example", "python pytest tutorial", "how to mock function in pytest", "python assert examples",
    "how to document python code", "python docstring format", "how to publish package to pypi", "python setup.py example",
    "how to use argparse in python", "python command line arguments", "how to handle env variables in python", "python dotenv usage",
    "how to schedule tasks in python", "python apscheduler example", "python datetime now utc", "python timezone conversion",
    "python encrypt string", "python hash password", "how to use hashlib in python", "python os vs sys module",
    "python read env variables", "how to debug in vscode python", "python breakpoints in vscode", "python linter setup",
    "black formatter python", "python typing hints", "python type annotations", "python dataclasses tutorial",
    "python namedtuple vs dataclass", "python path vs os.path", "python pathlib examples", "python zip and unzip file",
    "python tarfile extract example", "python create temporary file", "python create background task", "how to deploy flask app to heroku",
    "python gunicorn setup", "python wsgi vs asgi", "python fastapi tutorial", "fastapi vs flask performance", "how to validate input in fastapi",
    "python pydantic tutorial", "python websocket example", "python send email smtp", "python oauth2 login example",
    "python generate random string", "python uuid usage", "python performance optimization", "python memory profiling tools",
    "how to profile python code", "python project folder structure"
]


# Path to your msedgedriver.exe
EDGE_DRIVER_PATH = r"C:/Users/aarav/OneDrive/Desktop/Edge Rewards/msedgedriver.exe"  # Replace with your actual path

# Set up Edge options (optional)
edge_options = Options()
# edge_options.add_argument("--headless")  # Uncomment to run in headless mode

# Set up the Edge WebDriver service
service = Service(executable_path=EDGE_DRIVER_PATH)

# Initialize Edge WebDriver
from selenium.common.exceptions import WebDriverException

try:
    driver = webdriver.Edge(service=service, options=edge_options)
except WebDriverException as e:
    print("Failed to initialize Edge WebDriver.")
    print("Ensure that 'msedgedriver.exe' is correctly installed and the path is set in EDGE_DRIVER_PATH.")
    print("Download the latest version of msedgedriver from:")
    print("https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/")
    print(f"Error details: {e}")
    exit(1)


# Navigate to Bing
driver.get("https://www.bing.com")

for i in range(30):
    term = random.choice(search_terms)
    
    # Locate the search box and clear any existing text
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()

    # Simulate human-like typing
    for char in term:
        search_box.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))  # Random pause between keystrokes

    search_box.send_keys(Keys.RETURN)
    
    # Wait randomly between searches
    wait_time = random.uniform(5, 10)
    print(f"[{i+1}/30] Searched for: '{term}' | Waiting {wait_time:.1f}s")
    if i != 29:
        time.sleep(wait_time)

# Close the browser after completing the searches
driver.quit()
