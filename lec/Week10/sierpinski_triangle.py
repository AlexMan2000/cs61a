import turtle

# Draw a line
def line():
    t.fd(50)



# Repeatedly call the function f for k times
def repeat(k, f):
    if k == 0:
        return
    else:
        f()
        repeat(k-1, f)

# Draw a triangle
def tri(f):
    def func():
        f()
        t.lt(120)
    repeat(3,func)


def sier(depth, length):
    tri(lambda: t.fd(length) if depth == 1 else leg(depth, length))


def leg(depth, length):
    sier(depth - 1, length // 2)
    # This line does the same thing as t.fd(length), building the larger leg
    # after the innter triangles have been drawn
    t.penup()
    t.fd(length)
    t.pendown()


if __name__ == "__main__":
    t = turtle.Turtle()

    t.speed(0)
    sier(5, 200)

