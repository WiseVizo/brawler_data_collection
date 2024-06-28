import requests
import json

url = "https://api.brawlify.com/v1/brawlers"

response = requests.get(url)
brawler_dict = dict() # for storing final map from id to brawler name 
# Checking if the request was successful
if response.status_code == 200:
    # Parsing the JSON response
    data = response.json()
    brawler_list = data.get("list")
    print(len(brawler_list))
    print(type(brawler_list))
    for brawler in brawler_list:
        brawler_dict[brawler.get("id")] = brawler.get("name")
    
else:
    print(f"Failed to retrieve data: {response.status_code}")


# Save the dictionary to a JSON file
with open('brawler_to_id_map.json', 'w') as json_file:
    json.dump(brawler_dict, json_file, indent=4)