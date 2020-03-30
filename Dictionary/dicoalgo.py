
# creation of dictionaries
dico = {
  "f_name": "Shreeya",
  "l_name": "Bhandari",
  "age: 25"
}

# creation of dictionaries
dico = dict(f_name="Shreeya", l_name="Bhandari", age=25)

#length
print(len(dico))

#Accessing an item
item = dico["f_name"]

#Accessing an item
item = dico.get["f_name"]

#Updating an item
dico["f_name"] = "Shreeya"

#Looping through a dictionary
for x in dico:
  print(x)   #print out the keys
  
 
  
#Looping through a dictionary
for x in dico:
  print(dico[x])   #print out the values
  
#Looping through a dictionary
for x in dico.values():
  print(x)   
  
#Looping through a dictionary
for key, value in dico.items():
  print(key, value)   
  
  
  
# Checking the existence of a key
if "f_name" in dico:
  print("it exists !!!)
else:
   print("It does not T.T")
   
       
#adding items 
dico["city"] = "Cergy"        

        
# Removing Items
dico.pop("city")     # using key names
        
        
# Removing items
dico.popitem() #removing the last added item        
        
# Delecting a dictionary
del dico
        
# Emptying a dictionary
dico.clear()        
        
# copying a dictionary
dico_copy = dico.copy()        

        
# nested dictionary // A dictionary  can contain other dictionaries
group = {
  "person1":{
    "f_name": "Shreeya",
    "l_name": "Bhandari",
    "age": 25
  
  },
  
  "person2":{
    "f_name": "reeya",
    "l_name": "dari",
    "age": 23
  
  },
  
  
  

}
        
        
        
        
