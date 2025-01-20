import requests
r = requests.get("https://site.financialmodelingprep.com/developer/docs")
print(r.text)
print(r.status_code)