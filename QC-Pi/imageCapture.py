from time import sleep
from picamera import PiCamera


def imageCapture(imageName):
    camera = PiCamera()
    camera.rotation = 270
    camera.resolution = (3280, 2464)
    camera.rotation = 180
    camera.start_preview()
    #warm up
    sleep(3)
    imageJpg = imageName + '.jpg'
    camera.stop_preview()
    camera.capture(imageJpg)
    sleep(2)
    camera.close()

def imagePreview():
    camera = PiCamera()
    camera.start_preview()
    camera.rotation = 180
    sleep(20)
    camera.stop_preview()
    camera.close()

#def imageArea1() #Setting configurations for zoom(dig) for most specific area


#def imageArea2() #Setting configurations for zoom(dig) for middle specific area


#def imageArea3() #Setting configurations for zoom(dig) for least specific area
