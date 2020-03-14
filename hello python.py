def get_web(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

url=input('웹페이지 주소?')
content = get_web(url)
print(content)