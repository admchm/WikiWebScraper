import csv
import os

class CSVCreator:
    def __init__(self, path = "~/", file_name = "SNES_games_list.csv", path_combined = ""):
        self.path = path
        self.file_name = file_name
        self.path_combined = path_combined
    
    def set_path(self, path):
        self.path = path
        
    def set_file_name(self, filename):
        self.file_name = filename
        
    def combine_path_with_file_name(self):
        self.path_combined = os.path.expanduser(f"{self.path + self.file_name}")

    def prepare_file(self):
        self.combine_path_with_file_name()
        
        data = [
            ["Imię", "Nazwisko", "Wiek"],
            ["Jan", "Kowalski", 28],
            ["Anna", "Nowak", 22],
            ["Piotr", "Wiśniewski", 35]
        ]
        with open(self.path_combined, mode='w', newline='') as file:
            print(f"combined path: {self.path_combined}")
            writer = csv.writer(file)
            writer.writerows(data)
    
    def propagate_file_with_data():
        pass