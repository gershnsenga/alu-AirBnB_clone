#!/usr/bin/python3
"""Demo script for BaseModel class."""

from models.base_model import BaseModel

# Create a new instance of BaseModel
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))

print("--")

# Convert the instance to a dictionary
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(
        key, type(my_model_json[key]), my_model_json[key]))

print("--")
