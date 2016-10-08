import parser
deltax = float(raw_input("deltax "))
xCoordinate = float(raw_input("xCoordinate "))
yCoordinate = float(raw_input("yCoordinate "))
slopeEquationString = raw_input("slopeEquation ")
iterations = int(raw_input("iterations "))
slopeEquation = parser.expr(slopeEquationString).compile()
xOld = xCoordinate
yOld = yCoordinate
yNew = 0
xNew = 0


def xNewEquation(xOld, deltax):
    global xNew
    xNew = xOld + deltax


def yNewEquation(xOld, yOld, deltax, slopeEquation):
    global yNew
    y = yOld
    x = xOld
    yNew = (yOld + eval(slopeEquation)*deltax)


def setNewValues():
    global xOld
    global yOld
    xOld = xNew
    yOld = yNew

for i in range(iterations):
    xNewEquation(xOld, deltax)
    yNewEquation(xOld, yOld, deltax, slopeEquation)
    print xNew, yNew
    setNewValues()


wait = raw_input()
