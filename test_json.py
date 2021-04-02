import json
import Score_algorithm as SA        
json_master=SA.JSON_EDITOR()
json_master.Algorithm('LacI')

json_path = '/home/brian/ec-552-hw1/input/Eco1C1G1T1.input (copy).json'
f = open(json_path, "r")
data=json.load(f)
f.close()

add_string = '_sensor_model'
name = "".join(('LacI', add_string))
for i in range(17):
    if name in data[i]['name']:
        break

print(data[i]['parameters'])


