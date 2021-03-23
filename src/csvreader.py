import csv
from pprint import pprint

def ClassFactory(class_name, dictionary):
    return type(class_name, (object), dictionary)

class CsvReader:
    data = []

    def __init__(self, filepath):
        with open(filepath) as stuff:
            csv_data = csv.DictReader(stuff, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

    def return_stuff_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects