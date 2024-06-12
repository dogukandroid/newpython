import os

class Liste:
    def __init__(self, directory='.'):
        self.directory = directory

    def listele(self):
        for entry in os.listdir(self.directory):
            print(entry)

if __name__ == "__main__":
    directory_to_list = '.' 
    Liste(directory_to_list).listele()


