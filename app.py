import requests
import config

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": f"Bearer {config.api_key}"
}
params = {
    "term": "Barber",
    "location": "NYC"
}
response = requests.get(url=url, headers=headers, params=params)
print(response)
# print(response.text)
businesses = response.json()["businesses"]
print(businesses)
names = [business["name"] for business in businesses if business["rating"] > 4.5]
print(names)
# for business in businesses:
#     print(business["name"])
