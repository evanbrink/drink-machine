from guizero import *

def cmd01():
    print("BUTTON PRESSED!")

app = App(title = "Button Hack test", width = 600,
          height = 600, layout = "grid")

buttonPage = Box(app, grid = [0,0], align = "top", layout = "grid")
picturePage = Box(app, grid = [0,0], align = "top", layout = "grid")

def cmd01():
    print("BUTTON PRESSED!")
    

#invisibleButton = PushButton(buttonPage, grid = [0,0], align = "top",
#                             text = "YOU CAN'T SEE ME", command = cmd01)
#invisibleButton.height = 20
#invisibleButton.width = 40

picture = Picture(picturePage, grid = [0,0], image = "PinaColadaButton.png")
picture.when_clicked = cmd01

picture2 = Picture(picturePage, grid = [1,0], image = "MojitoButton.png")
picture2.when_clicked = cmd02

app.display()
67 
