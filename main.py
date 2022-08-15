from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import random

class Game(Widget):
    check = ObjectProperty(None)
    pcchoice = ObjectProperty(None)
    userchoice = ObjectProperty(None)

    def stone(self):
        images = ["img/stone.png", "img/paper.png", "img/scissor.png"]
        self.userchoice.source = "img/stone.png"
        self.pcchoice.source = random.choice(images)

        if self.pcchoice.source == "img/scissor.png":
            self.check.text = "YOU WIN   :)"

        elif self.pcchoice.source == "img/paper.png":
            self.check.text = "YOU LOSE   :("

        else:
            self.check.text = "DRAW!"

    def paper(self):
        images = ["img/stone.png", "img/paper.png", "img/scissor.png"]
        self.userchoice.source = "img/paper.png"
        self.pcchoice.source = random.choice(images)
        # Check who won
        if self.pcchoice.source == "img/scissor.png":
            self.check.text = "YOU LOSE   :("
        elif self.pcchoice.source == "img/stone.png":
            self.check.text = "YOU WIN!   :)"
        else:
            self.check.text = "DRAW!"

    def scissor(self):
        images = ["img/stone.png", "img/paper.png", "img/scissor.png"]
        self.userchoice.source = "img/scissor.png"
        self.pcchoice.source = random.choice(images)

        if self.pcchoice.source == "img/stone.png":
            self.check.text = "YOU LOSE   :("

        elif self.pcchoice.source == "img/paper.png":
            self.check.text = "YOU WIN    :)"

        else:
            self.check.text = "DRAW!"


class MainApp(App):
    def build(self):
        return Game()



if __name__ == '__main__':
    MainApp().run()