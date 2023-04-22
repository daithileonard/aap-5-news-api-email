import requests
from send_email import send_email

topic = "tesla"

api_keu = "e5b2ca1fec2d4cd8968c705086d31652"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-03-22&sortBy=publishedAt&" \
      "apiKey=e5b2ca1fec2d4cd8968c705086d31652&language=en"

# Make request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# access the article titles and descriptions
body = ""
for article in content["articles"][0:10]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" \
               + body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2*"\n"

body = body.encode("utf-8")

send_email(body)