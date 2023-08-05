import json

def write_to_json(merged_data, json_file_name):
  with open(json_file_name, "w") as templog:
    json.dump(merged_data, templog, indent=2)