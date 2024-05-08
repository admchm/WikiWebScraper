
class Item:
    def __init__(self, title, platform, release_NA, release_PAL, release_JP):
        self.title = title
        self.platform = platform
        self.release_NA = release_NA
        self.release_PAL = release_PAL
        self.release_JP = release_JP

    def show_item_details(self):
        print(f'Title: {self.title}')
        print(f'Platform: {self.platform}')
        print(f'NA release: {self.title}')
        print(f'PAL release: {self.title}')
        print(f'JP release: {self.title}')