## This is a test layout for a Drink Machine GUI

from guizero import App, Text, TextBox, PushButton, Slider, Picture, info, Box

## Global variables (not really but python is dumb)
window_height = 650
window_width = 1200
image_size = 250


app = App(title = "Mouth Smash GUI test", width = window_width,
          height = window_height, layout = "grid")

## Pages
main_screen = Box(app, grid = [0,0], align = "top", layout = "grid")                         

page_one = Box(app, grid = [0,0], align = "top", layout = "grid", enabled = False, visible = False)
page_one_text = Text(page_one, grid = [1,0], align = "top", text = "PAGE ONE")

page_two = Box(app, grid = [0,0], align = "top", layout = "grid", enabled = False, visible = False)
page_two_text = Text(page_two, grid = [0,0], align = "top", text = "PAGE TWO")

raw_page = Box(app, grid = [0,0], align = "top", layout = "grid", enabled = False, visible = False)

button_box = Box(app, grid = [0,2], align = "top", layout = "grid", enabled = False, visible = False)
                
## Navigation functions
def go_to_page(page):
    if page == 0:
        page_one.hide()
        page_one.disable()
        page_two.hide()
        page_two.disable()
        raw_page.hide()
        raw_page.disable()
        button_box.hide()
        button_box.disable()

        main_screen.show()
        main_screen.enable()
    if page == 1:
        main_screen.hide()
        main_screen.disable()
        page_two.hide()
        page_two.disable()
        raw_page.hide()
        raw_page.disable()

        page_one.show()
        page_one.enable()
        button_box.enable()
        button_box.show()
        
    if page == 2:
        page_one.hide()
        page_one.disable()
        main_screen.hide()
        main_screen.disable()
        raw_page.hide()
        raw_page.disable()

        page_two.show()
        page_two.enable()
        button_box.enable()
        button_box.show()
    if page == -1:
        page_one.hide()
        page_one.disable()
        page_two.hide()
        page_two.disable()
        main_screen.hide()
        main_screen.disable()
        button_box.hide()
        button_box.disable()

        raw_page.show()
        raw_page.enable()

## Drink functions
def pour_tequila():
    print("1 shot of tequila")

def pour_rum():
    print("1 shot of rum")

def pour_vodka():
    print("1 shot of vodka")

def pour_lemonade():
    print("3oz of lemonade")

def pour_mojito_mixer():
    print("3oz of mojito mixer")

def pour_strawberry_marg_mixer():
    print("3oz of strawberry margarita mixer")

def pour_pina_colada_mixer():
    print("3oz of pina colada mixer")
    
def make_mojito():
    info("Pouring", "Making a Mojito")
    pour_rum()
    pour_mojito_mixer()
    go_to_page(0)

def make_pina_colada():
    info("Pouring", "Making a Pina Colada")
    pour_rum()
    pour_pina_colada_mixer()
    go_to_page(0)

def make_strawberry_marg():
    info("Pouring", "Making a Strawberry Margarita")
    pour_strawberry_marg_mixer()
    pour_tequila()
    go_to_page(0)

def make_shrek_drink():
    info("Pouring", "Making a Shrek Cocktail")
    pour_lemonade()
    pour_vodka()
    go_to_page(0)


    

## Welcome Page Setup
welcome_text = Text(main_screen, grid = [0,0], align = "top", text = "Welcome to Mouth Smash!")
logo = Picture(main_screen, grid = [0,1], align = "top", image = "MouthSmash.jpg")
start_button = PushButton(main_screen, grid = [0,2], align = "top", text = "Get Started",
                          command = go_to_page, args = [1])

## Raw Page Setup
raw_text = Text(raw_page, grid = [0,0], align = "top", text = "INGREDIENTS PAGE")
ingredient_box = Box(raw_page, grid = [0,1], align = "top", layout = "grid")
back_button = PushButton(raw_page, grid = [0,2], align = "top", text = "Go Back",
                         command = go_to_page, args = [1])

tequila_button = PushButton(ingredient_box, grid = [0,0], align = "top", text = "Tequila",
                            command = pour_tequila)

rum_button = PushButton(ingredient_box, grid = [1,0], align = "top", text = "Rum",
                        command = pour_rum)

vodka_button = PushButton(ingredient_box, grid = [2,0], align = "top", text = "Vodka",
                          command = pour_vodka)
vodka_button.height = 10
vodka_button.width  = 30


## Button Box Setup
button_one = PushButton(button_box, command = go_to_page, args = [1],
                        text = "<", grid = [0,0])
button_two = PushButton(button_box, command = go_to_page, args = [2],
                        text = ">", grid = [1,0])
raw_button = PushButton(button_box, command = go_to_page, args = [-1],
                        text = "Ingredients", grid = [2,0])

## Drink Buttons
mojito_box = Box(page_one, grid = [0,1], align = "top", layout = "grid")
mojito_image = Picture(mojito_box, grid = [0,0], align = "top", image = "mojito.jpeg")
mojito_image.height = image_size
mojito_image.width = image_size
mojito_button = PushButton(mojito_box, grid = [0,1], text = "Mojito", command = make_mojito)

marg_box = Box(page_one, grid = [1,1], align = "top", layout = "grid")
marg_image = Picture(marg_box, grid = [0,0], align = "top", image = "strawberryMarg.jpg")
marg_image.height = image_size
marg_image.width = image_size
strawberry_marg_button = PushButton(marg_box, grid = [0,1], command = make_strawberry_marg,
                                    text = "Strawberry Margarita")

pina_colada_box = Box(page_two, grid = [0,1], align = "top", layout = "grid")
pina_colada_image = Picture(pina_colada_box, grid = [0,0], align = "top", image = "Pina-Colada.jpg")
pina_colada_image.height = image_size
pina_colada_image.width = image_size
pina_colada_button = PushButton(pina_colada_box, grid = [0,1], text = "Pina Colada",
                                command = make_pina_colada)

shrek_box = Box(page_two, grid = [1,1], align = "top", layout = "grid")
shrek_image = Picture(shrek_box, grid = [0,0], image = "shrekDrink.jpg", align = "top")
shrek_image.height = image_size
shrek_image.width  = image_size
shrek_button = PushButton(shrek_box, grid = [0,1], text = "Shrek Cocktail",
                          command = make_shrek_drink)


## Page Switch Buttons
def goto_p1():
    page_one.enable()
    page_one.show()
    page_two.hide()
    page_two.disable()

def goto_p2():
    page_two.show()
    page_two.enable()
    page_one.disable()
    page_one.hide()


app.display()
