import requests


res = requests.get("https://oauth.reddit.com/r/python/hot",
                   headers=headers)

print(res.json())  # let's see what we get