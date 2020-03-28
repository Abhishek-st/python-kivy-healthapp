# '''
# Camera Example
# ==============

# This example demonstrates a simple use of the camera. It shows a window with
# a buttoned labelled 'play' to turn the camera on and off. Note that
# not finding a camera, perhaps because gstreamer is not installed, will
# throw an exception during the kv language processing.

# '''

# # Uncomment these lines to see all the messages
# # from kivy.logger import Logger
# # import logging
# # Logger.setLevel(logging.TRACE)

# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.boxlayout import BoxLayout
# import time
# Builder.load_string('''
# <CameraClick>:
#     orientation: 'vertical'
#     Camera:
#         id: camera
#         resolution: (640, 480)
#         play: False
#     ToggleButton:
#         text: 'Play'
#         on_press: camera.play = not camera.play
#         size_hint_y: None
#         height: '48dp'
#     Button:
#         text: 'Capture'
#         size_hint_y: None
#         height: '48dp'
#         on_press: root.capture()
# ''')


# class CameraClick(BoxLayout):
#     def capture(self):
#         '''
#         Function to capture the images and give them the names
#         according to their captured time and date.
#         '''
#         camera = self.ids['camera']
#         timestr = time.strftime("%Y%m%d_%H%M%S")
#         print(camera.texture)
#         camera.export_to_png("IMG_{}.png".format(timestr))
#         print("Captured")


# class TestCamera(App):

#     def build(self):
#         return CameraClick()


# TestCamera().run()

# __author__ = 'bunkus'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

# import cv2

# class CamApp(App):

    # def build(self):
    #     self.img1=Image()
    #     layout = BoxLayout()
    #     layout.add_widget(self.img1)
    #     #opencv2 stuffs
    #     self.capture = cv2.VideoCapture(0)
    #     cv2.namedWindow("CV2 Image")
    #     Clock.schedule_interval(self.update, 1.0/33.0)
    #     return layout

    # def update(self, dt):
    #     # display image from cam in opencv window
    #     ret, frame = self.capture.read()
    #     cv2.imshow("CV2 Image", frame)
    #     # convert it to texture
    #     buf1 = cv2.flip(frame, 0)
    #     buf = buf1.tostring()
    #     texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
    #     texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
    #     # display image from the texture
    #     self.img1.texture = texture1

# if __name__ == '__main__':
#     CamApp().run()
#     cv2.destroyAllWindows()


# import kivy.core.text
# import cv2
# from kivy.app import App
# from kivy.base import EventLoop
# from kivy.uix.image import Image
# from kivy.clock import Clock
# from kivy.graphics.texture import Texture
# from kivy.uix.boxlayout import BoxLayout
# from kivy.core.window import Window


# class KivyCamera(Image):

#     def __init__(self, **kwargs):
#         super(KivyCamera, self).__init__(**kwargs)
#         self.capture = None

#     def start(self, capture, fps=30):
#         self.capture = capture
#         Clock.schedule_interval(self.update, 1.0 / fps)

#     def stop(self):
#         Clock.unschedule_interval(self.update)
#         self.capture = None

#     def update(self, dt):
#         return_value, frame = self.capture.read()
#         if return_value:
#             texture = self.texture
#             w, h = frame.shape[1], frame.shape[0]
#             if not texture or texture.width != w or texture.height != h:
#                 self.texture = texture = Texture.create(size=(w, h))
#                 texture.flip_vertical()
#             texture.blit_buffer(frame.tobytes(), colorfmt='rgb')
#             self.canvas.ask_update()


# capture = None


# class QrtestHome(BoxLayout):

#     def init_qrtest(self):
#         pass

#     def dostart(self, *largs):
#         global capture
#         capture = cv2.VideoCapture(0)
#         self.ids.qrcam.start(capture)

#     def doexit(self):
#         global capture
#         if capture != None:
#             capture.release()
#             capture = None
#         EventLoop.close()


# class qrtestApp(App):

#     def build(self):
#         Window.clearcolor = (.4,.4,.4,1)
#         Window.size = (400, 300)
#         homeWin = QrtestHome()
#         homeWin.init_qrtest()
#         return homeWin

#     def on_stop(self):
#         global capture
#         if capture:
#             capture.release()
#             capture = None

# qrtestApp().run()


# Sample Python application demonstrating 
# How to create GridLayout in Kivy 

# import kivy module 
import kivy 
	
# base Class of your App inherits from the App class. 
# app:always refers to the instance of your application 
from kivy.app import App 
	
# creates the button in kivy 
# if not imported shows the error 
from kivy.uix.button import Button 

# The GridLayout arranges children in a matrix. 
# It takes the available space and 
# divides it into columns and rows, 
# then adds widgets to the resulting “cells”. 
from kivy.uix.gridlayout import GridLayout 

# creating the App class 
class Grid_LayoutApp(App): 

	# to build the application we have to 
	# return a widget on the build() function. 
	def build(self): 

		# adding GridLayouts in App 
		# Defining number of coloumn 
		# You can use row as well depends on need 
		layout = GridLayout(cols = 2) 

		# 1st row 
		layout.add_widget(Button(text ='Skin Disease')) 
		layout.add_widget(Button(text ='Eye Disease')) 

		# 2nd row 
		layout.add_widget(Button(text ='Weight')) 
		layout.add_widget(Button(text ='Body Temperature')) 

		# 3rd row 
		layout.add_widget(Button(text ='Blood-sugar')) 
		layout.add_widget(Button(text ='Basic Medication')) 


		# returning the layout 
		return layout 

# creating object of the App class 
root = Grid_LayoutApp() 
# run the App 
root.run() 
