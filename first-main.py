from requests_html import HTMLSession

session = HTMLSession()

url = "https://medium.com/"

response = session.get(url)

print(response)