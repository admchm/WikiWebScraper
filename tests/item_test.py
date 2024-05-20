import pytest
from io import StringIO
import sys

from models.Item import Item

class TestItem:
    def test_initialization(self):
        
        item_fake = Item("Chrono Trigger 2")
        assert item_fake.title == "Chrono Trigger 2"
        assert item_fake.platform == "SNES"
        assert item_fake.release_NA == "———"
        assert item_fake.release_PAL == "———"
        assert item_fake.release_JP == "———"
        assert item_fake.game_url is None
        
        item_real = Item("Super Mario World", "SNES", "August 23, 1991", "April 11, 1992", "November 21, 1990", "https://en.wikipedia.org/wiki/Super_Mario_World")
        assert item_real.title == "Super Mario World"
        assert item_real.platform == "SNES"
        assert item_real.release_NA == "August 23, 1991"
        assert item_real.release_PAL == "April 11, 1992"
        assert item_real.release_JP == "November 21, 1990"
        assert item_real.game_url == "https://en.wikipedia.org/wiki/Super_Mario_World"
        
    def test_show_items(self, capsys):
        item_fake = Item("Chrono Trigger 2")
        item_fake.show_item_details()
        captured = capsys.readouterr()
        expected_output = (
            "Title: Chrono Trigger 2\n"
            "Platform: SNES\n"
            "NA release: ———\n"
            "PAL release: ———\n"
            "JP release: ———\n"
            "Wiki URL = None\n\n\n"
        )
        
        assert captured.out == expected_output
        
        #item_real = Item("Super Mario World", "SNES", "August 23, 1991", "April 11, 1992", "November 21, 1990", "https://en.wikipedia.org/wiki/Super_Mario_World")
        
    def test_set_dates(self):
        item = Item("Super Mario World")
        dates = {
            "NA": "August 23, 1991",
            "EU": "April 11, 1992",
            "JP": "November 21, 1990"
        }
        
        item.set_dates(dates)
        
        assert item.release_NA == "August 23, 1991"
        assert item.release_PAL == "April 11, 1992"
        assert item.release_JP == "November 21, 1990"