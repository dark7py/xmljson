from urllib.request import urlopen
from urllib.parse import quote
from json import loads
from itertools import groupby


article = r"https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=" + quote('Бельмондо,_Жан-Поль')
data = loads(urlopen(article).read().decode('utf8'))

revisions = data['query']['pages']['192203']['revisions']
keyfunc = lambda rev: rev['timestamp'][:rev['timestamp'].index('T')]
rev_count_by_date = {}

for key, group in groupby(revisions, keyfunc):
    rev_count_by_date[key] = len(list(group))
max_revs_count = max(rev_count_by_date, key=lambda date: rev_count_by_date[date])

print(max_revs_count) #полученная дата совпадает с датой смерти => можно пользоватся такой метрикой