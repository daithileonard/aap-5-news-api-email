import requests

api_keu = "e5b2ca1fec2d4cd8968c705086d31652"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-03-22&sortBy=publishedAt&apiKey=e5b2ca1fec2d4cd8968c705086d31652"

# Make request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])