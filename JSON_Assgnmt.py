# Part1
import json
  
# Opening JSON file
f = open('Employee.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['employee']:
    print(i)
  
# Closing file
f.close()



#Part2
import json
  
# Opening JSON file
f = open('State.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['State']:
    print(i)
  
# Closing file
f.close()