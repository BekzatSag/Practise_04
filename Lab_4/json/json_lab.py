import json
with open("sample-data.json", 'r') as file:
    x = json.load(file)
print("Interface Status\n================================================================================\n" + "DN".ljust(51)+"Description".ljust(22)+"Speed".ljust(9)+"MTU\n-------------------------------------------------- --------------------  ------  ------")
for i in x["imdata"]:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    speed = i["l1PhysIf"]["attributes"]["fecMode"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
    print(f"{dn}\t\t\t\t {speed}  {mtu}")