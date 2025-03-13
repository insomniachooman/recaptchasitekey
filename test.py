
import requests

# Define the URL
url = "https://xv-pacs.chargebee.com/api/js/v2/tokens/create_for_card"

# Define the headers
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "Basic live_cupWXU7Rz11h04ocdLKnWzZ1wRGcdYemucn",  # Use environment variables for security
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

# Define the updated payload
payload = {
    "card[number]": "5579100438105270",
    "card[cvv]": "325",
    "card[expiry_month]": "02",
    "card[expiry_year]": "29",
    "card[gateway_account_id]": "gw_AzZZDYU7ciRIk7oMe",
    "_jsapi_key": "live_cupWXU7Rz11h04ocdLKnWzZ1wRGcdYemucn",  # Secure this key
    "recaptchaToken": "P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiRjVWSTdoV1IxKy9hS0VwclFjNUVSWTMxV1g0amJCMWIvQ3FWNnJ0UVp3VWkyU3lrc3ZxR0w2aTU5YkdLbVFuTGF6UzAvVTB2eEJ6ZysxVE1ZTVZsRUhpeHRIeVJJNVpIUWtDUzlVRUhLbHV0bGFlWkdPZ2hmM0VPd3VUQzloY2ZhMnI5R21XekkyaXo0WHVTYjF5SGR4WHNLejhZdCtLRStYaWhYU01FdXMyeklxWUY3T0g2OTl5SjdYdTd5ZW5iS2ZYWkc3U1lKL2lWTlh2OUFqV2FyMm1aS2dhaGxBNG1iNmdUem82QXpPcnBiVjJvRDhSQ0FyNW5tNXg3Q2dZVHkwbjZWNm9oWmJUZU1mWXJyOEQwVHJLS0hGbjRIQXNWZXo2LzU4UVFCMGhSUjNjcGVlRjA4ckNtRzNVZXVtaEQyUXhwa1BBNjV6ZjhFS1VnMy84aFNkb2xJYVRhV0lxQ3poVk1qNHU5VEFvUEkyQWkzU0lyUzl5WlFlaVdvZC96VERQN3YrUHFzZThtOWczQ3ZpZUFsZG5BcDZ0TDhoVnAzSXFWNXNma213NjQxbHFHRVdmeFFLOTkzUjhnQWNySm91QXlBdTREZWRHeVVCY0w5cGtwbDEzblI4UzhMcGtYVVdjQXNWUmhpS2Y3NHlacmgrTFoxd09iWTRTSTRhdkVVblZDelZEN0pMeFZWbDVvZWZnTjJ4cmM3Q0loZ1dkaGFRWWFFdjBxZWFnMHJ3RnRreW1uSlFiRC82VUF3SlN0WXVBMUc5QkxJZS9YdFZrRzU1TUFWVmZVM1U0eTE1R2FhUFJVcm5pVjFBYXJHbmx2SDBEc3p3NElWNmlxbkt2OER5bmRLOTJkQ01PQ2RuVXJpKzZuZ0NwSlBpUDRVUkZwZ0dsU2cvbWtKUzdZVktyVHptYUxaZjJud0N1QWtOMER4V3FVQXJXNVVxWjlObDN1cnh2dEZuVWZpRlR2UWVaSSs5b25yd1RSbm9WeXJJSk9XVEk4cko4ME9GL05FUXVkNmk2ellML2doNllWNVo0RXMvdG83R29vc2NFdjZHd1d2cTRaUnU2MVU0d1gvcUU0VzJZL0ptTDZ0SnVxREtoeitaa3BnSTducFhUS0lIUU1JenVQNCtNU3pML1lNTzcyWkE2dHRYQmJUOGdneEwrQitBbm93NnByZWxGWU03enJFYjgrbmxaOXJoK1BSR090bW5qVk5lcFBYOGYzbWs1Qjc0OUcxNjQwMXZaV1MyTy9QOXFaVUVrWkVSZEtSM2kzZGVjMzVoZldXbnZES2FjTk82STAvclZVZkp3dnBqdHRlUGQ3QTdwV0ZwR1hTZlRaODZZeVZuVWFaYXFvRmprVy9obndHcVNHYmhIMXI3TWtFc0EvSVg5cGllVzVqVGNrSi92M2w1SmsyUFZMZ0dVWDQ4RlZIUHh2c29zc1E3dW1WcktrZDZQc2pic3VEcXVsdVZUSmV4ZmNxME9FeUZEYWdHdjZPWnd4Sk9tcjBJdUZydFVZZHo4NThOb3dRWTZnUjdrWXpvM0FsTXR1VTFSMEZYNnFZU0I5SkQrWjAzN1p0ZHhET0dOVEtnMUpKSHRjaS9Fc2lwdmhaS2xEemplbi9sYm1PMkhpT2RmbFRDczNBSVQ2NjI4U09rRXdPcVIyUmtFVzRpVWUyTzA1WHF5ZzNiRVZZUXg5Z2pGRDdHZEM1dVF6MFVLZGQ0UDlCRUhBWXVXZjU1YUZYMmZ5cWU5ajArYURrQzliZ1hLaXNRPT0iLCJleHAiOjE3NDE4NTYwNjAsInNoYXJkX2lkIjoyNTkxODkzNTksImtyIjoiNDE1MTBkOSIsInBkIjowfQ.ENaVxEiC6A9lfSJH8fYJadFq2X08c8lVbIqFX3PT67o"
}

# Send the POST request
response = requests.post(url, headers=headers, data=payload)

# Print the response
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")