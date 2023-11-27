import QtQuick 2.15
import QtQuick.Window
import QtQuick.Controls 2.15
import QtMultimedia
import QtQuick.Controls
import QtQuick.Dialogs
import Qt.labs.folderlistmodel
import MyCustomQMLObjects 2.35

Window {
    id:rootItem
    visible: true
    width: 640
    height: 480
    title: qsTr("Yolo Fish Application")


    Image {
        id:background
        anchors.fill: parent
        source: "file:///C:/Users/fabien/Desktop/App/Yolo-Fish/backgroundApp.png"

    }

    Component.onCompleted: {
        visibility = Window.Maximized;
    }

    MenuBar {

        Menu {
            title: "Preprocessing"

            MenuItem {
                text: "Median filter"
                background: Rectangle {
                    border.color: "#0083ff"
                    color: "#009edf"
                }


                onClicked: {
                    manager.median(mediaPlayer.source) // Émettre le signal
                    var source = mediaPlayer.source.toString() // Contenu de la propriété source

                    // Extraction du répertoire à partir de la propriété source
                    if (source.substring(0, 7) === "file://") {
                        source = source.substring(8)
                    }
                    var directory = source.substring(0, source.lastIndexOf("/"))
                    directory[0]='C'
                    directory+="/median_output_video.mp4"

                    mediaPlayer.source=directory
                    mediaPlayer.play()
                }
            }

            MenuItem {
                text: "Mean filter"
                background: Rectangle {
                    border.color: "#0083ff"
                    color: "#009edf"
                }

                onClicked: {
                    manager.mean(mediaPlayer.source) // Émettre le signal
                    var source = mediaPlayer.source.toString() // Contenu de la propriété source

                    // Extraction du répertoire à partir de la propriété source
                    if (source.substring(0, 7) === "file://") {
                        source = source.substring(8)
                    }
                    var directory = source.substring(0, source.lastIndexOf("/"))
                    directory[0]='C'
                    directory+="/mean_output_video.mp4"
                    console.log(directory)

                    mediaPlayer.source=directory
                    mediaPlayer.play()
                }
            }

            MenuItem {
                text: "Histogram filter"
                background: Rectangle {
                    border.color: "#0083ff"
                    color: "#009edf"
                }

                onClicked: {
                    manager.histo(mediaPlayer.source) // Émettre le signal
                    var source = mediaPlayer.source.toString() // Contenu de la propriété source

                    // Extraction du répertoire à partir de la propriété source
                    if (source.substring(0, 7) === "file://") {
                        source = source.substring(8)
                    }
                    var directory = source.substring(0, source.lastIndexOf("/"))
                    directory[0]='C'
                    directory+="/histo_output_video.mp4"
                    console.log(directory)

                    mediaPlayer.source=directory
                    mediaPlayer.play()
                }
            }

            MenuItem {
                text: "Light filter"
                background: Rectangle {
                    border.color: "#0083ff"
                    color: "#009edf"
                }

                onClicked: {
                    manager.light(mediaPlayer.source) // Émettre le signal
                    var source = mediaPlayer.source.toString() // Contenu de la propriété source

                    // Extraction du répertoire à partir de la propriété source
                    if (source.substring(0, 7) === "file://") {
                        source = source.substring(8)
                    }
                    var directory = source.substring(0, source.lastIndexOf("/"))
                    directory[0]='C'
                    directory+="/light_output_video.mp4"
                    console.log(directory)

                    mediaPlayer.source=directory
                    mediaPlayer.play()
                }
            }

            MenuItem {
                text: "Netteté"
                background: Rectangle {
                    border.color: "#0083ff"
                    color: "#009edf"
                }

                onClicked: {
                    manager.nettete() // Émettre le signal
                }
            }

            MenuItem { text: "Contraste"
                background: Rectangle {
                    border.color: "#0083ff"
                    color: "#009edf"
                }
                onClicked: {
                    manager.contraste() // Émettre le signal
                }
            }

            MenuItem { text: "Rétro diffusion"
                background: Rectangle {
                    border.color: "#0083ff"
                    color: "#009edf"
                }
                onClicked: {
                    manager.retrodiffusion() // Émettre le signal
                }
            }
        }
        Menu {
            title: "Without Deep learning"
            MenuItem { text: "By soustraction"

                background: Rectangle {
                    border.color: "#0083ff"
                    color: "#009edf"
                }
                onClicked: {
                    manager.by_soustraction() // Émettre le signal
                }
            }

        }

        Menu {
            title: "With Deep learning"
            MenuItem { text: "Yolo"
                background: Rectangle {
                    border.color: "#0083ff"
                    color: "#009edf"
                }
                onClicked: {
                    manager.yolo() // Émettre le signal
                }
            }

        }
        background: Rectangle {
            border.color: "#0083ff"
            color: "#00bcff"
        }
    }

    Rectangle {
        width: parent.width - 40
        height: parent.height - 40
        anchors.centerIn: parent
        color: "transparent"

        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: 30
            text: qsTr("YOLO FISH")
        }

        Button {
            id:importButton
            width: 100
            height: 100
            text: "IMPORT"
            anchors.left: parent.left
            anchors.leftMargin: 100
            anchors.verticalCenter: parent.verticalCenter
            onClicked: {
                openFile.open();
            }
        }

        Rectangle {
            id:contentVideo
            width: 800
            height: 600
            color: "black"
            anchors.centerIn: parent

            MediaPlayer {
                id: mediaPlayer
                videoOutput: videoOutput
                loops: MediaPlayer.Infinite
            }

            VideoOutput {
                id: videoOutput
                anchors.fill: parent

            }
        }
        FileDialog {
            id: openFile
            title: "Choisir une vidéo"

            nameFilters: ["Vidéos (*.mp4 *.avi)", "Tous les fichiers (*)"]
            onAccepted: {
                console.log("File accepted: " + openFile.selectedFile);
                mediaPlayer.source = openFile.selectedFile;
                mediaPlayer.play();
            }
        }


        Button {
            text: mediaPlayer.playbackState === MediaPlayer.PlayingState ? "Pause" : "Play"
            height: 50
            width: 100
            anchors {
                bottom: parent.bottom
                // bottomMargin: 50 // Ajoute de la marge en bas
                horizontalCenter: parent.horizontalCenter
            }

            background: Rectangle {

                color:"#0078d7"
                radius: 5
            }

            onClicked: {
                if (mediaPlayer.playbackState === MediaPlayer.PlayingState) {
                    mediaPlayer.pause();
                } else {
                    mediaPlayer.play();
                }
            }
        }





    }
}
