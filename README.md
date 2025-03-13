# reCAPTCHA Site Key Detector

A collection of tools for detecting and working with Google reCAPTCHA site keys.

## Features

- Detect reCAPTCHA v2 and v3 site keys on web pages
- Extract site keys from various implementations:
  - Data attributes
  - Script tags
  - Inline JavaScript code
- Generate reCAPTCHA tokens programmatically
- Handle reCAPTCHA validation in automated workflows

## Components

### SitekeyRecaptch.js
JavaScript utility to detect reCAPTCHA site keys on web pages. It can find keys from:
- Elements with data-sitekey attributes
- Script tags with recaptcha/api.js
- Inline grecaptcha.execute calls

### working.py
Python script for generating fresh reCAPTCHA tokens using Selenium WebDriver in headless mode.

### test.py
Test implementation for token generation and API interaction.

## Setup

1. Ensure you have Python installed with the following dependencies:
   - selenium
   - requests

2. For the JavaScript detector:
   - Can be run directly in browser console
   - Or integrated into your web automation workflow

## Usage

### Site Key Detection
Load `SitekeyRecaptch.js` in your browser's console on the target page to detect reCAPTCHA site keys.

### Token Generation
Use `working.py` to generate fresh reCAPTCHA tokens:

1. Replace `YOUR_CHARGEBEE_RECAPTCHA_SITE_KEY` with your actual site key
2. Run the script to generate a token
3. The token can be used for subsequent API calls

## Security Note

- Keep your API keys and tokens secure
- Don't commit sensitive credentials to version control
- Use environment variables for sensitive data

## Contributing

Feel free to submit issues and enhancement requests!