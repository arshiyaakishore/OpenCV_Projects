import cv2


def sketch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    
    blur_gray = cv2.GaussianBlur(gray, (5, 5), 900) 
    
    edges = cv2.Canny(blur_gray, 20, 70) 
    
    ret, thr = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV) 
    return gray, thr

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Error: Unable to open camera.")
    exit()

while True:
    ret, frame = cam.read()
    
    if not ret:
        print("Error: Unable to read frame from the camera.")
        break
    
    if frame is None:
        print("Error: Frame is empty.")
        continue
    
    cv2.imshow('thresholded', sketch(frame)[1]) #
    
    key = cv2.waitKey(1) 
    if key == 27:  # Esc key
        break
    elif key == 13:  # Enter key
        cv2.imwrite('sketch.jpg', sketch(frame)[1])
        print('Image Saved!!!')


cam.release()
cv2.destroyAllWindows()
