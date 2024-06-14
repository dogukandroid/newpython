import os
import json
import base64

class Common:
    def __init__(self, directory='.'):
        self.directory = directory

    def set_directory(self, directory):
        self.directory = directory

    def listDirectory(self):
        result = []
        for entry in os.listdir(self.directory):
            if entry.endswith('.py') or entry.endswith('.sh'):
                result.append(os.path.join(self.directory, entry))
        return result

    @staticmethod
    def toBase64(string):
        encoded_bytes = base64.b64encode(string.encode('utf-8'))
        return encoded_bytes.decode('utf-8')

    @staticmethod
    def fromBase64(base64_string):
        decoded_bytes = base64.b64decode(base64_string)
        return decoded_bytes.decode('utf-8')

    @staticmethod
    def readJson(filepath):
        try:
            with open(filepath, 'r') as file:
                print(f"Reading from file: {filepath}")  # Debug print
                return json.load(file)
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            return None
        except json.JSONDecodeError:
            print(f"Invalid JSON format in file: {filepath}")
            return None

    @staticmethod
    def writeJson(filepath, data):
        try:
            with open(filepath, 'w') as file:
                print(f"Writing to file: {filepath}")  # Debug print
                json.dump(data, file, indent=4)
            return True
        except Exception as e:
            print(f"Error writing JSON file: {e}")
            return False

    @staticmethod
    def addDataToJson(filepath, new_data):
        try:
            existing_data = Common.readJson(filepath)
            if existing_data is None:
                existing_data = {}  # If file does not exist or is empty, initialize with an empty dictionary

            # Check if existing_data is a dictionary or list and update accordingly
            if isinstance(existing_data, dict):
                if isinstance(new_data, dict):
                    existing_data.update(new_data)
                else:
                    print("New data must be a dictionary to update existing dictionary.")
                    return False
            elif isinstance(existing_data, list):
                if isinstance(new_data, list):
                    existing_data.extend(new_data)
                else:
                    existing_data.append(new_data)
            else:
                print(f"Unsupported JSON structure in file: {filepath}")
                return False

            return Common.writeJson(filepath, existing_data)
        except Exception as e:
            print(f"Error adding data to JSON file: {e}")
            return False
