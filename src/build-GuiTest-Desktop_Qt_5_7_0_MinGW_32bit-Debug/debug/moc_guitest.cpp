/****************************************************************************
** Meta object code from reading C++ file 'guitest.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.7.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../PYSAT_GUI/guitest.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'guitest.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.7.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
struct qt_meta_stringdata_GuiTest_t {
    QByteArrayData data[17];
    char stringdata0[305];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_GuiTest_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_GuiTest_t qt_meta_stringdata_GuiTest = {
    {
QT_MOC_LITERAL(0, 0, 7), // "GuiTest"
QT_MOC_LITERAL(1, 8, 21), // "on_toolButton_clicked"
QT_MOC_LITERAL(2, 30, 0), // ""
QT_MOC_LITERAL(3, 31, 23), // "on_toolButton_2_clicked"
QT_MOC_LITERAL(4, 55, 23), // "on_toolButton_3_clicked"
QT_MOC_LITERAL(5, 79, 23), // "on_toolButton_4_clicked"
QT_MOC_LITERAL(6, 103, 23), // "on_actionExit_triggered"
QT_MOC_LITERAL(7, 127, 24), // "on_pushButton_13_clicked"
QT_MOC_LITERAL(8, 152, 21), // "on_pushButton_clicked"
QT_MOC_LITERAL(9, 174, 16), // "setLabelsVisible"
QT_MOC_LITERAL(10, 191, 1), // "i"
QT_MOC_LITERAL(11, 193, 7), // "visible"
QT_MOC_LITERAL(12, 201, 19), // "setSpinrightVisible"
QT_MOC_LITERAL(13, 221, 18), // "setSpinleftVisible"
QT_MOC_LITERAL(14, 240, 30), // "on_norm_spinBox_9_valueChanged"
QT_MOC_LITERAL(15, 271, 4), // "arg1"
QT_MOC_LITERAL(16, 276, 28) // "on_norm_spinBox_valueChanged"

    },
    "GuiTest\0on_toolButton_clicked\0\0"
    "on_toolButton_2_clicked\0on_toolButton_3_clicked\0"
    "on_toolButton_4_clicked\0on_actionExit_triggered\0"
    "on_pushButton_13_clicked\0on_pushButton_clicked\0"
    "setLabelsVisible\0i\0visible\0"
    "setSpinrightVisible\0setSpinleftVisible\0"
    "on_norm_spinBox_9_valueChanged\0arg1\0"
    "on_norm_spinBox_valueChanged"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_GuiTest[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
      12,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    0,   74,    2, 0x08 /* Private */,
       3,    0,   75,    2, 0x08 /* Private */,
       4,    0,   76,    2, 0x08 /* Private */,
       5,    0,   77,    2, 0x08 /* Private */,
       6,    0,   78,    2, 0x08 /* Private */,
       7,    0,   79,    2, 0x08 /* Private */,
       8,    0,   80,    2, 0x08 /* Private */,
       9,    2,   81,    2, 0x08 /* Private */,
      12,    2,   86,    2, 0x08 /* Private */,
      13,    2,   91,    2, 0x08 /* Private */,
      14,    1,   96,    2, 0x08 /* Private */,
      16,    1,   99,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int, QMetaType::Bool,   10,   11,
    QMetaType::Void, QMetaType::Int, QMetaType::Bool,   10,   11,
    QMetaType::Void, QMetaType::Int, QMetaType::Bool,   10,   11,
    QMetaType::Void, QMetaType::Int,   15,
    QMetaType::Void, QMetaType::Int,   15,

       0        // eod
};

void GuiTest::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        GuiTest *_t = static_cast<GuiTest *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->on_toolButton_clicked(); break;
        case 1: _t->on_toolButton_2_clicked(); break;
        case 2: _t->on_toolButton_3_clicked(); break;
        case 3: _t->on_toolButton_4_clicked(); break;
        case 4: _t->on_actionExit_triggered(); break;
        case 5: _t->on_pushButton_13_clicked(); break;
        case 6: _t->on_pushButton_clicked(); break;
        case 7: _t->setLabelsVisible((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 8: _t->setSpinrightVisible((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 9: _t->setSpinleftVisible((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 10: _t->on_norm_spinBox_9_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 11: _t->on_norm_spinBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObject GuiTest::staticMetaObject = {
    { &QMainWindow::staticMetaObject, qt_meta_stringdata_GuiTest.data,
      qt_meta_data_GuiTest,  qt_static_metacall, Q_NULLPTR, Q_NULLPTR}
};


const QMetaObject *GuiTest::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *GuiTest::qt_metacast(const char *_clname)
{
    if (!_clname) return Q_NULLPTR;
    if (!strcmp(_clname, qt_meta_stringdata_GuiTest.stringdata0))
        return static_cast<void*>(const_cast< GuiTest*>(this));
    return QMainWindow::qt_metacast(_clname);
}

int GuiTest::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 12)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 12;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 12)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 12;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
