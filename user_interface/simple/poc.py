#!/usr/bin/env python3
#
# poc.py
#
# Copyright (c) 2017 Franco Masotti <franco.masotti@student.unife.it>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

'''
class EngagedLabel(Widget):
    engaged = ObjectProperty(None) 

    def display():
        pass
    def delete():        pass
'''

class SlidersWidget(Widget):

    slider_one = ObjectProperty(None)
#    switch = ObjectProperty(None)

    # Respond to actions.
    def slider_value(self, instance, value):
        if value > 50:
            print ("This is a high value:" + str(value))
        else:
            print ("This is a LOW value:" + str(value))
        #print (instance)
        #print(self.ids)

    def switch_activeness(self, instance, active):
        if active:
            self.engaged = Label(text="[b][color=ff0000]Engaged[/color][/b]",markup=True)
            # Add this as a son of the current FloatLayout instance instead of
            # the current Slider instance
            self.parent.add_widget(self.engaged)
            print ("Enabled, something gets crunched by Python")
        else:
            self.parent.remove_widget(self.engaged)
            print ("Disabled")

class PocApp(App):
    def build(self):
        return SlidersWidget()


if __name__ == '__main__':
    PocApp().run()

