
layout = BoxLayout(orientation='vertical')
Button(text="Take Photo")

        self.camaraClick = Button(text="Take Photo")

        self.camaraClick.size_hint=(.5, .2)

        self.camaraClick.pos_hint={'x': .25, 'y':.75}

 

        # bind the button's on_press to onCameraClick

        self.camaraClick.bind(on_press=self.onCameraClick)



        layout.add_widget(self.cameraObject)

        layout.add_widget(self.camaraClick)

       

        # return the root widget

        return layout

