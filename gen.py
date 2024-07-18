import json


j = './philippine_provinces_cities_municipalities_and_barangays_2019v2.json'
new_j = 'new.json'


old_dict = {}
new_dict = {"arr": []}
dest = {}

with open(j) as json_file:
    old_dict = json.load(json_file)


for region in old_dict:
    for province in old_dict[str(region)]['province_list']:
        for mun in old_dict[str(region)]['province_list'][province]['municipality_list']:
            for barangay in old_dict[str(region)]['province_list'][province]['municipality_list'][mun]['barangay_list']:
                new_dict["arr"].append({
                    "postcode": 'none',
                    "locality": mun,
                    "state": province,
                    "barangay": barangay,
                    "long": 0,
                    "lat": 0,
                    "id": 0,
                    "dc": old_dict[str(region)]['region_name'],
                    "type": "none",
                    "status": ""
                })

                print(barangay)



with open(new_j, "w") as outfile:
    json.dump(new_dict, outfile, indent=2)