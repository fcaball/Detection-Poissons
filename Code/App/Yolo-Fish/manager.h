#ifndef MANAGER_H
#define MANAGER_H

#include <QObject>
#include <QGuiApplication>
#include <QString>

class Manager : public QObject
{
    Q_OBJECT
public:
    QGuiApplication *a;
    explicit Manager(QGuiApplication *app, QObject *parent = nullptr);

signals:

public slots:
    void nettete(QString path);
    void contraste();
    void retrodiffusion();
    void by_soustraction(QString seuil,QString path);
    void yolo(QString nb_epochs, QString path);
    void median(QString path);
    void mean(QString path, QString taille_fenetre);
    void histo(QString path);
    void light(QString path);
    void proccess(QString program, QStringList arguments);

private:
    QObject *findMediaPlayer(QObject *object);
};

#endif // MANAGER_H
