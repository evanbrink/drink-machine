from guizero import *
import serial
import time

#  ---------------LOAD IN SETTINGS-------------------
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
gingerB     = 0
clubS       = 0
lime        = 4
tonic       = 0
coke        = 0
lemonade    = 0

#  ---------------GLOBAL VARIALBES-------------------
window_height = 700
window_width = 1000
image_size = 250

cup_size = 8     # in fl oz
shot_size = 1.5  # in fl oz

# nominal pump speed
pump_speed = 1774  # ms / fl oz

#  Calibration constants
cc1 = 2.711
cc2 = 3.017
cc3 = 2.583
cc4 = 2.861
cc5 = 1.007
cc6 = 1
cc7 = 1
cc8 = 1
cc9 = 1
cc10 = 1
cc11 = 1
cc12 = 1
calib = [cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10, cc11, cc12]

# -----------------SERIAL FUNCITONS-----------------------
# open serial port
#ser = serial.Serial('/dev/cu.usbmodem14201', 9600)  # Mac
ser = serial.Serial('/dev/ttyACM0', 9600)  # Raspberry pi


def ping():
    ser.write(b'\xff\x03\x01\x04\x00')

def pour(pump, time1):
    header = b'\xff'
    length = b'\x06'
    instr  = b'\x02'
    pnum   = bytes([pump])
    ptimeL = bytes([time1%256])
    ptimeH = bytes([int(time1/256)])
    CRC =  ((6+2+pump+time1%256+int(time1/256))%65536
            ).to_bytes(2,byteorder='little')

    packet = header+length+instr+pnum+ptimeL+ptimeH+CRC
    ser.write(packet)
    time.sleep(time1/1000.0)

def pour2(pump, time1, pump2, time2):
    header = b'\xff'
    length = b'\x09'
    instr  = b'\x02'
    pnum1  = bytes([pump])
    time1L = bytes([time1%256])
    time1H = bytes([int(time1/256)])
    pnum2  = bytes([pump2])
    time2L = bytes([time2%256])
    time2H = bytes([int(time2/256)])
    CRC =  ((9+2+pump+time1%256+int(time1/256)+pump2+time2%256+int(time2/256)
            )%65536).to_bytes(2,byteorder='little')

    packet = header+length+instr+pnum1+time1L+time1H+pnum2+time2L+time2H+CRC
    ser.write(packet)
    time.sleep(max([time1, time2])/1000.0)

def pour3(pump, time1, pump2, time2, pump3, time3):
    header = b'\xff'
    length = b'\x0c'
    instr  = b'\x02'
    pnum1  = bytes([pump])
    time1L = bytes([time1%256])
    time1H = bytes([int(time1/256)])
    pnum2  = bytes([pump2])
    time2L = bytes([time2%256])
    time2H = bytes([int(time2/256)])
    pnum3  = bytes([pump3])
    time3L = bytes([time3%256])
    time3H = bytes([int(time3/256)])
    CRC =  ((12+2+pump+time1%256+int(time1/256)+pump2+time2%256+int(time2/256)+
            pump3+time3%256+int(time3/256))%65536).to_bytes(2,byteorder='little')

    packet = (header+length+instr+pnum1+time1L+time1H+pnum2+time2L+time2H+pnum3
    + time3L+time3H+CRC)
    ser.write(packet)
    time.sleep(max([time1, time2, time3])/1000.0)


def pour4(pump, time1, pump2, time2, pump3, time3, pump4, time4):
    header = b'\xff'
    length = b'\x0f'
    instr  = b'\x02'
    pnum1  = bytes([pump])
    time1L = bytes([time1%256])
    time1H = bytes([int(time1/256)])
    pnum2  = bytes([pump2])
    time2L = bytes([time2%256])
    time2H = bytes([int(time2/256)])
    pnum3  = bytes([pump3])
    time3L = bytes([time3%256])
    time3H = bytes([int(time3/256)])
    pnum4  = bytes([pump4])
    time4L = bytes([time4%256])
    time4H = bytes([int(time4/256)])
    CRC =  ((15+2+pump+time1%256+int(time1/256)+pump2+time2%256+int(time2/256)+
            pump3+time3%256+int(time3/256)+pump4+time4%256+int(time4/256)
             )%65536).to_bytes(2,byteorder='little')

    packet = (header+length+instr+pnum1+time1L+time1H+pnum2+time2L+time2H+pnum3
    + time3L+time3H+pnum4+time4L+time4H+CRC)
    ser.write(packet)
    time.sleep(max([time1, time2, time3, time4])/1000.0)

