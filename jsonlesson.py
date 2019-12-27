jsondata = {
"employee":{ "name":"Bill", "age":30, "city":"New York" }
}


for data in jsondata:
    if jsondata["employee"]["name"] == "John":
        print(jsondata["employee"]["name"])
    else:
        print("Oops, His name ain't John!")