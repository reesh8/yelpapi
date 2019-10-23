import requests
import boto3
import datetime
#dynamodb=boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb', region_name='us-east-2', aws_access_key_id="", aws_secret_access_key="")
table=dynamodb.Table('yelp-restaurants')


URL="https://api.yelp.com/v3/businesses/search"
#categories="chinese"
params={"term": "chinese", "location": "Manhattan, New York City", "limit":50, "offset":0}

headers={"Authorization": "Bearer "}

while params["offset"]<1000:

    r = requests.get(url = URL, params = params, headers=headers)

    data=r.json()
    print data["total"]
    #print data
    print len(data["businesses"])

    for each in data["businesses"]:

       
        table.put_item(Item={'restaurant_id':each["id"],"name":each["name"],"rating":str(each["rating"]) if each["rating"] else "N/A" , "insertedAtTimestamp":str(datetime.datetime.now()),"Address":each["location"]["address1"] if each["location"]["address1"] else "N/A" ,"coordinates":str(each["coordinates"]["latitude"])+"  "+str(each["coordinates"]["longitude"]) if each["coordinates"]["latitude"] and each["coordinates"]["longitude"] else "N/A", "number_of_reviews": each["review_count"] if each["review_count"] else "N/A","zip": each["location"]["zip_code"] if each["location"]["zip_code"] else "N/A" })

       
    params["offset"]+=50


#print data["businesses"][1]["name"]
