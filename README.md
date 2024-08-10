
# Testing Clickjack Vulnerabilities

This project contains a Python script designed to test websites for clickjacking vulnerabilities. The script checks if the target site has appropriate security headers and attempts to simulate a clickjacking attack using Selenium.

## Features

- **X-Frame-Options Check:** Verifies the presence of the `X-Frame-Options` header to determine if the site is protected against clickjacking.
- **Simulated Clickjacking Attack:** Uses Selenium to load the target URL in an iframe and checks if the page is vulnerable.
- **Frame Busting Detection:** Detects JavaScript-based frame busting techniques to further assess clickjacking defenses.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/arifbinekram/Testing-Clickjack-Vulnerabilities.git
   cd Testing-Clickjack-Vulnerabilities
   ```

2. **Install the required Python packages:**

   The script requires Python 3, `requests`, and `selenium` libraries. Install the required packages using pip:

   ```bash
   pip install requests selenium
   ```

3. **Download WebDriver:**

   - For Chrome, download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Ensure the WebDriver executable is in your system's PATH or specify its location in the script.

## Usage

1. **Run the script:**

   Execute the script using Python 3:

   ```bash
   python3 clickjack.py
   ```

2. **Enter the URL when prompted:**

   The script will ask for a URL input. Provide the URL you want to test for clickjacking vulnerabilities.

## Output

- **X-Frame-Options Presence:** Indicates whether the `X-Frame-Options` header is set and its configuration.
- **Clickjacking Vulnerability:** Determines if the page is vulnerable based on the iframe load test.
- **Frame Busting Detection:** Reports if JavaScript-based frame busting is detected.

## Contributions

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to discuss potential improvements or features.

## Disclaimer

This tool is intended for educational and authorized testing purposes only. Ensure you have permission to test any system with this script, as unauthorized testing can be illegal and unethical.

## Acknowledgments

- Inspired by the need for assessing web applications' vulnerability to clickjacking attacks.
- Thanks to the open-source community for providing tools and libraries that make projects like this possible.

---

For more information, visit the [project repository](https://github.com/arifbinekram/Testing-Clickjack-Vulnerabilities).
```

This `README.md` file provides a comprehensive overview of the project, including its purpose, features, installation instructions, usage guidelines, and important notes about responsible use and contributions. Adjust any sections as needed to fit additional project specifics or updates.
