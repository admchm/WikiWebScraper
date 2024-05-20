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

    def prepare_file(self, SNES_games_list):
        self.combine_path_with_file_name()
        
        with open(self.path_combined, mode='w', newline='') as file:
            print(f"Created file at: {self.path_combined}")
            
            self.populate_file_with_data(SNES_games_list, file)
            
            file.close()

    def populate_file_with_data(self, SNES_games_list, file):
        writer = csv.writer(file)
        writer.writerow(["Title", "Platform", "NA release", "PAL release", "JP release", "Wiki URL"])
            
        for item in SNES_games_list:
            data_to_append = [item.title, item.platform, item.release_NA, item.release_PAL, item.release_JP, item.game_url]
            writer.writerow(data_to_append)