def pour5(pump, time1, pump2, time2, pump3, time3, pump4, time4, pump5, time5):
    header = b'\xff'
    length = b'\x12'
    instr  = b'\x02'
    pnum1  = bytes([pump])
    time1L = bytes([time1%256])
    time1H = bytes([int(time1/256)])
    pnum2  = bytes([pump2])
    time2L = bytes([time2%256])
    time2H = bytes([int(time2/256)])
    pnum3  = bytes([pump3])
    time3L = bytes([time3%256])
    time3H = bytes([int(time3/256)])
    pnum4  = bytes([pump4])
    time4L = bytes([time4%256])
    time4H = bytes([int(time4/256)])
    pnum5  = bytes([pump5])
    time5L = bytes([time5%256])
    time5H = bytes([int(time5/256)])
    CRC =  ((18+2+pump+time1%256+int(time1/256)+pump2+time2%256+int(time2/256)+
            pump3+time3%256+int(time3/256)+pump4+time4%256+int(time4/256)+pump5+
            time5%256+int(time5/256))%65536).to_bytes(2,byteorder='little')

    packet = (header+length+instr+pnum1+time1L+time1H+pnum2+time2L+time2H+pnum3
    + time3L+time3H+pnum4+time4L+time4H+pnum5+time5L+time5H+CRC)
    ser.write(packet)
    time.sleep(max([time1, time2, time3, time4, time5])/1000.0)

def pour6(pump, time1, pump2, time2, pump3, time3, pump4, time4, pump5, time5,
          pump6, time6):
    header = b'\xff'
    length = b'\x15'
    instr  = b'\x02'
    pnum1  = bytes([pump])
    time1L = bytes([time1%256])
    time1H = bytes([int(time1/256)])
    pnum2  = bytes([pump2])
    time2L = bytes([time2%256])
    time2H = bytes([int(time2/256)])
    pnum3  = bytes([pump3])
    time3L = bytes([time3%256])
    time3H = bytes([int(time3/256)])
    pnum4  = bytes([pump4])
    time4L = bytes([time4%256])
    time4H = bytes([int(time4/256)])
    pnum5  = bytes([pump5])
    time5L = bytes([time5%256])
    time5H = bytes([int(time5/256)])
    pnum6  = bytes([pump5])
    time6L = bytes([time5%256])
    time6H = bytes([int(time5/256)])
    CRC =  ((21+2+pump+time1%256+int(time1/256)+pump2+time2%256+int(time2/256)+
            pump3+time3%256+int(time3/256)+pump4+time4%256+int(time4/256)+pump5+
            time5%256+int(time5/256)+pump6+time6%256+int(time6/256))%
            65536).to_bytes(2,byteorder='little')

    packet = (header+length+instr+pnum1+time1L+time1H+pnum2+time2L+time2H+pnum3
    + time3L+time3H+pnum4+time4L+time4H+pnum5+time5L+time5H+pnum6+time6L+time6H+CRC)
    ser.write(packet)
    time.sleep(max([time1, time2, time3, time4, time5, time6])/1000.0)

def back(pump, time1):
    header = b'\xff'
    length = b'\x06'
    instr  = b'\x04'
    pnum   = bytes([pump])
    ptimeL = bytes([time1%256])
    ptimeH = bytes([int(time1/256)])
    CRC =  ((6+4+pump+time1%256+int(time1/256))%65536
            ).to_bytes(2,byteorder='little')

    packet = header+length+instr+pnum+ptimeL+ptimeH+CRC
    ser.write(packet)
    time.sleep(time1/1000.0)

def back2(pump, time1, pump2, time2):
    header = b'\xff'
    length = b'\x09'
    instr  = b'\x04'
    pnum1  = bytes([pump])
    time1L = bytes([time1%256])
    time1H = bytes([int(time1/256)])
    pnum2  = bytes([pump2])
    time2L = bytes([time2%256])
    time2H = bytes([int(time2/256)])
    CRC =  ((9+4+pump+time1%256+int(time1/256)+pump2+time2%256+int(time2/256)
            )%65536).to_bytes(2,byteorder='little')

    packet = header+length+instr+pnum1+time1L+time1H+pnum2+time2L+time2H+CRC
    ser.write(packet)
    time.sleep(max([time1, time2])/1000.0)

