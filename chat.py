from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

import pyaudio
from gtts import gTTS
from playsound import playsound

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot("HealthBot")

convo = [
    'hello',
    'hi sir I am health bot can I get your age',
    'what is the matter with you',
    'ok fine sir, let me give you something',
    'thank you',
    'your welcome sir'

]

trainer = ListTrainer(bot)
trainer.train(convo)


class Message(Widget):
    pass

class KatApp(App):
    def post(self):
        msg = self.root.ids.usrinp.text
        if len(msg) > 0:
            msgbox = Message()
            msgbox.ids.mlab.text = msg
            msgbox.pos_hint = {'right': 1}
            self.root.ids.chatbox.add_widget(msgbox)
            self.root.ids.scrlv.scroll_to(msgbox)
            self.root.ids.usrinp.text = ''

    def resp(self, msg):
        if len(msg) > 0:
            ansr = str((bot.get_response(msg)))
            tts=gTTS(text=ansr, lang= 'en-in')
            tts.save('audio.mp3')
            # mixer.init()
            # mixer.music.load('audio.mp3')
            # mixer.music.play()
            playsound('audio.mp3')
            ansrbox = Message()
            ansrbox.ids.mlab.text = str(ansr)
            ansrbox.pos_hint = {'x': 0}
            self.root.ids.chatbox.add_widget(ansrbox)
            self.root.ids.scrlv.scroll_to(ansrbox)
            self.root.ids.usrinp.text = ''

    def build(self):
        return Builder.load_string('''
<Message@Widget>:
    size_hint: None, None
    height: mlab.height
    width: mlab.width
    canvas:
        Color:
            rgba: 0, 1, 0, 0.7
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        id: mlab
        center: root.center
        padding: 10, 10
        markup: True
        text_size: (None, None)
        text: ''
        haligh: 'left'
        valign: 'top'
        size_hint: (1, None)
        size: self.texture_size
        color: 0, 0, 0

ScreenManager:
    Screen:

        BoxLayout:
            orientation: 'vertical'

            ScrollView:

                canvas.before:
                    Color:
                        rgb: 1, 1, 1
                    Rectangle:
                        pos: self.pos
                        size: self.size

                BoxLayout:
					orientation: 'vertical'
                    id: chatbox
                    padding: 10, 10
                    spacing: 5

            BoxLayout:
                orientation: 'horizontal'
                padding: 10, 10, 10, 10
                size_hint: 1, None
                height: 50

                BoxLayout:
                    id: inpbox
                    height: max(40, scrlv.height)
                    size_hint: 0.9, None

                    ScrollView:
                        id: scrlv
                        width: inpbox.width - 15
                        x: inpbox.x + 10
                        y: inpbox.y
                        height: 
                            (len(usrinp._lines)+1) * usrinp.line_height - 5 \
                            if (len(usrinp._lines)+1 <= 5) \
                            else 5 * usrinp.line_height - 5

                        TextInput:
                            id: usrinp
                            pos_hint: {'right': 1}
                            valign: 'middle'
                            halign: 'left'
                            font_size: 16
                            multiline: True
                            size_hint: scrlv.size_hint_x, None
                            padding: 10, 0, 10, 0


                Button:
                    id: post
                    border: 0, 0, 0, 0
                    size: 40, 40
                    size_hint: None, None
                    on_press:
                        root.inp = usrinp.text
                        app.post()
                    on_release:
                        app.resp(root.inp)
''')

if __name__ == "__main__":
    KatApp().run()
