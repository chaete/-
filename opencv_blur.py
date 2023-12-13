import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def adjust_blur_strength(image, strength=30, kernel_size=(99, 99)):
    blurred_roi = cv2.GaussianBlur(image, kernel_size, strength)
    return blurred_roi

def mouse_callback(event, x, y, flags, param):
    global img, faces, selected_face, v
    if event == cv2.EVENT_LBUTTONDOWN:
        for i, (fx, fy, fw, fh) in enumerate(faces):
            if x > fx and x < fx + fw and y > fy and y < fy + fh:
                selected_face = i
                break

img = cv2.imread('cha_image.jpeg')
if img is None:
    print("Not photo")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 5)
selected_face = None
v = 20

cv2.namedWindow('Blur out')
cv2.setMouseCallback('Blur out', mouse_callback)

while True:

    img_display = img.copy()

    for i, (x, y, w, h) in enumerate(faces):
        roi = img[y:y + h, x:x + w]
        if i == selected_face:
     
            roi = adjust_blur_strength(roi, strength=v, kernel_size=(99, 99))
        img_display[y:y + roi.shape[0], x:x + roi.shape[1]] = roi

        cv2.rectangle(img_display, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Blur out', img_display)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    k = cv2.waitKey(1) & 0xFF
    if k == ord('b'):
        if v > 0:
            v -= 1
    elif k == ord('n'):
        v += 1

cv2.destroyAllWindows()
