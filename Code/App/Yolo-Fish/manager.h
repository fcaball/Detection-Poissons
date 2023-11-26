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
    void nettete();
    void contraste();
    void retrodiffusion();
    void by_soustraction();
    void yolo();
    void median(QString path);
    void mean(QString path);
    void histo(QString path);
    void light(QString path);
    void proccess(QString program, QStringList arguments);

private:
    QObject *findMediaPlayer(QObject *object);
};

#endif // MANAGER_H
