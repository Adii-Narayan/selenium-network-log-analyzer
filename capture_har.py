import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def capture_har():
    driver = setup_browser()
    driver.get("https://exactspace.co/")
    driver.implicitly_wait(10)

    logs = driver.get_log("performance")
    har_data = []
    status_codes = []

    for entry in logs:
        message = json.loads(entry["message"])  # Parse the string as JSON
        har_data.append(message)

        # Extracting status codes from response received entries
        if 'method' in message['message'] and message['message']['method'] == "Network.responseReceived":
            params = message['message']['params']
            if 'response' in params:
                response = params['response']
                if 'status' in response:
                    status_code = response['status']
                    status_codes.append(status_code)

    har_file_path = "network_log.har"
    with open(har_file_path, 'w') as har_file:
        json.dump(har_data, har_file, indent=4)

    print(f".har file saved at {har_file_path}")
    
    # Display all the status codes
    print("Status Codes:")
    for code in set(status_codes):  # Use set to display unique status codes
        print(code)

    driver.quit()

if __name__ == "__main__":
    capture_har()
