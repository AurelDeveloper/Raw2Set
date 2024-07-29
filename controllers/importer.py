import json
import csv

class Importer:
    def import_json(path):
        # Read JSON file from path and return a list of strings (one string per item)
        with open(path, 'r') as file:
            return json.load(file)
    
    def import_csv(path):
        # Read CSV file from path and return a list strings (one string per row)
        with open(path, 'r') as file:
            reader = csv.reader(file)
            return [row[0] for row in reader]
    
    def import_text(paths):
        # Read text files from paths and return a list of strings (one string per file)
        texts = []
        for path in paths:
            with open(path, 'r') as file:
                texts.append(file.read())
        return texts