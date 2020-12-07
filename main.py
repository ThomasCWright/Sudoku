import os
from random import random

from kivy.utils import platform

if platform == 'android':
    from android.permissions import Permission, request_permissions
    from android.storage import primary_external_storage_path


from jnius import autoclass, cast
from kivy.app import App
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget


class PrintScreen(BoxLayout):

    def build(self):
        pass

    def print(self):
        if platform == 'android':
            # path = os.path.join(self.ids.fc.path, self.ids.fc.selection[0])

            path = os.path.abspath(self.ids.im.source)
            path = self.copy_to_external_storage(path)
            AndroidOSVERSION = autoclass('android.os.Build$VERSION')
            print(f"sharing file path: {path}\nAPI={AndroidOSVERSION.SDK_INT}")
            self.share(path)

    def copy_to_external_storage(self,path):
        if platform == 'android':
            Environment = autoclass('android.os.Environment')
            FileOutputStream = autoclass('java.io.FileOutputStream')
            FileInputStream = autoclass('java.io.FileInputStream')

            rootpath = Environment.getExternalStorageDirectory().getAbsolutePath()
            File = autoclass('java.io.File')

            dstFile = File(os.path.join(rootpath,os.path.basename(path)))
            srcFile = File(os.path.abspath(path))
            if dstFile.exists():
                return dstFile.toURI()
            else:
                dstFile.createNewFile()

            print(f"File to new dst: {dstFile.toURI()}")

            source = FileInputStream(srcFile)
            destination = FileOutputStream(dstFile)

            b = bytearray

            print(f"Source available = {source.available()}")

            while source.available() > 0:
                b = source.read()
                destination.write(b)

            source.close()
            destination.close()

            return dstFile.toURI()

    def share(self,path):
        if platform == 'android':
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            File = autoclass('java.io.File')
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setType("image/*")
            uri = Uri.fromFile(File(path))
            parcelable = cast('android.os.Parcelable', uri)
            intent.putExtra(Intent.EXTRA_STREAM, parcelable)

            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            self.context = cast('android.content.ContextWrapper', currentActivity.getApplicationContext())

            if intent.resolveActivity(self.context.getPackageManager()) != None:
                currentActivity.startActivity(intent)

class BVWSudoku(App):
    def build(self):
        if platform == 'android':
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE,
                        Permission.READ_EXTERNAL_STORAGE])
        return PrintScreen()

if __name__ == '__main__':
    BVWSudoku().run()

