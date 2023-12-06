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

void Manager::nettete(QString path) {
    std::cout << "filtre de nettetée" << std::endl;
                                             a->setOverrideCursor(QCursor(Qt::WaitCursor)); // Définir le curseur de chargement

    QFileInfo fileInfo(path);
    QString directory = fileInfo.path();
    directory.append("/");
    QString testD=directory;
    if (testD.remove(0, 7).compare("file://")) {

        directory = directory.remove(0,8);
    }
    std::cout<<directory.toStdString()<<std::endl;

    QString program = "python"; // Chemin vers l'exécutable Python
    QStringList arguments;
    arguments << "../../clean_images.py" <<"nettete"<<directory<< path;
    proccess(program,arguments);


}


void Manager::median(QString path) {
    std::cout << "filtre de nettetée" << std::endl;
                                             a->setOverrideCursor(QCursor(Qt::WaitCursor)); // Définir le curseur de chargement

    QFileInfo fileInfo(path);
    QString directory = fileInfo.path();
    directory.append("/");
    QString testD=directory;
    if (testD.remove(0, 7).compare("file://")) {

        directory = directory.remove(0,8);
    }
    std::cout<<directory.toStdString()<<std::endl;

    QString program = "python"; // Chemin vers l'exécutable Python
    QStringList arguments;
    arguments << "../../clean_images.py" <<"median"<<directory<< path;
    proccess(program,arguments);


}

void Manager::mean(QString path,QString taille_fenetre)
{
    std::cout << "filtre de nettetée" << std::endl;
    a->setOverrideCursor(QCursor(Qt::WaitCursor)); // Définir le curseur de chargement
    std::cout<<path.toStdString()<<std::endl;
    QFileInfo fileInfo(path);
    QString directory = fileInfo.path();
    directory.append("/");
    QString testD=directory;
    if (testD.remove(0, 7).compare("file://")) {
        directory = directory.remove(0,8);
    }
    directory[0]='C';

    std::cout<<directory.toStdString()<<std::endl;

    QString program = "python"; // Chemin vers l'exécutable Python
    QStringList arguments;
    arguments << "../../clean_images.py" <<"mean"<<directory<< path<<taille_fenetre;
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
    if (testD.remove(0, 7).compare("file://")) {
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
    if (testD.remove(0, 7).compare("file://")) {
        directory = directory.remove(0,8);
    }

    std::cout<<directory.toStdString()<<std::endl;
    std::cout<<path.toStdString()<<std::endl;

    QString program = "python"; // Chemin vers l'exécutable Python
    QStringList arguments;
    arguments << "../../clean_images.py" <<"light"<<directory<< path;

    proccess(program,arguments);
}

void Manager::proccess(QString program, QStringList arguments)
{
    QProcess *myProcess = new QProcess();
    connect(myProcess, &QProcess::finished, [=](int exitCode, QProcess::ExitStatus exitStatus){
        // Gérer la fin du processus ici
        // Par exemple, nettoyer et détruire le QProcess ici
        myProcess->deleteLater();
    });
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
    if (!myProcess->waitForFinished(-1)) {
        // Le processus n'a pas pu se terminer
    }
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

void Manager::by_soustraction(QString seuil, QString path)
{
    std::cout << "méthode by_soustraction" << std::endl;

                                                      a->setOverrideCursor(QCursor(Qt::WaitCursor)); // Définir le curseur de chargement


    QFileInfo fileInfo(path);
    QString directory = fileInfo.path();
    directory.append("/");
    QString testD=directory;
    if (testD.remove(0, 7).compare("file://")) {
        directory = directory.remove(0,8);
    }

    std::cout<<directory.toStdString()<<std::endl;
    std::cout<<path.toStdString()<<std::endl;

    QString program = "python";
    QStringList arguments;
    arguments << "../../without_dl.py" <<path<<directory<<seuil;

    proccess(program,arguments);



}

void Manager::yolo(QString nb_epochs, QString path)
{
    std::cout << "méthode yolo" << std::endl;
                                       a->setOverrideCursor(QCursor(Qt::WaitCursor)); // Définir le curseur de chargement


    QFileInfo fileInfo(path);
    QString directory = fileInfo.path();
    directory.append("/");
    QString testD=directory;
    if (testD.remove(0, 7).compare("file://")) {
        directory = directory.remove(0,8);
    }

    std::cout<<directory.toStdString()<<std::endl;
    std::cout<<path.toStdString()<<std::endl;

    QString program = "python"; // Chemin vers l'exécutable Python
    QStringList arguments;
    arguments << "../../predict.py" <<nb_epochs<<path<<directory;

    proccess(program,arguments);


}
