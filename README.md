# Automate 30 Bing Searches with Microsoft Edge

## Overview

This Python script automates 30 Bing searches in the Microsoft Edge browser, simulating human-like typing and random intervals between searches. It's tailored for users participating in the Microsoft Rewards program who wish to efficiently complete their daily search quota.

## Features

- **Automated Searches**: Performs 30 Bing searches with randomly selected search terms.
- **Human-like Behavior**: Simulates typing each character with random delays and introduces random wait times between searches to mimic human interaction.
- **Edge Browser Integration**: Utilizes the Microsoft Edge browser for executing searches.
- **Customizable Search Terms**: Easily modify the list of search terms to suit your preferences.

## Prerequisites

- **Python 3.7 or higher**: Ensure Python is installed on your system.
- **Selenium Library**: Install using `pip install selenium`.
- **Microsoft Edge Browser**: Ensure Edge is installed and updated.
- **Edge WebDriver**: Download the version that matches your Edge browser from the [official Microsoft Edge WebDriver page](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/edge-bing-search-automation.git
   cd edge-bing-search-automation
   ```

2. **Install Dependencies**:
   ```bash
   pip install selenium
   ```

3. **Configure Edge WebDriver Path**:
   - Download the appropriate `msedgedriver.exe` for your Edge version.
   - Place the `msedgedriver.exe` in a known directory.
   - Update the `EDGE_DRIVER_PATH` variable in the script with the path to your `msedgedriver.exe`.

## Usage

1. **Run the Script**:
   ```bash
   python main.py
   ```

2. **Monitor the Output**:
   - The script will open the Edge browser and perform 30 searches.
   - Each search term is selected randomly from the predefined list.
   - Typing and search intervals are randomized to emulate human behavior.

## Important Notes

- **Microsoft Rewards Compliance**: While this script simulates human-like behavior, automating searches may violate Microsoft's [Terms of Service](https://www.microsoft.com/en-us/servicesagreement). Use at your own discretion.
- **Customization**: Feel free to modify the `search_terms` list in the script to include topics of your interest.
- **Error Handling**: The script includes basic error handling for WebDriver initialization. Ensure that the Edge WebDriver path is correctly set.

## Disclaimer

This script is intended for educational purposes. Automating interactions with web services can lead to account restrictions or bans. The author is not responsible for any consequences arising from the use of this script.
