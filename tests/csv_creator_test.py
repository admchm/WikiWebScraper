import pytest
import os
from CSVCreator import CSVCreator

class TestCSVCreator:
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
        csv_creator = CSVCreator()
        csv_creator.prepare_file()
        
        assert os.path.exists(csv_creator.path_combined)
        
    def test_access_removed_file(self):
        csv_creator = CSVCreator()
        
        if os.path.exists(csv_creator.path_combined):
            os.remove(csv_creator.path_combined)
        
        assert not os.path.exists(csv_creator.path_combined)

#check if file contains columns
#check if file contains specific game titles
#check if file contains dates for specific titles
#check if file contains regions
#check if file contains links