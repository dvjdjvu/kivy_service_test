#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os

from time import sleep
from kivy.utils import platform

from jnius import cast
from jnius import autoclass

# Подключение классов Android
if platform == 'android':
    PythonService = autoclass('org.kivy.android.PythonService')
    # Автоперезапуск упавшего сревиса
    PythonService.mService.setAutoRestartService(True)

    CurrentActivityService = cast("android.app.Service", PythonService.mService)
    ContextService = cast('android.content.Context', CurrentActivityService.getApplicationContext())
    ContextWrapperService = cast('android.content.ContextWrapper', CurrentActivityService.getApplicationContext())
    Manager = CurrentActivityService.getPackageManager()

    Intent = autoclass('android.content.Intent')

    def application_start():
        pm = CurrentActivityService.getPackageManager()
        ix = pm.getLaunchIntentForPackage(CurrentActivityService.getPackageName())
        ix.setAction(Intent.ACTION_VIEW)
        ix.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK)

        CurrentActivityService.startActivity(ix)

    while True:
        print("python service running.....", CurrentActivityService.getPackageName(), os.getpid())
        sleep(10)
else:
    def application_start():
        pass

    while True:
        print("python service running.....", os.getpid())
        sleep(10)
