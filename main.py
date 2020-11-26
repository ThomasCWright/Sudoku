import os
from random import random

from kivy.utils import platform

if platform == 'android':
    from android.permissions import Permission, request_permissions

from jnius import autoclass, cast
from kivy.app import App
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter

class PrintScreen(BoxLayout):
    def build(self):
        pass

class BVWSudoku(App):
    def build(self):
        if platform == 'android':
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE,
                        Permission.READ_EXTERNAL_STORAGE])
        return PrintScreen()

    # def print_canvas(self, obj):
    #     # PrintHelper = autoclass('androidx.print.PrintHelper')
    #     # PrintHelper.printBitmap('jobname','./blank_9x9.png')


    #     # # Context is a normal java class in the Android API
    #     # Context = autoclass('android.content.Context')

    #     # # PythonActivity is provided by the Kivy bootstrap app in python-for-android
    #     # PythonActivity = autoclass("org.kivy.android.PythonActivity")

    #     # # The PythonActivity stores a reference to the currently running activity
    #     # # We need this to access the vibrator service
    #     # activity = PythonActivity.mActivity

    #     # # This is almost identical to the java code for the vibrator
    #     # vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)

    #     # vibrator.vibrate(500)  # The value is in milliseconds - this is 0.5s
    #     if platform == 'android':
    #         path = os.path.join('images','blank_9x9.png')

    #         self.share(path)

    # def share(self,path):
    #     if platform == 'android':
    #         PythonActivity = autoclass('org.kivy.android.PythonActivity')
    #         Intent = autoclass('android.content.Intent')
    #         # String = autoclass('java.lang.String')
    #         Uri = autoclass('android.net.Uri')
    #         File = autoclass('java.io.File')
    #         FileProvider = autoclass('android.support.v4.content.FileProvider')
    #         Context = autoclass("android.content.Context")
    #         # Environment = autoclass("android.os.Environment")

    #         shareIntent = Intent(Intent.ACTION_SEND)
    #         shareIntent.setType('"image/*"')
    #         imageFile = File(path)
    #         # uri = Uri.fromFile(imageFile)

    #         # File imagePath = new File(Context.getFilesDir(), "images");
    #         # File newFile = new File(imagePath, "default_image.jpg");
    #         uri = FileProvider.getUriForFile(Context.getApplicationContext(),"org.test.myapp.fileprovider", imageFile)

    #         parcelable = cast('android.os.Parcelable', uri)
    #         shareIntent.putExtra(Intent.EXTRA_STREAM, parcelable)

    #         currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
    #         currentActivity.startActivity(shareIntent)

if __name__ == '__main__':
    BVWSudoku().run()

# Builds with the following:
# p4a apk --private /mnt/c/Users/tcw25/Documents/GitHub/Sudoku/
#         --package=com.chdirections
#         --name "myapp"
#         --version 0.1
#         --bootstrap=sdl2
#         --requirements=python3,kivy,pyjnius
#         --arch=arm64-v8a
#         --permission VIBRATE
