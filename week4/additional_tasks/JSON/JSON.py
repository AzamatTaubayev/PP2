import json

with open("C:/Users/Саламат/Desktop/PP2/week4/additional_tasks/JSON/sample_data.json") as f:
    data = json.load(f)

header = "Interface Status/n" + "=" * 80 + "/n"
header += "{:<50}{:<25}{:<8}{}/n".format("DN", "Description", "Speed", "MTU")
header += "-" * 80 + "/n"

body = ""
for interface in data["data"]:
    body += "{:<50}{:<25}{:<8}{}/n".format(interface["DN"], interface["description"], interface["speed"],
                                           interface["mtu"])

print(header + body)