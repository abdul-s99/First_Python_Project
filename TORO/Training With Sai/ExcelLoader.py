import csv

class CSVtoARRAY (object):
    def __init__(self, file_in):
        self.file_in=file_in
        self.array = []
        self.compiler()


    def compiler(self):
        with open(f"{self.file_in}", "r") as array:
            array = list(csv.reader(array))
            self.array=array
        return