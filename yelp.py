import requests

URL="https://api.yelp.com/v3/businesses/search"
#categories="chinese"
params={"term": "restaurants", "location": "Manhattan, New York City"}

headers={"Authorization": "Bearer o7KiYRSz2gnLm142gBwbN5Qt-_yyUbw7CqCRC4jdUNT97K4574b2HuOZgtkiWNCbW4s8LqUcqLXX27s_fU1_QHGGDUOz4TspT-o0ylvla2N19XnlduFvrkvV-jGSXXYx"}
r = requests.get(url = URL, params = params, headers=headers) 
data=r.json()
#print data
print data["total"]

for each in data["businesses"]:
    print each["name"]
    print each["id"] 
#print data["businesses"][1]["name"]
