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
        
        try:
            with open(self.path_combined, mode='w', newline='') as file:
                self.populate_file_with_data(SNES_games_list, file)
                
        except PermissionError:
            print(f"Error: Permission denied when trying to write to {self.path_combined}")
        except IOError as e:
            print(f"IOError: Permission denied when trying to write to {self.path_combined}")
        except Exception as e:
            print(f"An unexpected error occured: {e}")
        finally:
            file.close()
            print(f"Created file at: {self.path_combined}")    

    def populate_file_with_data(self, SNES_games_list, file):
        try:
            writer = csv.writer(file)
            writer.writerow(["Title", "Platform", "NA release", "PAL release", "JP release", "Wiki URL"])
                
            for item in SNES_games_list:
                data_to_append = [item.title, item.platform, item.release_NA, item.release_PAL, item.release_JP, item.game_url]
                writer.writerow(data_to_append)
        except csv.Error as e:
            print(f"CSV error occured: {e}")
        