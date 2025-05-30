dict ={
    "name":"John",
    "age":30,
    "city":"New York",
    "hobbies":["reading", "traveling", "swimming"],
    "is_student": False,
}

print(dict)
print(dict["name"])# Accessing a value by key



# nested dictionary

nested_dict = { 
    "person": {
        "name": "Alice",
        "age": 25,
        "address": {
            "street": "123 Main St",
            "city": "Los Angeles"
        }
    },
    "is_employee": True
}

print(nested_dict)
print(nested_dict["person"]["name"])  # Accessing nested value
print(nested_dict["person"]["address"]["city"])  # Accessing nested value in address