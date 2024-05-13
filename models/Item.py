
class Item:
    def __init__(self, title, platform = "SNES", release_NA="———", release_PAL="———", release_JP="———", game_url=None):
        self.title = title
        self.platform = platform
        self.release_NA = release_NA
        self.release_PAL = release_PAL
        self.release_JP = release_JP
        self.game_url = game_url

    def show_item_details(self):
        print(f'Title: {self.title}')
        print(f'Platform: {self.platform}')
        print(f'NA release: {self.release_NA}')
        print(f'PAL release: {self.release_PAL}')
        print(f'JP release: {self.release_JP}')
        print(f'Wiki URL = {self.game_url}')
        print('\n')