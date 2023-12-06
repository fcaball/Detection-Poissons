/****************************************************************************
** Meta object code from reading C++ file 'manager.h'
**
** Created by: The Qt Meta Object Compiler version 68 (Qt 6.2.10)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../../Yolo-Fish/manager.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'manager.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 68
#error "This file was generated using the moc from 6.2.10. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_Manager_t {
    uint offsetsAndSizes[36];
    char stringdata0[150];
};
#define QT_MOC_LITERAL(ofs, len) \
    uint(sizeof(qt_meta_stringdata_Manager_t::offsetsAndSizes) + ofs), len 
static const qt_meta_stringdata_Manager_t qt_meta_stringdata_Manager = {
    {
        QT_MOC_LITERAL(0, 7),  // "Manager"
        QT_MOC_LITERAL(8, 7),  // "nettete"
        QT_MOC_LITERAL(16, 0),  // ""
        QT_MOC_LITERAL(17, 4),  // "path"
        QT_MOC_LITERAL(22, 9),  // "contraste"
        QT_MOC_LITERAL(32, 14),  // "retrodiffusion"
        QT_MOC_LITERAL(47, 15),  // "by_soustraction"
        QT_MOC_LITERAL(63, 5),  // "seuil"
        QT_MOC_LITERAL(69, 4),  // "yolo"
        QT_MOC_LITERAL(74, 9),  // "nb_epochs"
        QT_MOC_LITERAL(84, 6),  // "median"
        QT_MOC_LITERAL(91, 4),  // "mean"
        QT_MOC_LITERAL(96, 14),  // "taille_fenetre"
        QT_MOC_LITERAL(111, 5),  // "histo"
        QT_MOC_LITERAL(117, 5),  // "light"
        QT_MOC_LITERAL(123, 8),  // "proccess"
        QT_MOC_LITERAL(132, 7),  // "program"
        QT_MOC_LITERAL(140, 9)   // "arguments"
    },
    "Manager\0nettete\0\0path\0contraste\0"
    "retrodiffusion\0by_soustraction\0seuil\0"
    "yolo\0nb_epochs\0median\0mean\0taille_fenetre\0"
    "histo\0light\0proccess\0program\0arguments"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_Manager[] = {

 // content:
      10,       // revision
       0,       // classname
       0,    0, // classinfo
      10,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags, initial metatype offsets
       1,    1,   74,    2, 0x0a,    1 /* Public */,
       4,    0,   77,    2, 0x0a,    3 /* Public */,
       5,    0,   78,    2, 0x0a,    4 /* Public */,
       6,    2,   79,    2, 0x0a,    5 /* Public */,
       8,    2,   84,    2, 0x0a,    8 /* Public */,
      10,    1,   89,    2, 0x0a,   11 /* Public */,
      11,    2,   92,    2, 0x0a,   13 /* Public */,
      13,    1,   97,    2, 0x0a,   16 /* Public */,
      14,    1,  100,    2, 0x0a,   18 /* Public */,
      15,    2,  103,    2, 0x0a,   20 /* Public */,

 // slots: parameters
    QMetaType::Void, QMetaType::QString,    3,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QString, QMetaType::QString,    7,    3,
    QMetaType::Void, QMetaType::QString, QMetaType::QString,    9,    3,
    QMetaType::Void, QMetaType::QString,    3,
    QMetaType::Void, QMetaType::QString, QMetaType::QString,    3,   12,
    QMetaType::Void, QMetaType::QString,    3,
    QMetaType::Void, QMetaType::QString,    3,
    QMetaType::Void, QMetaType::QString, QMetaType::QStringList,   16,   17,

       0        // eod
};

void Manager::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<Manager *>(_o);
        (void)_t;
        switch (_id) {
        case 0: _t->nettete((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1]))); break;
        case 1: _t->contraste(); break;
        case 2: _t->retrodiffusion(); break;
        case 3: _t->by_soustraction((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast< std::add_pointer_t<QString>>(_a[2]))); break;
        case 4: _t->yolo((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast< std::add_pointer_t<QString>>(_a[2]))); break;
        case 5: _t->median((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1]))); break;
        case 6: _t->mean((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast< std::add_pointer_t<QString>>(_a[2]))); break;
        case 7: _t->histo((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1]))); break;
        case 8: _t->light((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1]))); break;
        case 9: _t->proccess((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast< std::add_pointer_t<QStringList>>(_a[2]))); break;
        default: ;
        }
    }
}

const QMetaObject Manager::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_meta_stringdata_Manager.offsetsAndSizes,
    qt_meta_data_Manager,
    qt_static_metacall,
    nullptr,
qt_incomplete_metaTypeArray<qt_meta_stringdata_Manager_t
, QtPrivate::TypeAndForceComplete<Manager, std::true_type>
, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<QStringList, std::false_type>


>,
    nullptr
} };


const QMetaObject *Manager::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Manager::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_Manager.stringdata0))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int Manager::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 10)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 10;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 10)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 10;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
