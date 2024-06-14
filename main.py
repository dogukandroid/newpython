#ZXhhbXBsZWJhc2U2NHRvc3RyaW5nCg==
#commonı ımport et
#test fonksıyonlarını calıstır (buraya def ıle yaz)
#sonra gel



#value base64 bı deger orada bır json var nodeInfos/ oradakı nameyı oku bır tane parametre alsın fonksıyonum burada yazan namenın gectıgı her yerı bu parametre ıle degısıtr
import sys
from common import Common

if __name__ == "__main__":

    json_file_path = 'test.json'
    if len(sys.argv) > 1:
        json_file_path = sys.argv[1]

    print(f"Using JSON file: {json_file_path}")

    # Decode the base64 string
    from_base64 = "ZXhhbXBsZXNjcmlwdA=="
    decoded_string = Common.fromBase64(from_base64)
    print("Decoded string:", decoded_string)

    # Encode the sentence to base64
    to_base64 = "examplescript"
    encoded_string = Common.toBase64(to_base64)
    print("Encoded string:", encoded_string)
    print("Re-decoded string:", Common.fromBase64(encoded_string))

    data_to_write = {
        "name": "John Doe",
        "age": 30
    }

    
    if not Common.addDataToJson(json_file_path, data_to_write):
        print("Initial data addition failed")


    read_data = Common.readJson(json_file_path)
    print("Read data from JSON file:", read_data)

    # Additional data to add
    additional_data = {
        "occupation": "Software Engineer"
    }

    # Add more data to the JSON file
    if not Common.addDataToJson(json_file_path, additional_data):
        print("Additional data addition failed")

    # Read the updated data back from the JSON file
    updated_read_data = Common.readJson(json_file_path)
    print("Updated read data from JSON file:", updated_read_data)
