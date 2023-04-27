import os,json

filePath = "author.json"
file = open(filePath,"r")
data = json.load(file)

if data:
    for item in data:
        print(item['id'],item['name'],item['age'])
    # Access the keys and values of each dictionary
        # for key, val in item.items():
        #     print(key ,val,"\n")

else:
    print("No Captured data")