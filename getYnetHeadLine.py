import bs4, requests

res = requests.get("http://webcache.googleusercontent.com/search?q=cache:http://ynet.co.il")
try:
    res.raise_for_status()
except Exception as e:
    print("issue with %s" % e)

soup = bs4.BeautifulSoup(res.text, features="html.parser")
topStory = soup.select(".title, .sub-title")

headline = ''

for tag in topStory:
    if tag.get('href') is not None:
        headline += tag.getText()

print(headline)


