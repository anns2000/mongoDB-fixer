import json
import os
import re

def is_objectid(value):
    # Regular expression to match MongoDB ObjectId
    objectid_pattern = re.compile(r'^[0-9a-fA-F]{24}$')
    return isinstance(value, str) and objectid_pattern.match(value)

def convert_to_objectid(value):
    return {"$oid": value}

def convert_ids_to_objectid(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if is_objectid(value):
                obj[key] = convert_to_objectid(value)
            elif isinstance(value, (list, dict)):
                convert_ids_to_objectid(value)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            if is_objectid(item):
                obj[i] = convert_to_objectid(item)
            elif isinstance(item, (list, dict)):
                convert_ids_to_objectid(item)

# Directory containing JSON files
directory = "path to your Directory"

# Iterate over all JSON files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        file_path = os.path.join(directory, filename)

        # Read the JSON file with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Convert IDs to ObjectId format
        convert_ids_to_objectid(data)

        # Write the modified data back to the file with UTF-8 encoding
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

        print(f"IDs converted to ObjectId format in {filename}.")

print("All JSON files processed.")
