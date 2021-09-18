print("This is Divit bhaisaab ka calculator")

def distance():
    w=input("Input the number for x1")
    x=input("Input the number for x2")
    y=input("Input the number for y1")
    z=input("Input the number for y2")
    distance= ((float(x)-float(w))**2+(float(z)-float(y))**2)**0.5
    print(distance)

def midpoint():
    JUSTIN=input("Input the number for x1")
    BIEBER=input("Input the number for y1")
    KATIE=input("Input the number for x2")
    PERRY=input("Input the number for y2")
    midpointX = ((float(JUSTIN)+float(KATIE))/2)
    midpointY= ((float(BIEBER)+float(PERRY))/2)
    print("("+str(midpointX)+","+str(midpointY)+")")

Question = input("Which operation would you like to perform? Distance or Midpoint?")
Question=Question.lower()
if Question=="distance":
    distance()

elif Question=="midpoint":
    midpoint()

else : print("That is not an operation")