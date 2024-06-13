import os
import sys

class Liste:
    def __init__(self, directory='.'):
        self.directory = directory

    def listele(self):
        for entry in os.listdir(self.directory):
            print(entry)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory_to_list = sys.argv[1]
    else:
        print("Usage: python3 script.py <directory_path>")
        sys.exit(1)

    Liste(directory_to_list).listele()


