import os
import qrcode 
url=(input("please enter the url: ")) 
while not url.strip(): 
    print("url is empty. Please enter a valid url.") 
    url=(input("please enter the url: "))
a=qrcode.make(url)
img=a.get_image()
img.show()
save=input("Do you want to save the QR (yes or no): ")
if save=='yes':
    image_name=input("please enter the name you want to save it with: ")
    img.save(f"{image_name}.png")
    print("QR code saved successfully")
    print(os.getcwd())
else:
    img.show()

