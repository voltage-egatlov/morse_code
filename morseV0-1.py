from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import time




class MainApp(App):
    def build(self):
        self.printed=TextInput(multiline=True, readonly=False, halign="left", font_size=55)
        self.translated=TextInput(multiline=True, readonly=True, halign="left", font_size=55)

        self.nowTime= None
        self.futureTime=None
        self.spaceTimeStart=0
        self.spaceTimeEnd=None
        self.temporaryHolder=""
        self.list_of_things=[["._", "A"],
                            ["_...", "B"],
                            ["_._.", "C"],
                            ["_..", "D"],
                            [".", "E"],
                            [".._.", "F"],
                            ["__.", "G"],
                            ["....", "H"],
                            ["..", "I"],
                            [".___", "J"],
                            ["_._", "K"],
                            ["._..", "L"],
                            ["__", "M"],
                            ["_.", "N"],
                            ["___", "O"],
                            [".__.", "P"],
                            ["__._", "Q"],
                            ["._.", "R"],
                            ["...", "S"],
                            ["_", "T"],
                            [".._", "U"],
                            ["..._", "V"],
                            [".__", "W"],
                            ["_.._", "X"],
                            ["_.__", "Y"],
                            ["__..", "Z"],
                            ]
        main_layout = BoxLayout(orientation="vertical")
        main_layout.add_widget(self.printed)
        main_layout.add_widget(self.translated)

        sub_layout= BoxLayout(orientation="horizontal")
        btn = Button(background_normal='button_img.png',
                    background_down='button_pressed.png',
                    size_hint=(1, 1),
                    pos_hint={'center_x': 0.5, 'center_y': .5})
        btn.bind(on_press=self.on_press_)
        btn.bind(on_release=self.on_release_)
        sub_layout.add_widget(btn)
        
        btn2=Button(background_normal='green_button.png',
                    background_down='green_button.png',
                    size_hint=(1, 1),
                    pos_hint={'center_x': 0.5, 'center_y': .5})
        btn2.bind(on_press=self.runRQ)
        btn2.bind(on_release=self.reset)
        sub_layout.add_widget(btn2)
        main_layout.add_widget(sub_layout)
        return main_layout
    def runRQ(self, instance):
        for letter in self.list_of_things:
            if letter[0]==self.temporaryHolder:
                currentTemp=self.translated.text
                self.translated.text=currentTemp+letter[1]
                self.temporaryHolder=""
    def reset(self, instance):
        self.printed.text=""
        self.translated.text=""
        self.nowTime= None
        self.futureTime=None
        self.spaceTimeStart=0
        self.spaceTimeEnd=None
        self.temporaryHolder=""
    def on_press_(self, instance):
        self.spaceTimeEnd=time.time()
        spaceTimeTook=self.spaceTimeEnd-self.spaceTimeStart
        current=self.printed.text
        if spaceTimeTook>1.5:
            self.printed.text= current+" "
            for letter in self.list_of_things:
                if letter[0]==self.temporaryHolder:
                    currentTemp=self.translated.text
                    self.translated.text=currentTemp+letter[1]
                    self.temporaryHolder=""
                    
                    
        self.nowTime=time.time()

    def on_release_(self, instance):
        current=self.printed.text
        
        self.futureTime=time.time()
        
        amountOfTime=self.futureTime-self.nowTime
        amountOfTime=round(amountOfTime, 3)
        
        if amountOfTime>0 and amountOfTime<0.3:
            self.printed.text= current+"."
            currentTemp=self.temporaryHolder
            self.temporaryHolder=currentTemp+"."
            
        elif amountOfTime>0.5 and amountOfTime<1.5:
            self.printed.text= current+"_"
            currentTemp=self.temporaryHolder
            self.temporaryHolder=currentTemp+"_"
            
        #newText=current+str(amountOfTime)+" "
        #self.printed.text= newText
        
        self.spaceTimeStart=time.time()
        
if __name__ == '__main__':
    app = MainApp()
    app.run()