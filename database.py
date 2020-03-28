# import kivy

# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.camera import Camera
# from kivy.uix.boxlayout import BoxLayout

# from kivy.uix.button import Button

# class MainApp(App):
#     def build(self):
#         layout = BoxLayout(orientation='vertical')
#         self.cam = Camera(play=True, index=2, resolution=(640,480))
#         self.camaraClick = Button(text="Take Photo")
#         self.camaraClick.bind(on_press=self.onCameraClick)
#         self.camaraClick.size_hint=(.5, .2)
#         self.camaraClick.pos_hint={'x': .25, 'y':.75}
#         layout.add_widget(self.cam)
#         layout.add_widget(self.camaraClick)
#         return layout
	
#     def onCameraClick():
# 	    pass

# if __name__== "__main__":
#     MainApp().run(




# mait.mai()

# mait.got()

# import time
# from reportlab.lib.enums import TA_JUSTIFY
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib.units import inch
# doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
#                         rightMargin=72,leftMargin=72,
#                         topMargin=72,bottomMargin=18)
# Story=[]
# nam = "atss"
# logo = "eye.jpg"
# logo2 = "eye.jpg"
# magName = "Virtual Health"
# issueNum = 12
# subPrice = "99.00"
# limitedDate = "03/05/2010"
# freeGift = "tin foil hat"
# formatted_time = time.ctime()
# full_name = "Abhishek Tiwari"
# address_parts = ["kuch bhi", "address hai mera"]
# im = Image(logo, 2*inch, 2*inch)
# im2 = Image(logo2,2*inch,2*inch)
# Story.append(im)
# Story.append(im2)
# styles=getSampleStyleSheet()
# styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
# ptext = '<font size="12">%s</font>' % formatted_time
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
# # Create return address
# ptext = '<font size="12">%s</font>' % full_name
# Story.append(Paragraph(ptext, styles["Normal"]))       
# for part in address_parts:
#     ptext = '<font size="12">%s</font>' % part.strip()
#     Story.append(Paragraph(ptext, styles["Normal"]))   
# Story.append(Spacer(1, 12))
# ptext = '<font size="12">Dear %s:</font>' % full_name.split()[0].strip()
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
# ptext = f'<font size="12">Name : {nam} </font>' 
# Story.append(Paragraph(ptext, styles["Justify"]))
# Story.append(Spacer(1, 12))
# ptext = '<font size="12">Eye : Normal </font>' 
# Story.append(Paragraph(ptext, styles["Justify"]))
# Story.append(Spacer(1, 12))
# ptext = '<font size="12">Skin : Normal </font>' 
# Story.append(Paragraph(ptext, styles["Justify"]))
# ptext = '<font size="12">Weight : 100kg </font>' 
# Story.append(Paragraph(ptext, styles["Justify"]))
# Story.append(Spacer(1, 30))
# ptext = '<font size="12">Thank you very much and we look forward to serving you.</font>'
# Story.append(Paragraph(ptext, styles["Justify"]))
# Story.append(Spacer(1, 12))
# ptext = '<font size="12">Sincerely,</font>'
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 48))
# ptext = '<font size="12">Team TechnoBuilders</font>'
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
# doc.build(Story)



# import email, smtplib, ssl

# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# subject = "An email with attachment from Python"
# body = "This is an email with attachment sent from Python"
# sender_email = "anktiw2000@gmail.com"
# receiver_email = "ankit2632000@gmail.com"  
# password = "Fall@25404"

# # Create a multipart message and set headers
# message = MIMEMultipart()
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Subject"] = subject
# message["Bcc"] = receiver_email  # Recommended for mass emails

# # Add body to email
# message.attach(MIMEText(body, "plain"))

# filename = "hello.pdf"  # In same directory as script

# # Open PDF file in binary mode
# with open(filename, "rb") as attachment:
#     # Add file as application/octet-stream
#     # Email client can usually download this automatically as attachment
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(attachment.read())

# # Encode file in ASCII characters to send by email    
# encoders.encode_base64(part)

# # Add header as key/value pair to attachment part
# part.add_header(
#     "Content-Disposition",
#     f"attachment; filename= {filename}",
# )

# # Add attachment to message and convert message to string
# message.attach(part)
# text = message.as_string()

# # Log in to server using secure context and send email
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, text)


# import cv2
# import numpy as np
# from tensorflow.keras import models,layers,optimizers

# # model1=models.load_model('eyed.h5',compile=True)
# model2=models.load_model('eyed.h5',compile=True)

# img3 = cv2.imread('ewq2.jpeg',1)
# img3 = cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)
# img3 = cv2.resize(img3,(224,224))
# img4 = np.reshape(img3,[1,224,224,3])
# img4=img4/255.0
# disease = model2.predict_classes(img4)
# prediction = disease[0]
# print(prediction)

# import cv2 
import pytesseract

# img = cv2.imread('pytte.png')

# # Adding custom options
# custom_config = r'--oem 3 --psm 6'
# text = pytesseract.image_to_string(img, config=custom_config)

# print(text)


import cv2
import numpy as np

img = cv2.imread('pytte.png')

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


custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)

print(text)