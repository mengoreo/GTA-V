import modules


X = 0
Y = 40
WIDTH = 1200
HEIGHT = 900
while True:
    original_screen = modules.capture(x=X, y=Y, width=WIDTH, height=HEIGHT)
    processed_screen = modules.process(original_screen)
    if not modules.show(processed_screen):
        break
