#Importing turtle
from turtle import *

#Screen size
setup(1.0, 1.0)
bgpic("4.stars.png")
shape("turtle")

# Print coordinate where clicked:
onscreenclick(lambda x,y: print("x: %d, y: %d" % (x, y)))