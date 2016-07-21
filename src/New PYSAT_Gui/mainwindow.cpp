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
QFile file("out.py");
QTextStream out(&file);

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
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Maskfile");
    ui->lineEdit->setText(QDir::toNativeSeparators(file_name));
    isFalse[0] = 1;
}

void MainWindow::on_unknownDataButton_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Unknwon Data File");
    ui->lineEdit_2->setText(QDir::toNativeSeparators(file_name));
    isFalse[1] = 1;
}

void MainWindow::on_fullDataBaseButton_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Database File");
    ui->lineEdit_3->setText(QDir::toNativeSeparators(file_name));
    isFalse[2] = 1;
}

void MainWindow::on_outPutLocationButton_clicked(){
    const QString &file_name = QFileDialog::getExistingDirectory(this, "Select Output Directory");
    ui->lineEdit_4->setText(QDir::toNativeSeparators(file_name));
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
        qDebug() << (norm_push+1)*2;
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
//    if (isMissingData()){
//        QMessageBox::critical(this, "Warning", "There is missing information please make sure to fill all data in");
//        return;
//    }
    file.open(QIODevice::WriteOnly | QIODevice::Text);
    QTextStream out(&file);

    out << "from pysat.spectral.spectral_data import spectral_data\n"                               ;
    out << "from pysat.regression.pls_sm import pls_sm\n"                                           ;
    out << "import pandas as pd\n"                                                                  ;
    out << "maskfile = r\"" << ui->lineEdit->text() << "\"\n";
    out << "unknowndatacsv = r\"" << ui->lineEdit_2->text() << "\"\n";
    out << "db = r\"" << ui->lineEdit_3->text() << "\"\n";
    out << "outpath = r\"" << ui->lineEdit_4->text() << "\"\n";

    out << "data = pd.read_csv(db, header=[0, 1])\n"                                                ;
    out << "data = spectral_data(data)\n"                                                           ;
    out << "unknown_data = pd.read_csv(unknowndatacsv, header=[0, 1])\n"                            ;
    out << "unknown_data = spectral_data(unknown_data)\n"                                           ;
    out << "unknown_data.interp(data.df['wvl'].columns)\n"                                          ;
    out << "data.mask(maskfile)\n"                                                                  ;
    out << "unknown_data.mask(maskfile)\n"                                                          ;

    out << "ranges3 = [";
    for (int i = 0; i <  (norm_push+1); i++){
        out << "(" << spinArray1[i-1] << ", "<< spinArray1[i] <<")";
        //if i at the end stop adding commas
        if (i+1 < norm_push+1)
            out << ",";
    }
    out << "]\n";

    out << "ranges1 = [(0, 1000)]\n"                                                                ;

    out << "data3 = data\n"                                                                         ;
    out << "data3.norm(ranges3)\n"                                                                  ;
    out << "unknown_data3 = unknown_data\n"                                                         ;
    out << "unknown_data3.norm(ranges3)\n"                                                          ;
    out << "data1 = data\n"                                                                         ;
    out << "data1.norm(ranges1)\n"                                                                  ;
    out << "unknown_data1 = unknown_data\n"                                                         ;
    out << "unknown_data1.norm(ranges1)\n"                                                          ;

    out << "el = '" << ui->elementNameLine->text() << "'\n"                                                                          ;
    out << "nfolds_test = "<< ui->nfolds_test->value()<<"\n"                                                                      ;
    out << "testfold_test = 4\n"                                                                    ;
    out << "nfolds_cv = 5\n"                                                                        ;
    out << "testfold_cv = 3\n"                                                                      ;
    out << "compranges = [[" << ui->comp_range->value() << ", " << ui->comp_range_2->value() << "], [" << ui->comp_range_3->value() << ", " << ui->comp_range_4->value() << "], [" << ui->comp_range_5->value() << ", " << ui->comp_range_6->value() << "], [" << ui->comp_range_7->value() << ", " << ui->comp_range_8->value() << "]]\n"                              ;
    out << "nc = 20\n"                                                                              ;

    out << "data3.stratified_folds(nfolds=nfolds_test, sortby=('meta', el))\n"                      ;
    out << "data3_train = data3.rows_match(('meta', 'Folds'), [testfold_test], invert=True)\n"      ;
    out << "data3_test = data3.rows_match(('meta', 'Folds'), [testfold_test])\n"                    ;
    out << "data1.stratified_folds(nfolds=nfolds_test, sortby=('meta', el))\n"                      ;
    out << "data1_train = data1.rows_match(('meta', 'Folds'), [testfold_test], invert=True)\n"      ;
    out << "data1_test = data1.rows_match(('meta', 'Folds'), [testfold_test])\n"                    ;

    out << "ncs = [" << ui->create_model_spin->value() << ", " << ui->create_model_spin_2->value() << ", " << ui->create_model_spin_3->value() << ", " << ui->create_model_spin_4->value() << "]\n"                                                                   ;

    out << "traindata = [data3_train.df, data3_train.df, data1_train.df, data3_train.df]\n"         ;
    out << "testdata = [data3_test.df, data3_test.df, data1_test.df, data3_test.df]\n"              ;
    out << "unkdata = [unknown_data3.df, unknown_data3.df, unknown_data1.df, unknown_data3.df]\n"   ;

    out << "sm = pls_sm()\n"                                                              ;
    out << "sm.fit(traindata, compranges, ncs, el, figpath=outpath)\n"                    ;
    out << "predictions_train = sm.predict(traindata)\n"                                  ;
    out << "predictions_test = sm.predict(testdata)\n"                                    ;
    out << "blended_train = sm.do_blend(predictions_train, traindata[0]['meta'][el])\n"   ;
    out << "blended_test = sm.do_blend(predictions_test)\n"                               ;

    out << "sm.final(testdata[0]['meta'][el],\n"                                          ;
    out << "blended_test,\n"                                                              ;
    out << "el=el,\n"                                                                     ;
    out << "xcol='Ref Comp Wt. %',\n"                                                     ;
    out << "ycol='Predicted Comp Wt. %',\n"                                               ;
    out << "figpath=outpath)\n";
    file.flush();
    file.close();
    system(qPrintable(ui->lineEdit_6->text() + " " + "out.py"));
}
