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
        with open(filepath, 'r') as file:
            return json.load(file)

    @staticmethod
    def writeJson(filepath, data):
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)

def TestListDirectory(arg):
    common = Common(arg)
    return common.listDirectory()
