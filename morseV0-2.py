from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import time

class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    solution=ObjectProperty(None)
    translation=ObjectProperty(None)
    nowTime= None
    futureTime=None
    nowTime= None
    futureTime=None
    spaceTimeStart=0
    spaceTimeEnd=None
    temporaryHolder=""
    list_of_things=[["._", "A"],
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

    def on_press_(self):
        self.spaceTimeEnd=time.time()
        spaceTimeTook=self.spaceTimeEnd-self.spaceTimeStart
        current=self.solution.text
        if spaceTimeTook>1.5:
            self.solution.text= current+" "
            for letter in self.list_of_things:
                if letter[0]==self.temporaryHolder:
                    currentTemp=self.translation.text
                    self.translation.text=currentTemp+letter[1]
                    self.temporaryHolder=""
                    
                    
        self.nowTime=time.time()

    def on_release_(self):
        current=self.solution.text
        
        self.futureTime=time.time()
        
        amountOfTime=self.futureTime-self.nowTime
        amountOfTime=round(amountOfTime, 3)
        
        if amountOfTime>0 and amountOfTime<0.3:
            self.solution.text= current+"."
            currentTemp=self.temporaryHolder
            self.temporaryHolder=currentTemp+"."
            
        elif amountOfTime>0.5 and amountOfTime<1.5:
            self.solution.text= current+"_"
            currentTemp=self.temporaryHolder
            self.temporaryHolder=currentTemp+"_"
            
        #newText=current+str(amountOfTime)+" "
        #self.printed.text= newText
        
        self.spaceTimeStart=time.time()
    def reset(self):
        self.solution.text=""
        self.translation.text=""
        self.nowTime= None
        self.futureTime=None
        self.spaceTimeStart=0
        self.spaceTimeEnd=None
        self.temporaryHolder=""

class HelperWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()