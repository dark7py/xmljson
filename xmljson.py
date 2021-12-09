import xml.etree.ElementTree as ET
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf-8')
root = ET.fromstring(data)
arr = []

for child in root.iter():
    if child.tag == "item":
        arr.append({'pubDate': child.find('pubDate').text, 'title': child.find('title').text})

print(arr)