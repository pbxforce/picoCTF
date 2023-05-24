import requests

sites_list = ['http://jupiter.challenges.picoctf.org:9670', 'http://jupiter.challenges.picoctf.org:9670/mycss.css', 'http://jupiter.challenges.picoctf.org:9670/myjs.js']

for url in sites_list:
    response = requests.get(url)
    content = response.text
    lines = content.split('\n')
    for line in lines:
        if "flag:" in line:
            colon_index = line.find(':')
            flag = line[colon_index + 1:].strip()[:-3].replace(" ", "")
            print(flag, end="")
