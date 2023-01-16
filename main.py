import cv2

cap = cv2.VideoCapture(0) # sets this video capture as the first webcam//.VideoCapture is getting information from the webcam


cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
while True:
    _, frame = cap.read()  # Reading and outputting the information from the webcam
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Converts our color detection from BRG range to HSV Range
    height, width, _ = frame.shape

    # This gives us our coordinates for making the center bore
    cx = int(width/2)
    cy = int(height/2)

    pixelCenter = hsv_frame[cy, cx]

    hueValue = pixelCenter[0]
    color = "undefined"
    if hueValue < 5:
        color = 'red'
    elif hueValue < 22:
        color = 'orange'
    elif hueValue < 33:
        color = 'yellow'
    elif hueValue < 78:
        color = 'green'
    elif hueValue < 131:
        color = 'blue'
    elif hueValue < 167:
        color = 'violet'
    else:
        color = 'shi ion know, prolly red'


    pixelCenterBRG = frame[cy,cx] #This is our pure color numeric ,so we use this for displaying text

    # If you see the error 'not numeric' it's because a value isn't an integer
    cv2.putText(frame, color, (10, 50), 0, 1, (int(pixelCenterBRG[0]), int(pixelCenterBRG[1]), int(pixelCenterBRG[2])), 2)
    cv2.circle(frame, (cx, cy), 5, (225, 0, 0), 3)
    # Make sure these lines of code are always at the bottom
    # These are the compiling code so everything must be done before then
    cv2.imshow("Frames", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
