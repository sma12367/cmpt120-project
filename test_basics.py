import cmpt120image
from main import init_env, play_sound

def test_play_sound(env):
    play_sound("apples", env)
    input("Press enter to continue after sound has played. ")

def test_get_image():
    cmpt120image.get_image("images/apples.png")

def test_save_image():
    my_image = cmpt120image.get_image("images/apples.png")
    cmpt120image.save_image(my_image, "copy_of_apples.png")

def test_show_image():
    my_image = cmpt120image.get_image("images/apples.png")
    cmpt120image.show_image(my_image)
    input("Press enter when done viewing image")

def test_get_black_image():
    b = cmpt120image.get_black_image(100, 100)
    cmpt120image.show_image(b)
    input("Press enter when done viewing image")

def test_get_white_image():
    w = cmpt120image.get_white_image(100, 100)
    cmpt120image.show_image(w)
    input("Press enter when done viewing image")

ENV = init_env()


# ===
# CODE TO TEST SOUNDS 
# ===
# Uncomment the below code to make sure you can play a sound!
# If this doesn't run, try to debug your error message or let the instructors know!

# test_play_sound(ENV)


# ===
# CODE TO TEST IMAGES
# ===
# screen = cmpt120image.init()

# Uncomment the below code to make sure you can get an image

test_get_image()
test_save_image()
test_show_image()

# Uncomment the below code to make sure you generate "blank" black and white images

test_get_black_image()
test_get_white_image()