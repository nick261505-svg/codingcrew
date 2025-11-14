import turtle

turtle.register_shape("0926/owl.gif")
미켈란젤로=turtle.Turtle()
미켈란젤로.shape("0926/owl.gif")
#미켈란젤로.hideturtle()
한변=300

for _ in range(3):
    미켈란젤로.forward(한변)
    미켈란젤로.right(120)

미켈란젤로.forward(한변/3)
미켈란젤로.left(60)
미켈란젤로.forward(한변/3)

for _ in range(3):
    미켈란젤로.right(120)
    미켈란젤로.forward(한변)

turtle.done()