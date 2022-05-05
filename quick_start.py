import requests

url = 'http://export.arxiv.org/api/query?search_query=all:machine+AND+all:learning&sortBy=lastUpdatedDate&sortOrder=descending'

r = requests.get(url)
print(f'Status code: {r.status_code}')
print(r.text)
