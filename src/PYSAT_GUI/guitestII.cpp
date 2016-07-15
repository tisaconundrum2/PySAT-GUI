#include "guitest.h"
#include "ui_guitest.h"
#include <QString>
#include <QFile>
#include <QDir>
#include <QMessageBox>
#include <QFileDialog>
#include <QDebug>
#include <QRect>
#include <QDesktopWidget>
#include <QSignalMapper>
#include <QFile>
#include <QTextStream>


int isNormalizationFilled = 0;
int isSpinBoxFilled = 0;
int normalizationBtnCnt = 0;
int normalizationSize = 0;
int spinArray[16] = {0,0,0,0,
                     0,0,0,0,
                     0,0,0,0};

