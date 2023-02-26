import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import csv
from datetime import datetime

class QBotGrid(Widget):
    startTime = ObjectProperty(None)
    endTime = ObjectProperty(None)
    queueTime = ObjectProperty(None)
    parkChoice = ObjectProperty(None)
    rideChoice = ObjectProperty(None)

    def startQueue(self):
        self.parkChoice = self.parkChoice.text
        self.rideChoice = self.rideChoice.text
        self.startTime = datetime.now()
        print(self.parkChoice, self.rideChoice, self.startTime)

    def endQueue(self):
        self.endTime = datetime.now()
        print(self.endTime)

    def queueDuration(self):
        self.queueTime = self.endTime-self.startTime
        print(self.queueTime)

    def checkData(self):
        content = Button(text="Submitting this info to the database:\n\nPark: {}\nRide: {}\nQueue Duration: {}\n\nTap to continue.".format(self.parkChoice,self.rideChoice,self.queueTime))
        pop = Popup(content=content,auto_dismiss=False)
        content.bind(on_press=pop.dismiss)
        pop.open()
        
        q = [self.parkChoice,self.rideChoice,self.startTime,self.queueTime]
        f = open("queue_times.csv", 'a')
        w = csv.writer(f, lineterminator='\n')
        w.writerows([q])
        f.close()
        
kv = Builder.load_file("qbot.kv")

class QBotApp(App):
    def build(self):
        return QBotGrid()

if __name__ == "__main__":
    QBotApp().run()