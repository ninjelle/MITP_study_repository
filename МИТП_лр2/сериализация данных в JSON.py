import json

def serialize_to_json(data):
    try:
        return json.dumps(data,)
    except TypeError as e:
        print(f"Serialization error: {e}")
        return None

person = {
    "name": "Anna",
    "age": 28,
    "is_student": False,
    "hobbies": ["reading", "traveling", "programming"],
    "address": {
        "city": "Saint-Petersburg",
        "street": "Nevskiy prospect"
    },
    "languages": ["Python", "JavaScript", "SQL"]
}

json_string = serialize_to_json(person)
print("Serialized data:")
print(json_string)
