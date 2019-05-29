import modules

X = 10
Y = 50
WIDTH = 1190
HEIGHT = 720


while True:
    original_screen = modules.capture(x=X, y=Y, width=WIDTH, height=HEIGHT)
    processed_screen = modules.process(original_screen)
    if not modules.show(processed_screen):
        break
