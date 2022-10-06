import cv2

# We load the pretrained fucker
tfd = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# The data.haarcascades isn't included either in the video LOL

# We give'im food
test1 = cv2.imread(r"C:\Users\Usuario\Desktop\Programming\PythonStuff\artificialScumbag\notTheSame.png")
test2 = cv2.imread(r"C:\Users\Usuario\Desktop\Programming\PythonStuff\artificialScumbag\dicaprio.png")
# Video retard didn't put the fucking address, just the name and didn't convert it to a raw string lmao

# Now we set the to grayscale
gtest1 = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
gtest2 = cv2.cvtColor(test2, cv2.COLOR_BGR2GRAY)

# We find the face
faceCoord = tfd.detectMultiScale(gtest1)

# We draw on it

def rectangle(number,useimage,coords =[], *args):

    fcx = coords[number,0]
    fcy = coords[number,1]
    fch = coords[number,2]
    fcw = coords[number,3]

    cv2.rectangle(useimage,(fcx,fcy),(fcx+fcw,fcy+fch),(255,0,0),2)

rectangle(0,gtest1,faceCoord)


# We preview the food
cv2.imshow('We are not the same',gtest1)

# Press key to close it
cv2.waitKey()