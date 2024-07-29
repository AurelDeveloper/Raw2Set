import csv
import json

class Exporter:
    def export_csv(self, data, path):
        with open(path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([[item] for item in data])

    def export_json(self, data, path):
        with open(path, 'w') as file:
            json.dump(data, file)