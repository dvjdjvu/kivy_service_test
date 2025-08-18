package com.heattheatr.kivy_service_test;

import android.os.Build;
import android.content.BroadcastReceiver;
import android.content.Intent;
import android.content.Context;
import org.kivy.android.PythonActivity;

import java.lang.reflect.Method;

import com.heattheatr.kivy_service_test.ServiceTest;


public class MyBroadcastReceiver extends BroadcastReceiver {

    public MyBroadcastReceiver() {

    }

    // pythonforandroid/bootstraps/webview/build/src/main/java/org/kivy/android/PythonActivity.java
    // method _do_start_service()

    // Запуск приложения.
    public void start_app(Context context, Intent intent) {
        Intent ix = new Intent(context, PythonActivity.class);
        ix.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        context.startActivity(ix);
    }

    // Запуск сервиса.
    public void service_start(Context context, Intent intent) {
        String package_root = context.getFilesDir().getAbsolutePath();
        String app_root =  package_root + "/app";
        Intent ix = new Intent(context, ServiceTest.class);
        ix.putExtra("androidPrivate", package_root);
        ix.putExtra("androidArgument", app_root);
        ix.putExtra("serviceEntrypoint", "service.py");
        ix.putExtra("pythonName", "test");
        ix.putExtra("pythonHome", app_root);
        ix.putExtra("pythonPath", package_root);
        ix.putExtra("serviceStartAsForeground", "true");
        ix.putExtra("serviceTitle", "ServiceTest");
        ix.putExtra("serviceDescription", "ServiceTest");
        ix.putExtra("pythonServiceArgument", app_root + ":" + app_root + "/lib");
        ix.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            context.startForegroundService(ix);
        } else {
            context.startService(ix);
        }
    }

    public void service_stop(Context context, Intent intent) {
        Intent intent_stop = new Intent(context, ServiceTest.class);

        context.stopService(intent_stop);
    }

    // Обработчик сигналов.
    public void onReceive(Context context, Intent intent) {
        switch (intent.getAction()) {
            case Intent.ACTION_BOOT_COMPLETED:
                System.out.println("python MyBroadcastReceiver.java MyBroadcastReceiver.class onReceive.method: ACTION_BOOT_COMPLETED");
                this.service_start(context, intent);
                break;
            case Intent.ACTION_DELETE:
                System.out.println("python MyBroadcastReceiver.java MyBroadcastReceiver.class onReceive.method: ACTION_DELETE");
                this.service_stop(context, intent);
                break;
            case Intent.ACTION_MAIN:
                System.out.println("python MyBroadcastReceiver.java MyBroadcastReceiver.class onReceive.method: ACTION_MAIN");
                this.start_app(context, intent);
                break;
            default:
               break;
        }
    }
}