def back3(pump, time1, pump2, time2, pump3, time3):
    header = b'\xff'
    length = b'\x0c'
    instr  = b'\x04'
    pnum1  = bytes([pump])
    time1L = bytes([time1%256])
    time1H = bytes([int(time1/256)])
    pnum2  = bytes([pump2])
    time2L = bytes([time2%256])
    time2H = bytes([int(time2/256)])
    pnum3  = bytes([pump3])
    time3L = bytes([time3%256])
    time3H = bytes([int(time3/256)])
    CRC =  ((12+4+pump+time1%256+int(time1/256)+pump2+time2%256+int(time2/256)+
            pump3+time3%256+int(time3/256))%65536).to_bytes(2,byteorder='little')

    packet = (header+length+instr+pnum1+time1L+time1H+pnum2+time2L+time2H+pnum3
    + time3L+time3H+CRC)
    ser.write(packet)
    time.sleep(max([time1, time2, time3])/1000.0)


def back4(pump, time1, pump2, time2, pump3, time3, pump4, time4):
    header = b'\xff'
    length = b'\x0f'
    instr  = b'\x04'
    pnum1  = bytes([pump])
    time1L = bytes([time1%256])
    time1H = bytes([int(time1/256)])
    pnum2  = bytes([pump2])
    time2L = bytes([time2%256])
    time2H = bytes([int(time2/256)])
    pnum3  = bytes([pump3])
    time3L = bytes([time3%256])
    time3H = bytes([int(time3/256)])
    pnum4  = bytes([pump4])
    time4L = bytes([time4%256])
    time4H = bytes([int(time4/256)])
    CRC =  ((15+4+pump+time1%256+int(time1/256)+pump2+time2%256+int(time2/256)+
            pump3+time3%256+int(time3/256)+pump4+time4%256+int(time4/256)
             )%65536).to_bytes(2,byteorder='little')

    packet = (header+length+instr+pnum1+time1L+time1H+pnum2+time2L+time2H+pnum3
    + time3L+time3H+pnum4+time4L+time4H+CRC)
    ser.write(packet)
    time.sleep(max([time1, time2, time3, time4])/1000.0)

#  -------------------GUI SETUP---------------------------
app = App(title="MouthSmash", width=window_width,
         height=window_height, layout="grid", bg="white")

#  Pages
page_one = Box(app, grid=[0, 0], align="top", layout="grid")
page_one_text = Text(page_one, grid = [0,0], align = "top", text = "PAGE ONE")
page_two = Box(app, grid=[0,0], align="top", layout="grid",
               enabled=False, visible=False)
page_two_text = Text(page_two, grid = [0,0], align = "top", text = "PAGE TWO")
page_three = Box(app, grid=[0,0], align="top", layout="grid",
               enabled=False, visible=False)
page_two_three = Text(page_three, grid=[0, 0], align="top", text="PAGE THREE")
loading_page = Box(app, grid=[0,0], align="top", layout="grid",
               enabled=False, visible=False)
loading_page_text = Text(loading_page, grid = [0,0], align = "top",
                         text = "LOADING SCREEN")
loading_image = Picture(loading_page, grid = [0,1], align = "top", image = "MouthSmash.jpg")
# Button Box
button_box = Box(app, grid = [0,1], align = "top", layout = "grid")


# Navigation functions
def clear_screen():
    page_one.hide()
    page_one.disable()
    page_two.hide()
    page_two.disable()
    page_three.hide()
    page_three.disable()
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
    if page == 3:
        page_three.show()
        page_three.enable()
        button_box.enable()
        button_box.show()
    if page == 0:
        loading_page.show()
        loading_page.enable()
    app.update()

# Button Box Setup
button_one = PushButton(button_box, command = go_to_page, args = [1],
                        text = "1", grid = [0,0])
button_two = PushButton(button_box, command = go_to_page, args = [2],
                        text = "2", grid = [1,0])
button_three = PushButton(button_box, command = go_to_page, args = [3],
                        text = "3", grid = [2,0])

