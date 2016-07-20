#include "mainwindow.h"
#include "ui_mainwindow.h"
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
#include <QCloseEvent>

int isFalse[7];
int norm_size = 7;
int spinArray1[16];

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QRect rect = QApplication::desktop()->screenGeometry();
    int height = rect.height();
    this->resize(this->width(), height*0.9);
    for (int i = 0; i < norm_size; i++){
        setNormValuesVisible(i, false);
    }

    //Get all children of QSpinbox
    QList<QSpinBox*> spinBoxes= findChildren<QSpinBox*>();
    QSignalMapper* signalMapper= new QSignalMapper(this);
    QSpinBox* spinBox;
    foreach(spinBox, spinBoxes){
        connect(spinBox, SIGNAL(valueChanged(int)), signalMapper, SLOT(map()));
        signalMapper->setMapping(spinBox, spinBox);
    }
    connect(signalMapper, SIGNAL(mapped(QWidget*)), this, SLOT(spinboxWrite(QWidget*)));

    //Allocate by Zeroing out and false
    for (int i = 0; i < sizeof(isFalse)/sizeof(int) - 1; i++){
        isFalse[i] = 0;
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}


bool MainWindow::isMissingData(){
    int count = 0;
    for (int i = 0; i < sizeof(isFalse)/sizeof(int); i++){
        if (isFalse[i] == 0)
            count++;
    }
    if (count > 0)
        return true;
    else
        return false;
}

void MainWindow::on_maskFileButton_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Maskfile", QDir::homePath());
    ui->lineEdit->setText(file_name);
    isFalse[0] = 1;
}

void MainWindow::on_unknownDataButton_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Unknwon Data File", QDir::homePath());
    ui->lineEdit_2->setText(file_name);
    isFalse[1] = 1;
}

void MainWindow::on_fullDataBaseButton_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Database File", QDir::homePath());
    ui->lineEdit_3->setText(file_name);
    isFalse[2] = 1;
}

void MainWindow::on_outPutLocationButton_clicked(){
    const QString &file_name = QFileDialog::getExistingDirectory(this, "Select Output Directory", QDir::homePath());
    ui->lineEdit_4->setText(file_name);
    isFalse[3] = 1;
}

void MainWindow::on_pythonButton_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Python .exe File", QDir::rootPath());
    ui->lineEdit_6->setText(file_name);
    isFalse[4] = 1;
}


void MainWindow::setNormValuesVisible(int index, bool visible){
    QLabel* labels[norm_size] = {ui->norm_label_2,
                                 ui->norm_label_3,
                                 ui->norm_label_4,
                                 ui->norm_label_5,
                                 ui->norm_label_6,
                                 ui->norm_label_7,
                                 ui->norm_label_8};
    QSpinBox* spinright[norm_size] = {ui->norm_spinBox_2,
                                      ui->norm_spinBox_3,
                                      ui->norm_spinBox_4,
                                      ui->norm_spinBox_5,
                                      ui->norm_spinBox_6,
                                      ui->norm_spinBox_7,
                                      ui->norm_spinBox_8};
    QSpinBox* spinleft[norm_size] = {ui->norm_spinBox_10,
                                     ui->norm_spinBox_11,
                                     ui->norm_spinBox_12,
                                     ui->norm_spinBox_13,
                                     ui->norm_spinBox_14,
                                     ui->norm_spinBox_15,
                                     ui->norm_spinBox_16};
    labels[index]->setVisible(visible);
    spinright[index]->setVisible(visible);
    spinleft[index]->setVisible(visible);

}

int norm_push = 0;
void MainWindow::on_NormValuebutton_clicked(){ //Norm Add Value
    if (norm_push >= norm_size){
        QMessageBox::critical(this, "Warning", "Cannot add anymore values");
        return;
    } else {
        setNormValuesVisible(norm_push, true);
        norm_push++;
    }
}


int MainWindow::SpinBoxChanged(QWidget* wSp){
    QSpinBox* sp= (QSpinBox*)wSp;
    int value = sp->value();
    return value;
}

int flagBox = 0;
void MainWindow::spinboxWrite(QWidget* e){
    int spinNum = SpinBoxChanged(e);
    QString value = e->objectName();

    //TODO This really needs to get fixed... Please figure out a way to get these if statements cleaned up.
    if ((value == QString::fromStdString("norm_spinBox"))){           ui->norm_spinBox_10->setMinimum(spinNum); spinArray1[0] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_2"))){  ui->norm_spinBox_11->setMinimum(spinNum); spinArray1[1] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_3"))){  ui->norm_spinBox_12->setMinimum(spinNum); spinArray1[2] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_4"))){  ui->norm_spinBox_13->setMinimum(spinNum); spinArray1[3] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_5"))){  ui->norm_spinBox_14->setMinimum(spinNum); spinArray1[4] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_6"))){  ui->norm_spinBox_15->setMinimum(spinNum); spinArray1[5] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_7"))){  ui->norm_spinBox_16->setMinimum(spinNum); spinArray1[6] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_8"))){                                            spinArray1[7] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_9"))){  ui->norm_spinBox->setMinimum(spinNum);    spinArray1[8] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_10"))){ ui->norm_spinBox_2->setMinimum(spinNum);  spinArray1[9] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_11"))){ ui->norm_spinBox_3->setMinimum(spinNum);  spinArray1[10] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_12"))){ ui->norm_spinBox_4->setMinimum(spinNum);  spinArray1[11] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_13"))){ ui->norm_spinBox_5->setMinimum(spinNum);  spinArray1[12] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_14"))){ ui->norm_spinBox_6->setMinimum(spinNum);  spinArray1[13] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_15"))){ ui->norm_spinBox_7->setMinimum(spinNum);  spinArray1[14] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_16"))){ ui->norm_spinBox_8->setMinimum(spinNum);  spinArray1[15] = spinNum;
    }
    qDebug() << value << "\n";
    isFalse[5] = 1;

}

void MainWindow::on_elementNameLine_editingFinished(){
    int i = 0;
    isFalse[6] = 1;
}

void MainWindow::on_okButton_clicked(){
    if (isMissingData()){
        QMessageBox::critical(this, "Warning", "There is missing information please make sure to fill all data in");
        return;
    }
    //    file.close();
    //    system(qPrintable(python_file + " " + "out.py"));
}
