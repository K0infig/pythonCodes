import cv2
import time
import random
import dropbox
from dropbox.files import WriteMode

start_time = time.time()
print(start_time)

num = random.randint(0,100)

def takePicture():

    videoCaptureObject = cv2.VideoCapture(0)
  
    result = True

    while(result):

        ret, frame = videoCaptureObject.read()
        print(ret)

        imageName = "image"+ str(num)+ ".png"
        cv2.imwrite(imageName, frame)
        result = False

    return imageName
    print("Pic taken")

    videoCaptureObject.release()

    cv2.destroyAllWindows()


def upload_file(imageName):
        
        access_token = 'nT0QDyThNTcAAAAAAAAAAQhpXvwjnPaAhvUZS2VGBxBcUr8636p6AuenxKfO_amY'
    

        file_from = imageName
        file_to = "/oodles/"+(imageName)
        dbx = dropbox.Dropbox(access_token)
        print("Successfully connected to dropbox account!!!")

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode = WriteMode('overwrite'))


def main():
    while(True):
        if((time.time() - start_time >=1)):
            name  = takePicture()
            upload_file(name)
            


main()


