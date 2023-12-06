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
        source: "file:///C:/Users/fabien/Documents/M2/Projet-Image/Detection-Poissons/Code/App/Yolo-Fish/backgroundApp.png"
    }
    Popup {
        id: popup2
        width: 200
        height: 150
        visible: false
        anchors.centerIn: parent
        Column {
            anchors.centerIn: parent
            spacing: 10 // Ajoute un espacement de 10 pixels entre chaque élément
            padding: 50


            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: 15
                text: qsTr("Enter the desire threshold")
            }

            TextField {
                  id: numberInput
                  width: 80
                  anchors.horizontalCenter: parent.horizontalCenter

                  placeholderText: "Threshold"
                  validator: IntValidator { bottom: -100; top: 100 } // Limite le champ aux nombres entre -100 et 100
                  onAccepted: {
                      console.log(":",)
                  }
              }


            Button {
                text: "Submit"
                anchors.horizontalCenter: parent.horizontalCenter
                onClicked: {
                    var source = mediaPlayer.source.toString() // Contenu de la propriété source

                    // Extraction du répertoire à partir de la propriété source
                    if (source.substring(0, 7) === "file://") {
                        source = source.substring(8)
                    }
                    var directory = source.substring(0, source.lastIndexOf("/"))
                    directory[0]='C'

                    manager.by_soustraction(numberInput.text,mediaPlayer.source)
                    directory+="/output_without_dl.mp4"

                    mediaPlayer.source=directory
                    mediaPlayer.play()
                    popup2.close()
                }
            }
        }

    }


    Popup {
        id: popup
        width: 200
        height: 150
        visible: false
        anchors.centerIn: parent
        Column {
            anchors.centerIn: parent
            spacing: 10 // Ajoute un espacement de 10 pixels entre chaque élément
            padding: 50

            RadioButton {
                id: option1
                text: "10 Epochs"
                checked: true
            }
            RadioButton {
                id: option2
                text: "20 Epochs"
            }
            RadioButton {
                id: option3
                text: "50 Epochs"
            }
            RadioButton {
                id: option4
                text: "100 Epochs"
            }


            Button {
                text: "Submit"
                onClicked: {
                    var source = mediaPlayer.source.toString() // Contenu de la propriété source

                    // Extraction du répertoire à partir de la propriété source
                    if (source.substring(0, 7) === "file://") {
                        source = source.substring(8)
                    }
                    var directory = source.substring(0, source.lastIndexOf("/"))
                    directory[0]='C'


                    if (option1.checked) {
                        manager.yolo("10",mediaPlayer.source)
                        directory+="/output_predict_10.mp4"

                    } else if (option2.checked) {
                        manager.yolo("20",mediaPlayer.source)
                        directory+="/output_predict_20.mp4"

                    } else if (option3.checked) {
                        manager.yolo("50",mediaPlayer.source)
                        directory+="/output_predict_50.mp4"

                    } else if (option4.checked) {
                        manager.yolo("100",mediaPlayer.source)
                        directory+="/output_predict_100.mp4"

                    }

                    mediaPlayer.source=directory
                    mediaPlayer.play()
                    popup.close()
                }
            }
        }

    }



    Popup {
        id: popupMean
        width: 200
        height: 150
        visible: false
        anchors.centerIn: parent
        Column {
            anchors.centerIn: parent
            spacing: 10 // Ajoute un espacement de 10 pixels entre chaque élément
            padding: 50

            RadioButton {
                id: option1mean
                text: "3x3 filter window"
                checked: true
            }
            RadioButton {
                id: option2mean
                text: "5x5 filter window"
            }
            RadioButton {
                id: option3mean
                text: "11x11 filter window"
            }


            // Ajout d'un Item pour créer un espace vertical supplémentaire


            Button {
                text: "Submit"
                onClicked: {
                    var source = mediaPlayer.source.toString() // Contenu de la propriété source



                    if (option1mean.checked) {
                        manager.mean(mediaPlayer.source,"3")

                    } else if (option2mean.checked) {
                        manager.mean(mediaPlayer.source,"5")

                    } else if (option3mean.checked) {
                        manager.mean(mediaPlayer.source,"11")
                    }

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
                    popupMean.close()
                }
            }
        }

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
                  popupMean.open()
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
                    manager.nettete(mediaPlayer.source) // Émettre le signal
                    var source = mediaPlayer.source.toString() // Contenu de la propriété source

                    // Extraction du répertoire à partir de la propriété source
                    if (source.substring(0, 7) === "file://") {
                        source = source.substring(8)
                    }
                    var directory = source.substring(0, source.lastIndexOf("/"))
                    directory[0]='C'
                    directory+="/nettete_output_video.mp4"
                    console.log(directory)

                    mediaPlayer.source=directory
                    mediaPlayer.play()
                }
            }

            // MenuItem { text: "Rétro diffusion"
            //     background: Rectangle {
            //         border.color: "#0083ff"
            //         color: "#009edf"
            //     }
            //     onClicked: {
            //         manager.retrodiffusion() // Émettre le signal
            //     }
            // }
        }
        Menu {
            title: "Without Deep learning"
            MenuItem { text: "By soustraction"

                background: Rectangle {
                    border.color: "#0083ff"
                    color: "#009edf"
                }
                onClicked: {

                    popup2.open()


                }
            }
        }

        Menu {
            title: "With Deep learning"
            MenuItem { text: "test Yolo"
                background: Rectangle {
                    border.color: "#0083ff"
                    color: "#009edf"
                }
                onClicked: {
                    popup.open()
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
