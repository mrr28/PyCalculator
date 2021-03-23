import csv
from pprint import pprint

addition = "src/Unit Test Addition.csv"
subtraction = "src/Unit Test Subtraction.csv"
multiplication = "src/Unit Test Multiplication.csv"
division = "src/Unit Test Division.csv"
squared = "src/Unit Test Square.csv"
squareroot = "src/Unit Test Square Root.csv"

files = addition , subtraction, multiplication, division, squared, squareroot

def ClassFactory(class_name, dictionary):
    return type(class_name, (object), dictionary)

class CsvReader:
    data = []

    def __init__(self, filepath):
        for file in files:
            with open(file) as stuff:
                csv_data = csv.DictReader(stuff, delimiter=',')
            for row in csv_data:
                self.data.append(row)
                x = row[0]
                y = row[1]
        pass

    def return_stuff_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects