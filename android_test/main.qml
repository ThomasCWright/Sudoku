import QtQuick 2.12
import QtQuick.Window 2.12


Window {
        //@disable-check M16
        width: 640
        //@disable-check M16
        height: 480
        //@disable-check M16
        visible: true
        //@disable-check M16
        title: qsTr("Tabs")

    property alias mainWindow: mainWindow
    property alias bubble: bubble
    Rectangle {
        id: mainWindow
        visible: true
        color: "#ffffff"
        anchors.fill: parent

        Image {
            id: bubble
            x: 8
            y: 8
            source: "Bluebubble.svg"
            sourceSize.width: 182
            cache: false
            fillMode: Image.PreserveAspectFit
        }
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
