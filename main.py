from random import random
from jnius import cast, autoclass
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

from android.permissions import request_permissions, Permission

class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):

    def build(self):
        request_permissions([Permission.WRITE_EXTERNAL_STORAGE,
                     Permission.READ_EXTERNAL_STORAGE])

        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Print')
        clearbtn.bind(on_release=self.print_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def print_canvas(self, obj):
        # PrintHelper = autoclass('androidx.print.PrintHelper')
        # PrintHelper.printBitmap('jobname','./blank_9x9.png')


        # # Context is a normal java class in the Android API
        # Context = autoclass('android.content.Context')

        # # PythonActivity is provided by the Kivy bootstrap app in python-for-android
        # PythonActivity = autoclass("org.kivy.android.PythonActivity")

        # # The PythonActivity stores a reference to the currently running activity
        # # We need this to access the vibrator service
        # activity = PythonActivity.mActivity

        # # This is almost identical to the java code for the vibrator
        # vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)

        # vibrator.vibrate(500)  # The value is in milliseconds - this is 0.5s

        self.share('./blank_9x9.png')

    def share(self,path):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        String = autoclass('java.lang.String')
        Uri = autoclass('android.net.Uri')
        File = autoclass('java.io.File')

        shareIntent = Intent(Intent.ACTION_SEND)
        shareIntent.setType('"image/*"')
        imageFile = File(path)
        uri = Uri.fromFile(imageFile)

        # File imagePath = new File(Context.getFilesDir(), "images");
        # File newFile = new File(imagePath, "default_image.jpg");
        # uri = Uri.getUriForFile(getContext(), "com.mydomain.fileprovider", newFile)


        parcelable = cast('android.os.Parcelable', uri)
        shareIntent.putExtra(Intent.EXTRA_STREAM, parcelable)

        currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        currentActivity.startActivity(shareIntent)

if __name__ == '__main__':
    MyPaintApp().run()

# Builds with the following:
# p4a apk --private /mnt/c/Users/tcw25/Documents/GitHub/Sudoku/
#         --package=com.chdirections
#         --name "myapp"
#         --version 0.1
#         --bootstrap=sdl2
#         --requirements=python3,kivy,pyjnius
#         --arch=arm64-v8a
#         --permission VIBRATE