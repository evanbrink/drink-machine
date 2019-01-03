from guizero import *
import DrinkSerial
import time

## ---------------LOAD IN SETTINGS-------------------
rum         = 1
vodka       = 2
tequila     = 3
gin         = 0
peachS      = 9
tripleS     = 5
cranberry   = 6
pineapple   = 7
orange      = 8
coconut     = 0
gingerB     = 10
clubS       = 11
lime        = 4
tonic       = 12



## ---------------GLOBAL VARIALBES-------------------
window_height = 700
window_width = 1000
image_size = 250

## Calibration constants
cc1 = 1
cc2 = 0.98
cc3 = 1.1
cc4 = 1
cc5 = 1.2
cc6 = 1
cc7 = 0.8
cc9 = 0.95
cc10 = 1.02
cc11 = 1.15
cc12 = 1

## ---------------CUSTOM OBJECTS-------------------------
## Button Object:
## Provide a command for when button is clicked, GUI page,
## and x,y coordinates for location on the page
class DrinkButton:
    def __init__(self, command, img, page, x, y):
        self.button = Picture(page, grid = [x,y], image =img)
        self.button.when_clicked = command

## Pump Object:
## Provide the pump number and calibration constant
class Pump:
    def __init__(self, num, calib):
        self.number = num
        self.calibration = calib

class Recipe:
    def __init__(self, ingredients, proportions, image, addMessage):
        self.ing = ingredients
        self.prop = proportions
        self.image = image
        self.message = addMessage

DarkAndStormy = Recipe(ingredients = [rum, clubS, lime],
                       proportions = [0.36,0.55,0.09], image =
                       "DarkAndStormy.jpg", addMessage = "Enjoy!")

Margarita = Recipe(ingredients = [tequila, lime, tripleS],
                   proportions = [0.57, 0.29, 0.14], image =
                   "MargaritaButton.png", addMessage =
                   "Suggested: Add 1 pump Simple Syrup")

Cosmopolitan = Recipe(ingredients = [vodka, lime, tripleS, cranberry],
                      proportions = [0.67, 0.11, 0.11, 0.11], image =
                      "Cosmopolitan.jpg", addMessage = "Enjoy!")

RumPunch = Recipe(ingredients = [rum, orange, pineapple, cranberry],
                  proportions = [0.31, 0.23, 0.23, 0.23], image =
                  "RumPunch.jpg", addMessage =
                  "Suggested: Add 1 pump Grenadine")

MoscowMule = Recipe(ingredients = [vodka, gingerB, lime],
                    proportions = [0.24, 0.71, 0.06], image =
                    "MoscowMule.jpg", addMessage = "Enjoy!")

TequilaSunrise = Recipe(ingredients = [tequila, orange],
                        proportions = [0.33, 0.67], image =
                        "TequilaSunrise.jpg", addMessage =
                        "Add 2 pumps Grenadine")

VodkaCranberry = Recipe(ingredients = [vodka, cranberry, lime],
                        proportions = [0.15, 0.77, 0.08], image =
                        "VodkaCranberry.jpg", addMessage = "Enjoy!")

SexOnTheBeach = Recipe(ingredients = [vodka, peachS, orange, cranberry],
                       proportions = [0.13, 0.13, 0.37, 0.37], image =
                       "SexOnTheBeach.jpg", addMessage = "Enjoy!")

Mojito = Recipe(ingredients = [rum, lime, clubS], proportions =
                [0.23, 0.15, 0.62], image = "Mojito.jpg", addMessage =
                "Add 2 pumps simple syrup + 2 pumps mint syrup")

## -------------------GUI SETUP---------------------------
app = App(title="MouthSmash", width=window_width,
         height=window_height, layout="grid")

## Pages
page_one = Box(app, grid=[0,0], align="top", layout="grid")
page_one_text = Text(page_one, grid = [0,0], align = "top", text = "PAGE ONE")
page_two = Box(app, grid=[0,0], align="top", layout="grid",
               enabled=False, visible=False)
page_two_text = Text(page_two, grid = [0,0], align = "top", text = "PAGE TWO")
raw_page = Box(app, grid=[0,0], align="top", layout="grid",
               enabled=False, visible=False)
raw_page_text = Text(raw_page, grid = [0,0], align = "top", text = "RAW PAGE")
loading_page = Box(app, grid=[0,0], align="top", layout="grid",
               enabled=False, visible=False)
loading_page_text = Text(loading_page, grid = [0,0], align = "top",
                         text = "LOADING SCREEN")
## Button Box
button_box = Box(app, grid = [0,1], align = "top", layout = "grid")


## Navigation functions
def clear_screen():
    page_one.hide()
    page_one.disable()
    page_two.hide()
    page_two.disable()
    raw_page.hide()
    raw_page.disable()
    button_box.hide()
    button_box.disable()
    loading_page.hide()
    loading_page.disable()

def go_to_page(page):
    clear_screen()
    if page == 1:
        page_one.show()
        page_one.enable()
        button_box.enable()
        button_box.show()
    if page == 2:
        page_two.show()
        page_two.enable()
        button_box.enable()
        button_box.show()
    if page == -1:
        raw_page.show()
        raw_page.enable()
        button_box.enable()
        button_box.show()
    if page == 0:
        loading_page.show()
        loading_page.enable()
    
## Button Box Setup
button_one = PushButton(button_box, command = go_to_page, args = [1],
                        text = "1", grid = [0,0])
button_two = PushButton(button_box, command = go_to_page, args = [2],
                        text = "2", grid = [1,0])
raw_button = PushButton(button_box, command = go_to_page, args = [-1],
                        text = "Ingredients", grid = [2,0])

def cmd01():
    print("BUTTON1 PRESSED!")

def cmd02():
    print("BUTTON2 PRESSED!")

def cmd03():
    print("BUTTON3 PRESSED!")
    print(DarkAndStormy.ing)

def cmd04():
    print("Margarita:")
    print(Margarita.ing)

def cmd05():
    print("Cosmo:")
    print(Cosmopolitan.ing)

def cmd06():
    print("Rum Punch:")
    print(RumPunch.ing)

def cmd07():
    print("Moscow Mule")
    print(MoscowMule.ing)

mojitoButton = DrinkButton(cmd01, "MojitoButton.png", page_one, 0,0)
pinaColadaButton = DrinkButton(cmd02, "Pina-Colada.jpg", page_one, 1,0)
darkAndStormyButton = DrinkButton(cmd03, DarkAndStormy.image, page_one, 2,0)
margaritaButton = DrinkButton(cmd04, Margarita.image, page_two, 0,0)
#cosmopolitanButton = DrinkButton(cmd05, Cosmopolitan.image, page_two, 1,0)
rumPunchButton = DrinkButton(cmd06, RumPunch.image, page_two, 2,0)
moscowMuleButton = DrinkButton(cmd07, MoscowMule.image, page_two, 0,1)

app.display()
