import pytest
import os
import csv
from src.CSVCreator import CSVCreator
from models.Item import Item

class TestCSVCreator:
    
    #file structure: Title - Platform - NA release - PAL release - JP release - Wiki URL
    
    def test_combine_path_with_file_name(self):
        csv_creator = CSVCreator()
        csv_creator.set_path("~/")
        csv_creator.set_file_name("someFileToTest.csv")
        
        csv_creator.combine_path_with_file_name()
        
        assert csv_creator.path_combined == os.path.expanduser("~/someFileToTest.csv")
    
    def test_combine_path_with_file_name_defaults(self):
        csv_creator = CSVCreator()
        csv_creator.combine_path_with_file_name()
        
        assert csv_creator.path_combined == os.path.expanduser("~/SNES_games_list.csv")
    
    def test_prepare_file(self):
        
        list_of_items = []
        
        item_first = Item("The Addams Family", release_NA="December 01, 1992", release_PAL="———", release_JP="———", game_url="https://en.wikipedia.org/wiki/The_Addams_Family_(video_game)")
        item_second = Item("Asterix & Obelix", release_NA="———", release_PAL="December 01, 1995", release_JP="———", game_url="https://en.wikipedia.org/wiki/Asterix_%26_Obelix_(video_game)")
        item_third = Item("Bill Walsh College Football", release_NA="February 01, 1994", release_PAL="———", release_JP="———", game_url="https://en.wikipedia.org/wiki/Bill_Walsh_College_Football")
        
        list_of_items.append(item_first)
        list_of_items.append(item_second)
        list_of_items.append(item_third)
        
        csv_creator = CSVCreator()
        csv_creator.prepare_file(list_of_items)
        
        assert os.path.exists(csv_creator.path_combined)
        
    def test_access_removed_file(self):
        csv_creator = CSVCreator()
        
        if os.path.exists(csv_creator.path_combined):
            os.remove(csv_creator.path_combined)
        
        assert not os.path.exists(csv_creator.path_combined)
        
    def test_csv_columns(self):
        csv_creator = CSVCreator()
        test_data = [
            {"title": "Super Mario World", "platform": "SNES", "release_NA": "1990", 
             "release_PAL": "1992", "release_JP": "1990", "game_url": "http://example.com"}
        ]
        
        csv_creator.prepare_file(test_data)
        
        with open(csv_creator.path_combined, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader) #getting headers from the first line
            expected_headers = ["Title", "Platform", "NA release", "PAL release", "JP release", "Wiki URL"]
            assert headers == expected_headers

    def test_presence_of_specific_title_in_first_column(self):
        csv_creator = CSVCreator()
        
        list_of_items = []
        
        item_first = Item("The Addams Family", release_NA="December 01, 1992", release_PAL="———", release_JP="———", game_url="https://en.wikipedia.org/wiki/The_Addams_Family_(video_game)")
        item_second = Item("Asterix & Obelix", release_NA="———", release_PAL="December 01, 1995", release_JP="———", game_url="https://en.wikipedia.org/wiki/Asterix_%26_Obelix_(video_game)")
        item_third = Item("Bill Walsh College Football", release_NA="February 01, 1994", release_PAL="———", release_JP="———", game_url="https://en.wikipedia.org/wiki/Bill_Walsh_College_Football")
        
        list_of_items.append(item_first)
        list_of_items.append(item_second)
        list_of_items.append(item_third)
        
        csv_creator = CSVCreator()
        csv_creator.prepare_file(list_of_items)
        
        with open(csv_creator.path_combined, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader) #skipping headers
            found = False
            
            for row in reader:
                if row[0] == "Bill Walsh College Football":
                    found = True
                    break
            assert found, "Bill Walsh College Football not found in the first column"

    def test_presence_of_specific_date_in_column(self):
        csv_creator = CSVCreator()
        
        list_of_items = []
        
        item_first = Item("The Addams Family", release_NA="December 01, 1992", release_PAL="———", release_JP="———", game_url="https://en.wikipedia.org/wiki/The_Addams_Family_(video_game)")
        item_second = Item("Asterix & Obelix", release_NA="———", release_PAL="December 01, 1995", release_JP="———", game_url="https://en.wikipedia.org/wiki/Asterix_%26_Obelix_(video_game)")
        item_third = Item("Bill Walsh College Football", release_NA="February 01, 1994", release_PAL="———", release_JP="———", game_url="https://en.wikipedia.org/wiki/Bill_Walsh_College_Football")
        
        list_of_items.append(item_first)
        list_of_items.append(item_second)
        list_of_items.append(item_third)
        
        csv_creator = CSVCreator()
        csv_creator.prepare_file(list_of_items)
        
        with open(csv_creator.path_combined, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            found = False
            
            for row in reader:
                if row[2] == "February 01, 1994":
                    found = True
                    break
            assert found, "February 01, 1994 not found in the third column"
            
    def test_presence_of_specific_link_in_last_column(self):
        csv_creator = CSVCreator()
        
        list_of_items = []
        
        item_first = Item("The Addams Family", release_NA="December 01, 1992", release_PAL="———", release_JP="———", game_url="https://en.wikipedia.org/wiki/The_Addams_Family_(video_game)")
        item_second = Item("Asterix & Obelix", release_NA="———", release_PAL="December 01, 1995", release_JP="———", game_url="https://en.wikipedia.org/wiki/Asterix_%26_Obelix_(video_game)")
        item_third = Item("Bill Walsh College Football", release_NA="February 01, 1994", release_PAL="———", release_JP="———", game_url="https://en.wikipedia.org/wiki/Bill_Walsh_College_Football")
        
        list_of_items.append(item_first)
        list_of_items.append(item_second)
        list_of_items.append(item_third)
        
        csv_creator = CSVCreator()
        csv_creator.prepare_file(list_of_items)
        
        with open(csv_creator.path_combined, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            found = False
            
            for row in reader:
                if row[5] == "https://en.wikipedia.org/wiki/Asterix_%26_Obelix_(video_game)":
                    found = True
                    break
            assert found, "https://en.wikipedia.org/wiki/Asterix_%26_Obelix_(video_game) not found in the sixth column"
            