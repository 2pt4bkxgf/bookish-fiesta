import requests
url = "http://nouser:f29db2e9-4d94-44fe-a9a2-5c67944048cd@www.duckdns.org/v3/update?hostname=githubtest&myip=1.1.1.1"
r = requests.get(url)
print(r)
