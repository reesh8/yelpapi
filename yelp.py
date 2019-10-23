import requests

URL="https://api.yelp.com/v3/businesses/search"
#categories="chinese"
params={"term": "restaurants", "location": "Manhattan, New York City"}

headers={"Authorization": "Bearer "}
r = requests.get(url = URL, params = params, headers=headers) 
data=r.json()
#print data
print data["total"]

for each in data["businesses"]:
    print each["name"]
    print each["id"] 
#print data["businesses"][1]["name"]
