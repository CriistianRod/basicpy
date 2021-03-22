import turtle

def run():
    window = turtle.Screen()
    cris = turtle.Turtle()

    make_square(cris)

    turtle.mainloop()

def make_square(cris):
    length = int(input('¿De qué tamaño será el cuadrado?: '))

    for i in range(4):
        make_line_and_turn(cris, length)


def make_line_and_turn(cris, length):
    cris.speed(1)
    cris.forward(length)
    cris.left(90)
    

if __name__ == '__main__':
    run()