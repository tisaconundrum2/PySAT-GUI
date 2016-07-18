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


int normSize = 0,
normPushValue = 0,
isNormFilled = 0,
isSpinBoxFilled = 0,
normalizationBtnCnt = 0,
spinArray[16] = {0,0,0,0,
                 0,0,0,0,
                 0,0,0,0};

QString pythonProgrmaFile = "";
QString outputDirectory = "";
QFile file("pls_sm_output.py");
QTextStream output(&file);

GuiTest::GuiTest (QWidget *parent){
    QMainWindow(parent), ui(new Ui::GuiTest){
        ui->setupUi(this);
        setSizeOfWindow();
        setQSpinWidgets();
        setOutputFile();
    }
}

GuiTest::~GuiTest()(){
    delete ui;
}

void setSizeOfWindow(){
    QRect currentWindowSize = QApplication::desktop()->screenGeometry();
    int height = currentWindowSize.height();
    this->resize(this->width(), height*0.9);
    for (int i = 0; i < norm_size; i++){        //setting up visibility
        setSpinleftVisible(i, false);
        setSpinrightVisible(i, false);
        setLabelsVisible(i, false);
    }
}

void GuiTest::setupQSpinWidgets(){
    QList<QSpinBox*> allChildSpinBoxes = findChildren<QSpinBox*>();
    QSignalMapper* signalMapper = new QSignalMapper(this);
    QSpinBox oneChildSpinbox;
    foreach(oneChildSpinbox, allChildSpinBoxes){
        connect(oneChildSpinbox, SIGNAL(valueChanged(int)), signalMapper, SLOT(map()));
        signalMapper->setMapping(oneChildSpinbox, oneChildSpinbox);
    }
    connect(signalMapper, SIGNAL(mapped(QWidget*)), this, SLOT(getSpinboxValue(QWidget*)));
}

void GuiTest::SetupOutFile(){
    file.open(QIODevice::WriteOnly | QIODevice::Text);
    QTextStream output(&file);
    output << "from pysat.spectral.spectral_data import spectral_data\n";
    output << "from pysat.regression.pls_sm import pls_sm\n";
    output << "import pandas as pd\n";
}

void GuiTest::setLabelAndSpinVisible(int index, bool visible){
    int arraySize = 7;
    QLabel* labels[arraySize] = {ui->norm_label_2,
                                 ui->norm_label_3,
                                 ui->norm_label_4,
                                 ui->norm_label_5,
                                 ui->norm_label_6,
                                 ui->norm_label_7,
                                 ui->norm_label_8};
    QSpinBox* spinBoxR[arraySize] = {ui->norm_spinBox_2,
                                     ui->norm_spinBox_3,
                                     ui->norm_spinBox_4,
                                     ui->norm_spinBox_5,
                                     ui->norm_spinBox_6,
                                     ui->norm_spinBox_7,
                                     ui->norm_spinBox_8};
    QSpinBox* spinBoxL[arraySize] = {ui->norm_spinBox_10,
                                     ui->norm_spinBox_11,
                                     ui->norm_spinBox_12,
                                     ui->norm_spinBox_13,
                                     ui->norm_spinBox_14,
                                     ui->norm_spinBox_15,
                                     ui->norm_spinBox_16
                                    };
    labels[index]->setVisible(visible);
    spinBoxL[index]->setVisible(visible);
    spinBoxR[index]->setVisible(visible);
}

void GuiTest::on_maskFileButton_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Maskfile", QDir::homePath());
    ui->lineEdit->setText(file_name);
    out << "maskfile = \"" << file_name << "\"\n";
    isNormFilled++;
}

void GuiTest::on_unknownDataButton_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Unknwon Data File", QDir::homePath());
    ui->lineEdit_2->setText(file_name);
    out << "unknowndatacsv = \"" << file_name << "\"\n";
    isNormFilled++;
}

void GuiTest::on_fullDataBaseButton_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Database File", QDir::homePath());
    ui->lineEdit_3->setText(file_name);
    out << "db = \"" << file_name << "\"\n";
    isNormFilled++;
}

void GuiTest::on_outPutLocation_clicked(){
    output_location = QFileDialog::getExistingDirectory(this, "Select Output Directory", QDir::homePath());
    ui->lineEdit_4->setText(output_location);
    out << "outpath = \"" << output_location << "\"\n";
    isNormFilled++;
}

void GuiTest::on_pythonButton_clicked(){
    python_file = QFileDialog::getOpenFileName(this, "Python .exe File", QDir::rootPath());
    ui->lineEdit_6->setText(python_file);
}

void GuiTest::on_NormAddValuebutton_clicked(){
    if (normPushValue >= normSize){
        QMessageBox::critical(this, "Warning", "Cannot add anymore values");
    } else {
        setLabelAndSpinVisible(normPushValue, true);
        normPushValue++;
    }
}

int GuiTest::getSpinValue(){
    QSpinBox* spinValue = (QSpinBox*)widgetSpinValue;
    int valueofSpin = spinValue->value();
    return value;
}

void GuiTest::getSpinboxValue(QWidget* e){
    int spinNum = SpinBoxChanged(e);
    QString spinboxObjectName = e->objectName();
    if (isNormFilled < 4){
        QMessageBox::critical(this, "Error", "Please add all Files");
        return;
    } else {
        out << "data = pd.read_csv(db, header=[0, 1])\n";
        out << "data = spectral_data(data)\n";
        out << "unknown_data = pd.read_csv(unknowndatacsv, header=[0, 1])\n";
        out << "unknown_data = spectral_data(unknown_data)\n";
        out << "unknown_data.interp(data.df['wvl'].columns)\n";
        out << "data.mask(maskfile)\n";
        out << "unknown_data.mask(maskfile)\n";
    }
}

