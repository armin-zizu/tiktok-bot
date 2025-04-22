import requests
from bs4 import BeautifulSoup

def get_trending_hashtags():
    url = "https://www.tiktok.com/discover"
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")
    hashtags = []

    for tag in soup.find_all("a"):
        href = tag.get("href", "")
        if "/tag/" in href:
            name = href.split("/tag/")[-1]
            if name not in hashtags:
                hashtags.append(f"#{name}")

    return hashtags[:10]