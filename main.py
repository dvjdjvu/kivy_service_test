#!/usr/bin/python3
#-*- coding: utf-8 -*-

import kivy
kivy.require("2.1.0")
from kivy.app import App
from kivy.uix.button import Button

from kivy.utils import platform

import jnius
from jnius import cast
from jnius import autoclass

# Подключение классов Android
if platform == 'android':
    # Подключение класса System
    System = autoclass('java.lang.System')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    CurrentActivity = cast('android.app.Activity', PythonActivity.mActivity)

# Класс графики, который создает кнопку для выхода из приложения.
class ButtonApp(App):

    def build(self):
        # use a (r, g, b, a) tuple
        btn = Button(text ="Push Me !",
                   font_size ="20sp",
                   background_color = (1, 1, 1, 1),
                   color = (1, 1, 1, 1),
                   size_hint = (.2, .1),
                   pos_hint = {'x':.4, 'y':.45})

        # bind() use to bind the button to function callback
        btn.bind(on_press = self.callback)
        return btn

    def on_start(self):
        self.service = None

        # При старте приложения запускаем сервис.
        self.service_start()

    # callback function tells when button pressed
    def callback(self, event):
        if platform == 'android':
            CurrentActivity.finishAndRemoveTask()

            System.exit(0)
        else :
            exit()

    # функция запуска сервиса
    def service_start(self):
        if platform == 'android':
            self.service = autoclass(CurrentActivity.getPackageName() + ".ServiceTest")
            self.service.start(CurrentActivity, "")

    # функция остановки сервиса
    def service_stop(self):
        if self.service :
            if platform == 'android':
                self.service.stop(CurrentActivity)

##
#  Старт.
##
if __name__ == "__main__":
    # Отрисовка графики приложения
    ButtonApp().run()
