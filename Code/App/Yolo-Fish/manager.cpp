#include "manager.h"
#include <iostream>
#include <QProcess>
#include <QGuiApplication>
#include <QCursor>
#include <QFileInfo>

#include <QQmlApplicationEngine>
#include <QQmlContext>
Manager::Manager(QGuiApplication *app, QObject *parent)
    : QObject{parent}
{a=app;}

void Manager::nettete() {
    std::cout << "filtre de nettetée" << std::endl;
                                             a->setOverrideCursor(QCursor(Qt::WaitCursor)); // Définir le curseur de chargement


    QString program = "python"; // Chemin vers l'exécutable Python
    QStringList arguments;
    arguments << "../../clean_images.py" << "../Yolo-Fish/yo2.png";

    QProcess *myProcess = new QProcess();
    myProcess->start(program, arguments);

    // Connectez-vous aux signaux de QProcess pour gérer la sortie, les erreurs, etc.
    QObject::connect(myProcess, &QProcess::readyReadStandardOutput, [=]() {
        std::string res = myProcess->readAllStandardOutput().toStdString();
        std::cout << "Output:" << res << std::endl;
    });

    QObject::connect(myProcess, &QProcess::readyReadStandardError, [=]() {
        std::string res1 = myProcess->readAllStandardError().toStdString();
        std::cout << "Error:" << res1 << std::endl;
    });

    // Attendre la fin de l'exécution du script Python
    myProcess->waitForFinished();

    // Récupérer le code de sortie du processus Python
    int exitCode = myProcess->exitCode();
    std::cout << "Process finished with exit code:" << exitCode << std::endl;

    a->restoreOverrideCursor(); // Restaurer le curseur par défaut
    delete myProcess; // Libérez la mémoire du processus

}


void Manager::median(QString path) {
    std::cout << "filtre de nettetée" << std::endl;
                                             a->setOverrideCursor(QCursor(Qt::WaitCursor)); // Définir le curseur de chargement

    QFileInfo fileInfo(path);
    QString directory = fileInfo.path();
    directory.append("/");
    QString testD=directory;
    if (testD.remove(0, 7) == "file://") {
        directory = directory.remove(0,8);
    }
    std::cout<<directory.toStdString()<<std::endl;

    QString program = "python"; // Chemin vers l'exécutable Python
    QStringList arguments;
    arguments << "../../clean_images.py" <<"median"<<directory<< path;
    proccess(program,arguments);


}

void Manager::mean(QString path)
{
    std::cout << "filtre de nettetée" << std::endl;
    a->setOverrideCursor(QCursor(Qt::WaitCursor)); // Définir le curseur de chargement
    path[0]='C';
    std::cout<<path.toStdString()<<std::endl;
    QFileInfo fileInfo(path);
    QString directory = fileInfo.path();
    directory.append("/");
    QString testD=directory;
    if (testD.remove(0, 7) == "file://") {
        directory = directory.remove(0,8);
    }

    std::cout<<directory.toStdString()<<std::endl;

    QString program = "python"; // Chemin vers l'exécutable Python
    QStringList arguments;
    arguments << "../../clean_images.py" <<"mean"<<directory<< path;
    proccess(program,arguments);


}

void Manager::histo(QString path)
{
    std::cout << "filtre de nettetée" << std::endl;
                                             a->setOverrideCursor(QCursor(Qt::WaitCursor)); // Définir le curseur de chargement

    QFileInfo fileInfo(path);
    QString directory = fileInfo.path();
    directory.append("/");
    QString testD=directory;
    if (testD.remove(0, 7) == "file://") {
        directory = directory.remove(0,8);
    }
    std::cout<<directory.toStdString()<<std::endl;

    QString program = "python"; // Chemin vers l'exécutable Python
    QStringList arguments;
    arguments << "../../clean_images.py" <<"histo"<<directory<< path;
    proccess(program,arguments);

}

void Manager::light(QString path)
{
    std::cout << "filtre de nettetée" << std::endl;
                                             a->setOverrideCursor(QCursor(Qt::WaitCursor)); // Définir le curseur de chargement


    QFileInfo fileInfo(path);
    QString directory = fileInfo.path();
    directory.append("/");
    QString testD=directory;
    if (testD.remove(0, 7) == "file://") {
        directory = directory.remove(0,8);
    }

    std::cout<<directory.toStdString()<<std::endl;

    QString program = "python"; // Chemin vers l'exécutable Python
    QStringList arguments;
    arguments << "../../clean_images.py" <<"light"<<directory<< path;

    proccess(program,arguments);


}

void Manager::proccess(QString program, QStringList arguments)
{
    QProcess *myProcess = new QProcess();
    myProcess->start(program, arguments);


    // Connectez-vous aux signaux de QProcess pour gérer la sortie, les erreurs, etc.
    QObject::connect(myProcess, &QProcess::readyReadStandardOutput, [=]() {
        std::string res = myProcess->readAllStandardOutput().toStdString();
        std::cout << "Output:" << res << std::endl;
    });

    QObject::connect(myProcess, &QProcess::readyReadStandardError, [=]() {
        std::string res1 = myProcess->readAllStandardError().toStdString();
        std::cout << "Error:" << res1 << std::endl;
    });

    // Attendre la fin de l'exécution du script Python
    myProcess->waitForFinished();

    // Récupérer le code de sortie du processus Python
    int exitCode = myProcess->exitCode();
    std::cout << "Process finished with exit code:" << exitCode << std::endl;

    a->restoreOverrideCursor(); // Restaurer le curseur par défaut
    delete myProcess; // Libérez la mémoire du processus


}



void Manager::contraste()
{
    std::cout << "filtre de contraste" << std::endl;

}

void Manager::retrodiffusion()
{
    std::cout << "filtre de retrodiffusion" << std::endl;
}

void Manager::by_soustraction()
{
    std::cout << "méthode by_soustraction" << std::endl;

}

void Manager::yolo()
{
    std::cout << "méthode yolo" << std::endl;

}