## --------------- RECIPE SETUP -------------------------
class Recipe:
    def __init__(self, ingredients, proportions, image, volume,
                 startMessage = None, endMessage = None):
        self.ing = ingredients
        self.prop = proportions
        self.image = image
        self.startMessage = startMessage if startMessage is not None else "Place cup below"
        self.endMessage = endMessage if endMessage is not None else "Enjoy!"
        self.vol = volume

    # define instructions
    def cmd(self):
        info(title="Hit OK when ready", text=self.startMessage)
        go_to_page(0)
        if len(self.ing) == 1:
            pour(self.ing[0], int(self.vol*self.prop[0]*pump_speed*calib[self.ing[0]-1]))
        if len(self.ing) == 2:
            pour2(self.ing[0],int(self.vol*self.prop[0]*pump_speed*calib[self.ing[0]-1]),
            self.ing[1], int(self.vol*self.prop[1]*pump_speed*calib[self.ing[1]-1]))
        if len(self.ing) == 3:
            pour3(self.ing[0],int(self.vol*self.prop[0]*pump_speed*calib[self.ing[0]-1]),
            self.ing[1], int(self.vol*self.prop[1]*pump_speed*calib[self.ing[1]-1]),
            self.ing[2], int(self.vol*self.prop[2]*pump_speed*calib[self.ing[2]-1]))
        if len(self.ing) == 4:
            pour4(self.ing[0],int(self.vol*self.prop[0]*pump_speed*calib[self.ing[0]-1]),
            self.ing[1], int(self.vol*self.prop[1]*pump_speed*calib[self.ing[1]-1]),
            self.ing[2], int(self.vol*self.prop[2]*pump_speed*calib[self.ing[2]-1]),
            self.ing[3], int(self.vol*self.prop[3]*pump_speed*calib[self.ing[3]-1]))
        if len(self.ing) == 5:
            pour5(self.ing[0],int(self.vol*self.prop[0]*pump_speed*calib[self.ing[0]-1]),
            self.ing[1], int(self.vol*self.prop[1]*pump_speed*calib[self.ing[1]-1]),
            self.ing[2], int(self.vol*self.prop[2]*pump_speed*calib[self.ing[2]-1]),
            self.ing[3], int(self.vol*self.prop[3]*pump_speed*calib[self.ing[3]-1]),
            self.ing[4], int(self.vol*self.prop[4]*pump_speed*calib[self.ing[4]-1]))
        if len(self.ing) == 6:
            pour6(self.ing[0],int(self.vol*self.prop[0]*pump_speed*calib[self.ing[0]-1]),
            self.ing[1], int(self.vol*self.prop[1]*pump_speed*calib[self.ing[1]-1]),
            self.ing[2], int(self.vol*self.prop[2]*pump_speed*calib[self.ing[2]-1]),
            self.ing[3], int(self.vol*self.prop[3]*pump_speed*calib[self.ing[3]-1]),
            self.ing[4], int(self.vol*self.prop[4]*pump_speed*calib[self.ing[4]-1]),
            self.ing[5], int(self.vol*self.prop[5]*pump_speed*calib[self.ing[5]-1]))
        go_to_page(1)
        app.update()
        info(title="Finished!", text=self.endMessage)


    # call this function to see if all the ingredients are available
    def available(self):
        avl = True
        for x in self.ing:
            if x == 0:
                avl = False
        return avl

## Button Object:
## Provide a recipe object, a drink volume (in fl oz), GUI page,
## and x,y coordinates for location on the page
class DrinkButton:
    def __init__(self, recipe, page, x, y):
        self.button = Picture(page, grid = [x,y], image =recipe.image)
        self.button.when_clicked = recipe.cmd


DarkAndStormy = Recipe(ingredients = [rum, gingerB, lime],
                       proportions = [0.36,0.55,0.09], image =
                       "DarkAndStormyButton.png", endMessage =
                       "Top off with Ginger Beer\nSuggested: Add a dash of Bitters", volume=cup_size)

Margarita = Recipe(ingredients = [tequila, lime, tripleS],
                   proportions = [0.57, 0.29, 0.14], image =
                   "MargaritaButton.png", startMessage =
                   "Suggested: Add 1 pump Simple Syrup", volume=cup_size)

Cosmopolitan = Recipe(ingredients = [vodka, lime, tripleS, cranberry],
                      proportions = [0.67, 0.11, 0.11, 0.11], image =
                      "CosmopolitanButton.png", volume=cup_size)

RumPunch = Recipe(ingredients = [rum, orange, pineapple, cranberry, lime],
                  proportions = [0.29, 0.22, 0.22, 0.22, 0.05], image =
                  "RumPunchButton.png", startMessage =
                  "Suggested: Add 1 pump Grenadine", volume=cup_size)

MoscowMule = Recipe(ingredients = [vodka, gingerB, lime],
                    proportions = [0.24, 0.71, 0.06], image =
                    "MoscowMuleButton.png", volume=cup_size,
                    endMessage="Top off with Ginger Beer")

TequilaSunrise = Recipe(ingredients = [tequila, orange],
                        proportions = [0.33, 0.67], image =
                        "TequilaSunriseButton.png", startMessage =
                        "Suggested: Add 2 pumps Grenadine", volume=cup_size)

VodkaCranberry = Recipe(ingredients = [vodka, cranberry, lime],
                        proportions = [0.15, 0.77, 0.08], image =
                        "VodkaCranberryButton.png", volume=cup_size)

