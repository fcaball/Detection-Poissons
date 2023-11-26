#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include "manager.h" // Assurez-vous d'inclure votre fichier manager.h ici

int main(int argc, char *argv[]) {
    QGuiApplication app(argc, argv);

    Manager manager(&app); // Créez une instance de Manager

    // Enregistrez la classe Manager pour être accessible depuis QML
    qmlRegisterType<Manager>("MyCustomQMLObjects", 2, 35, "Manager");

    // Créez le moteur QML
    QQmlApplicationEngine engine;

    // Exposez votre instance Manager au contexte QML
    engine.rootContext()->setContextProperty("manager", &manager);

    // Chargez votre fichier QML
    engine.load(QUrl(QStringLiteral("file:///C:/Users/fabien/Documents/M2/Projet-Image/Detection-Poissons/Code/App/Yolo-Fish/main.qml"))); // Assurez-vous de mettre le bon chemin vers votre fichier QML

    if (engine.rootObjects().isEmpty()) {
        return -1;
    }

    return app.exec();
}
