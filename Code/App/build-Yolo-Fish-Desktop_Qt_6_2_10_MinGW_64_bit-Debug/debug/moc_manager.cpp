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
    uint offsetsAndSizes[30];
    char stringdata0[119];
};
#define QT_MOC_LITERAL(ofs, len) \
    uint(sizeof(qt_meta_stringdata_Manager_t::offsetsAndSizes) + ofs), len 
static const qt_meta_stringdata_Manager_t qt_meta_stringdata_Manager = {
    {
        QT_MOC_LITERAL(0, 7),  // "Manager"
        QT_MOC_LITERAL(8, 7),  // "nettete"
        QT_MOC_LITERAL(16, 0),  // ""
        QT_MOC_LITERAL(17, 9),  // "contraste"
        QT_MOC_LITERAL(27, 14),  // "retrodiffusion"
        QT_MOC_LITERAL(42, 15),  // "by_soustraction"
        QT_MOC_LITERAL(58, 4),  // "yolo"
        QT_MOC_LITERAL(63, 6),  // "median"
        QT_MOC_LITERAL(70, 4),  // "path"
        QT_MOC_LITERAL(75, 4),  // "mean"
        QT_MOC_LITERAL(80, 5),  // "histo"
        QT_MOC_LITERAL(86, 5),  // "light"
        QT_MOC_LITERAL(92, 8),  // "proccess"
        QT_MOC_LITERAL(101, 7),  // "program"
        QT_MOC_LITERAL(109, 9)   // "arguments"
    },
    "Manager\0nettete\0\0contraste\0retrodiffusion\0"
    "by_soustraction\0yolo\0median\0path\0mean\0"
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
       1,    0,   74,    2, 0x0a,    1 /* Public */,
       3,    0,   75,    2, 0x0a,    2 /* Public */,
       4,    0,   76,    2, 0x0a,    3 /* Public */,
       5,    0,   77,    2, 0x0a,    4 /* Public */,
       6,    0,   78,    2, 0x0a,    5 /* Public */,
       7,    1,   79,    2, 0x0a,    6 /* Public */,
       9,    1,   82,    2, 0x0a,    8 /* Public */,
      10,    1,   85,    2, 0x0a,   10 /* Public */,
      11,    1,   88,    2, 0x0a,   12 /* Public */,
      12,    2,   91,    2, 0x0a,   14 /* Public */,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QString,    8,
    QMetaType::Void, QMetaType::QString,    8,
    QMetaType::Void, QMetaType::QString,    8,
    QMetaType::Void, QMetaType::QString,    8,
    QMetaType::Void, QMetaType::QString, QMetaType::QStringList,   13,   14,

       0        // eod
};

void Manager::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<Manager *>(_o);
        (void)_t;
        switch (_id) {
        case 0: _t->nettete(); break;
        case 1: _t->contraste(); break;
        case 2: _t->retrodiffusion(); break;
        case 3: _t->by_soustraction(); break;
        case 4: _t->yolo(); break;
        case 5: _t->median((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1]))); break;
        case 6: _t->mean((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1]))); break;
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
, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<QStringList, std::false_type>


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