SexOnTheBeach = Recipe(ingredients = [vodka, peachS, orange, cranberry],
                       proportions = [0.13, 0.13, 0.37, 0.37], image =
                       "SexOnTheBeachButton.png", volume=cup_size)

Mojito = Recipe(ingredients = [rum, lime, clubS], proportions =
                [0.23, 0.15, 0.62], image = "MojitoButton.png", startMessage =
                "Suggested: Add 2 pumps simple syrup + 2 pumps mint syrup",
                endMessage="Top off with club soda", volume=cup_size)

PinaColada = Recipe(ingredients=[rum, coconut, pineapple], proportions =
                    [0.2, 0.4, 0.4], image = "PinaColadaButton.png", endMessage=
                    "Suggested: Add 2 pumps simple syrup", volume=cup_size)

RumAndCoke = Recipe(ingredients=[rum, coke, lime], proportions=[0.28, 0.69, 0.03],
                    image="RumAndCokeButton.png",
                    endMessage="Top off with Coke", volume=cup_size)

VodkaTonic = Recipe(ingredients=[vodka, tonic, lime], proportions=
                    [0.31, 0.62, 0.08], image = "VodkaTonicButton.png",
                    endMessage="Top off with Tonic Water", volume=cup_size)

MouthSmash = Recipe(ingredients=[vodka, lemonade, peachS], proportions=
                    [0.25, 0.65, 0.1], image = "MouthSmashButton.png",
                    volume=cup_size)

# ------ Single ingredients ------

RumShot = Recipe(ingredients=[rum], proportions=[1], image="RumShotButton.png",
                 volume=shot_size)

VodkaShot = Recipe(ingredients=[vodka], proportions=
                    [1], image = "VodkaShotButton.png",
                    volume=shot_size)

TequilaShot = Recipe(ingredients=[tequila], proportions=
                    [1], image = "TequilaShotButton.png",
                    volume=shot_size)

GinShot = Recipe(ingredients=[gin], proportions=
                    [1], image = "GinShotButton.png",
                    volume=shot_size)

PeachSShot = Recipe(ingredients=[peachS], proportions=
                    [1], image = "PeachSShotButton.png",
                    volume=shot_size)

TripleSShot = Recipe(ingredients=[tripleS], proportions=
                    [1], image = "TripleSShotButton.png",
                    volume=shot_size)

CranberryShot = Recipe(ingredients=[cranberry], proportions=
                    [1], image = "CranberryButton.png",
                    volume=shot_size)

PineappleShot = Recipe(ingredients=[pineapple], proportions=
                    [1], image = "PineappleButton.png",
                    volume=shot_size)

OrangeShot = Recipe(ingredients=[orange], proportions=
                    [1], image = "OrangeButton.png",
                    volume=shot_size)

CoconutShot = Recipe(ingredients=[coconut], proportions=
                    [1], image = "CoconutButton.png",
                    volume=shot_size)

LimeShot = Recipe(ingredients=[lime], proportions=
                    [1], image = "LimeButton.png",
                    volume=shot_size)

LemonadeShot = Recipe(ingredients=[lemonade], proportions=
                    [1], image = "LemonadeButton.png",
                    volume=shot_size)

recipeList = [DarkAndStormy, Margarita, Cosmopolitan, RumPunch, MoscowMule,
              TequilaSunrise, VodkaCranberry, SexOnTheBeach, Mojito, PinaColada,
              RumAndCoke, VodkaTonic, MouthSmash, RumShot, VodkaShot,
              TequilaShot, GinShot, PeachSShot, TripleSShot, CranberryShot,
              PineappleShot, OrangeShot, CoconutShot, LimeShot, LemonadeShot]


# -------------------- POPULATE DRINK BUTTONS ------------------------
x = 0
y = 0
pg = 1

buttonList = []
for r in recipeList:
    if r.available():
        if pg == 3:
            buttonList.append(DrinkButton(r, page_three, x, y))
            x = x + 1
            if x == 4:
                x = 0
                y = y + 1
                if y == 2:
                    y = 0
                    pg = pg + 1
        if pg == 2:
            buttonList.append(DrinkButton(r, page_two, x, y))
            x = x + 1
            if x == 4:
                x = 0
                y = y + 1
                if y == 2:
                    y = 0
                    pg = pg + 1
        if pg == 1:
            buttonList.append(DrinkButton(r, page_one, x, y))
            x = x + 1
            if x == 4:
                x = 0
                y = y + 1
                if y == 2:
                    y = 0
                    pg = pg + 1

app.display()
