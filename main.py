#ZXhhbXBsZWJhc2U2NHRvc3RyaW5nCg==
#commonı ımport et
#test fonksıyonlarını calıstır (buraya def ıle yaz)
#sonra gel


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

    from_base64 = "ZXhhbXBsZXNjcmlwdA=="
    decoded_string = Common.fromBase64(from_base64)
    print("Decoded string:", decoded_string)

    to_base64 = "examplescript"
    encoded_string = Common.toBase64(to_base64)
    print("Encoded string:", encoded_string)
    print("Re-decoded string:", Common.fromBase64(encoded_string))

    json_data = Common.readJson(json_file_path)
    if json_data is None:
        print("Failed to read JSON data.")
    else:
        print("Original JSON data:", json_data)

        decoded_json_data = Common.decodeBase64InJson(json_data)
        print("Decoded JSON data:", decoded_json_data)

        updated_json_data = Common.updateGateway(decoded_json_data, new_gateway_value)
        print("Updated JSON data:", updated_json_data)

        if not Common.writeJson(json_file_path, updated_json_data):
            print("Failed to write updated JSON data.")

