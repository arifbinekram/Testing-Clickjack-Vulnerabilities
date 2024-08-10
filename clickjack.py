import requests
from selenium import webdriver
import os

# Prompt user for URL input
URL = input("Enter the URL to test for clickjacking: ").strip()

# Send an HTTP GET request to the specified URL
req = requests.get(URL)

# Check for the presence of the X-Frame-Options header
try:
    xframe = req.headers['x-frame-options']
    print('X-FRAME-OPTIONS:', xframe, 'present, clickjacking not likely possible')
except KeyError:
    print('X-FRAME-OPTIONS missing')
    print('Attempting clickjacking...')

    # Create an HTML page with an iframe embedding the target URL
    html = f'''
    <html>
    <body>
    <iframe src="{URL}" height='600px' width='800px'></iframe>
    </body>
    </html>'''
    html_filename = 'clickjack.html'
    with open(html_filename, 'w+') as f:
        f.write(html)

    # Set up Selenium WebDriver
    driver_path = '/path/to/chromedriver'  # Update this path
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('file://' + os.path.abspath(html_filename))

    # Check if the iframe loads successfully
    try:
        driver.switch_to.frame(0)
        print('Page is likely vulnerable to clickjacking')
    except:
        print('Clickjacking mitigated or frame busting detected')

    # Clean up
    driver.quit()
    os.unlink(html_filename)
