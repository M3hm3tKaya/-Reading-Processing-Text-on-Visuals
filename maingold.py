import time
import pyautogui
from cv2 import cv2
import easyocr

# image1 = pyautogui.screenshot()
# image1.save("1.png")

while True:
    time.sleep(2)
    image1 = pyautogui.screenshot()
    image1.save("1.png")
    image2 = cv2.imread("1.png")
    cut_image = image2[950: 1040,1400:1750]

    cv2.imwrite("cut_image.png",cut_image)
    try:

        reader = easyocr.Reader(['en'],gpu=True)
        result = reader.readtext("cut_image.png")
        result = result[0][1]
        file = open("C:/Users/mehme/OneDrive - ogr.gelisim.edu.tr/Masaüstü/BuildABoat_Gold.txt", "w")
        file.write(result)
        file.close()
        print(result)

    except:
        continue



