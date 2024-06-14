#ZXhhbXBsZWJhc2U2NHRvc3RyaW5nCg==
#commonı ımport et
#test fonksıyonlarını calıstır (buraya def ıle yaz)
#sonra gel
import sys
import json
from common import Common

if __name__ == "__main__":
    # Use the JSON file path provided as a command-line argument, or use 'releasekv.json' by default
    if len(sys.argv) > 1:
        json_file_path = sys.argv[1]
    else:
        json_file_path = 'test.json'

    # Decode the base64 string
    from_base64 = "ZXhhbXBsZXNjcmlwdA=="
    decoded_string = Common.fromBase64(from_base64)
    print("Decoded string:", decoded_string)

    # Encode the sentence to base64
    to_base64 = "examplescript"
    encoded_string = Common.toBase64(to_base64)
    print("Encoded string:", encoded_string)
    print("Re-decoded string:", Common.fromBase64(encoded_string))

    # Read the JSON file
    try:
        read_data = Common.readJson(json_file_path)
        print("Read data from JSON file:", read_data)
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {json_file_path}")
        sys.exit(1)

    # Append data to the JSON file
    additional_data = {
        "example_key": "example_value"
    }
    
    # Check if the JSON file contains a dictionary or a list
    if isinstance(read_data, dict):
        read_data.update(additional_data)
    elif isinstance(read_data, list):
        read_data.append(additional_data)
    else:
        print("Unsupported JSON structure")
        sys.exit(1)

    # Write the updated data back to the JSON file
    Common.writeJson(json_file_path, read_data)

    # Read the updated data back from the JSON file
    updated_read_data = Common.readJson(json_file_path)
    print("Updated read data from JSON file:", updated_read_data)
