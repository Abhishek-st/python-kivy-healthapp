import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.uix.button import Button
import time
import cv2
import numpy as np
from tensorflow.keras import models,layers,optimizers
from kivy.clock import Clock
import pyaudio
from gtts import gTTS
from playsound import playsound
import mait

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pytesseract


import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)


model1=models.load_model('eyed.h5',compile=True)
model2=models.load_model('skin_dis_1.h5',compile=True)


name = 'Abhishek Sunil Tiwari'
eye = 'Normal'
skin = 'Normal'
weight = 100
pulse = 72
temp = 37.2
med = 'ibuprofen'



subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "anktiw2000@gmail.com"
receiver_email = "ankit2632000@gmail.com"  
password = "Fall@25404"


class MainWindow(Screen):
    pass


class SkinWindow(Screen):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        global skin 
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        img = "IMG_{}.png".format(timestr)
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
        # model1=models.load_model('skin_dis.h5',compile=True)
        img3 = cv2.imread(img,1)
        img3 = cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)
        img3 = cv2.resize(img3,(224,224))
        img4 = np.reshape(img3,[1,224,224,3])
        img4=img4/255.0
        disease = model2.predict_classes(img4)
        prediction = disease[0]
        print(prediction)
        if prediction == 1:
            skin = 'Normal'
        else:
            skin = 'Cancer'



class EyeWindow(Screen,BoxLayout):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.cam = Camera(play=True, index=2, resolution=(640,480))
        self.camaraClick = Button(text="Take Photo")
        self.camaraClick.bind(on_press=self.capture)
        self.camaraClick.size_hint=(.5, .2)
        self.camaraClick.pos_hint={'x': .25, 'y':.75}
        layout.add_widget(self.cam)
        layout.add_widget(self.camaraClick)
        return layout

    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        global eye
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        img = "IMG_{}.png".format(timestr)
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
        img3 = cv2.imread(img,1)
        img3 = cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)
        img3 = cv2.resize(img3,(224,224))
        img4 = np.reshape(img3,[1,224,224,3])
        img4=img4/255.0
        disease = model1.predict_classes(img4)
        prediction = disease[0]
        print(prediction)
        if prediction == 1:
            eye = 'Normal'
        else:
            eye = 'Cataract'
        

    
    

class WeightWindow(Screen):
    pass

class TempWindow(Screen):
    pass

class Message(Widget):
    pass


class MedWindow(Screen, App):
    def emo(self):
        genpdf()
        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        filename = "form_letter.pdf"  # In same directory as script

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)

class BldsgWindow(Screen):
    def capeye(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        global eye
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        img = "IMG_{}.png".format(timestr)
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
        img3 = cv2.imread(img,1)
        img3 = cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)
        img3 = cv2.resize(img3,(224,224))
        img4 = np.reshape(img3,[1,224,224,3])
        img4=img4/255.0
        disease = model1.predict_classes(img4)
        prediction = disease[0]
        if prediction == 1:
            eye = 'Normal'
        else:
            eye = 'Cataract'
        print(eye)

    def capskin(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        global skin 
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        img = "IMG_{}.png".format(timestr)
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
        # model1=models.load_model('skin_dis.h5',compile=True)
        img3 = cv2.imread(img,1)
        img3 = cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)
        img3 = cv2.resize(img3,(224,224))
        img4 = np.reshape(img3,[1,224,224,3])
        img4=img4/255.0
        disease = model2.predict_classes(img4)
        prediction = disease[0]
        if prediction == 1:
            skin = 'Normal'
        else:
            skin = 'Cancer'
        print(skin)

    def captes(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        img = "IMG_{}.png".format(timestr)
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
        img2 = cv2.imread(img)
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(img2, config=custom_config)
        print(text)



class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv

def genpdf():
    # dic = {

# }
    Story=[]
    logo = "eye.jpg"
    logo2 = "eye.jpg"
    magName = "Virtual Health"
    issueNum = 12
    subPrice = "99.00"
    limitedDate = "03/05/2010"
    freeGift = "tin foil hat"
    formatted_time = time.ctime()
    full_name = "Abhishek Tiwari"
    address_parts = ["kuch bhi", "address hai mera"]
    im = Image(logo, 2*inch, 2*inch)
    im2 = Image(logo2,2*inch,2*inch)
    Story.append(im)
    Story.append(im2)
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size="12">%s</font>' % formatted_time
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    # Create return address
    ptext = '<font size="12">%s</font>' % full_name
    Story.append(Paragraph(ptext, styles["Normal"]))       
    for part in address_parts:
        ptext = '<font size="12">%s</font>' % part.strip()
        Story.append(Paragraph(ptext, styles["Normal"]))   
    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Dear %s:</font>' % full_name.split()[0].strip()
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ptext = f'<font size="12">Name : {name} </font>' 
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = f'<font size="12">Eye : {eye} </font>' 
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = f'<font size="12">Skin : {skin} </font>' 
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = f'<font size="12">Body Temperature : {temp} </font>' 
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = f'<font size="12">Pulse : {pulse} </font>' 
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Medicine Given : {med} </font>' 
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = f'<font size="12">Weight : {weight} kg </font>' 
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 30))
    ptext = f'<font size="12">Thank you very much and we look forward to serving you.</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = f'<font size="12">Sincerely,</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 48))
    ptext = f'<font size="12">Team TechnoBuilders</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    doc.build(Story)

if __name__ == "__main__":
    MyMainApp().run()






# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 
