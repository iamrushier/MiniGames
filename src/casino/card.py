import os
from PIL import Image,ImageTk

assets_folder = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "BlackJack/assets/")
).replace("\\", "/")

class Card:
    CARD_HEIGHT=120
    CARD_WIDTH=round(768/1063*CARD_HEIGHT)

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return " of ".join((self.value, self.suit))

    @classmethod
    def get_back_file(cls):
        back_img=Image.open(assets_folder + "/back.png")
        resized=back_img.resize((Card.CARD_WIDTH,Card.CARD_HEIGHT),)
        cls.back = ImageTk.PhotoImage(resized)
        return cls.back

    def get_file(self):
        icon=Image.open(assets_folder + f"/Cards/{self.suit}{self.value}.png")
        resized=icon.resize((Card.CARD_WIDTH,Card.CARD_HEIGHT),)
        self.icon = ImageTk.PhotoImage(resized)
        return self.icon
