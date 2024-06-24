import sys
from common import Common

if __name__ == "__main__":
    json_file_path = 'test.json'
    new_gateway_value = 'new_gateway_value'

    if len(sys.argv) > 1:
        json_file_path = sys.argv[1]
    if len(sys.argv) > 2:
        new_gateway_value = sys.argv[2]

    print(f"Using JSON file: {json_file_path}")
    print(f"New gateway value: {new_gateway_value}")

    json_data = Common.readJson(json_file_path)
    if json_data is None:
        print("Failed to read JSON data.")
    else:
        print("Original JSON data:", json_data)

        processed_data = Common.processJsonWithBase64(json_data, new_gateway_value)
        print("Updated JSON data:", processed_data)

        if not Common.writeJson(json_file_path, processed_data):
            print("Failed to write updated JSON data.")
        else:
            print("JSON data successfully updated and saved.")

