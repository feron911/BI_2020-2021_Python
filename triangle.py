from turtle import*

speed(100)
right(30)
shape("carpet")
hideturtle()

if __name__ == "__main__":
    def sierpinski(length,depth):
        if depth == 0:
            pd()
            stamp()
            pu()
            return
        else:
            pu()
            for i in range(3):
                forward(length)
                sierpinski(length/2, depth - 1)
                backward(length)
                left(120)

    sierpinski(200,5)