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

//Global variables
int norm_push = 0;                              // this variable measures how many time's the normalization button has been pushed
int norm_size = 7;                              // this variable measures the size of arrays in the normalization section
int spinArray1[16] = {0,0,0,0,
                      0,0,0,0,
                      0,0,0,0,
                      0,0,0,0
                     };
QString python_file = "";
QString output_location = "";

GuiTest::GuiTest (QWidget *parent):
    QMainWindow(parent), ui(new Ui::GuiTest){
    ui->setupUi(this);
    //TODO: fix sizing issues, this will allow any computer to have a nicely sized window
    QRect rect = QApplication::desktop()->screenGeometry();
    int height = rect.height();
    this->resize(this->width(), height*0.9);
    for (int i = 0; i < norm_size; i++){        //setting up visibility
        setSpinleftVisible(i, false);
        setSpinrightVisible(i, false);
        setLabelsVisible(i, false);
    }

    QList<QSpinBox*> spinBoxes= findChildren<QSpinBox*>();
    //create the QSignalMapper object
    QSignalMapper* signalMapper= new QSignalMapper(this);
    //loop through your spinboxes list
    QSpinBox* spinBox;
    foreach(spinBox, spinBoxes){
        //setup mapping for each spin box
        connect(spinBox, SIGNAL(valueChanged(int)), signalMapper, SLOT(map()));
        signalMapper->setMapping(spinBox, spinBox);
    }
    //connect the unified mapped(QWidget*) signal to your spinboxWrite slot
    connect(signalMapper, SIGNAL(mapped(QWidget*)), this, SLOT(spinboxWrite(QWidget*)));
}

GuiTest::~GuiTest(){
    delete ui;
}

/*
 *
 *           |--------------------------------------- this is a label it doesn't do anything
 *           |        |------------------------------ this value will be spinleft it will have values ranging from 0 to 99
 *           |        |            |----------------- this value will be spinright it will have values ranging from 0 to 99
 *           v        v            v
 *    |-------------------------------------------|
 *    |    value1 [         ] [         ]         | <- There are 8 of each; label, spinleft, spinright.
 *    |                         add value         | <- each of these fields are hidden until the user hits the add value button
 *    |                                           | -> Personal Note: Check to see if the user has increased "push++"
 *    |                                           |    if they had, then take the values entered in the boxes and write it to the
 *    |-------------------------------------------|    python file.
 *
 *    TODO: add the ability to show buttons for normalization these are a bunch of lists that parse
 *    each item and then will be setVisibile to false so they aren't there until you click a button
 */

/*************** GUI Interface **************
 *     |-----------------------------------|
 *     |   Maskfile               [..]     | <- on_toolButton_clicked  ; this will open a dialog to look for the .csv mask file
 *     |   Unknown Data           [..]     | <- on_toolButton_2_clicked; this will open a dialog to look for the .csv unknown data file
 *     |   Full Database          [..]     | <- on_toolButton_3_clicked; this will open a dialog to look for the .csv full database file
 *     |   Output Location        [..]     | <- on_toolButton_4_clicked; this will open a dialog to look for a directory that you'd like
 *     |                                   |                             to output your images to
 *     |                                   |
 *     .                                   .
 *     .                            [ok]   . <- on_pushButton_clicked; this will create the final py file
 *     |-----------------------------------|
 *
 */


void GuiTest::setLabelsVisible(int index, bool visible){
    QLabel* labels[norm_size] = {ui->norm_label_2,
                                 ui->norm_label_3,
                                 ui->norm_label_4,
                                 ui->norm_label_5,
                                 ui->norm_label_6,
                                 ui->norm_label_7,
                                 ui->norm_label_8};
    labels[index]->setVisible(visible);
}

void GuiTest::setSpinrightVisible(int index, bool visible){
    QSpinBox* spinright[norm_size] = {ui->norm_spinBox_2,
                                      ui->norm_spinBox_3,
                                      ui->norm_spinBox_4,
                                      ui->norm_spinBox_5,
                                      ui->norm_spinBox_6,
                                      ui->norm_spinBox_7,
                                      ui->norm_spinBox_8};
    spinright[index]->setVisible(visible);
}

void GuiTest::setSpinleftVisible(int index, bool visible){
    QSpinBox* spinleft[norm_size] = {ui->norm_spinBox_10,
                                     ui->norm_spinBox_11,
                                     ui->norm_spinBox_12,
                                     ui->norm_spinBox_13,
                                     ui->norm_spinBox_14,
                                     ui->norm_spinBox_15,
                                     ui->norm_spinBox_16};
    spinleft[index]->setVisible(visible);
}


void GuiTest::on_toolButton_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Maskfile", QDir::homePath());
    ui->lineEdit->setText(file_name);
}

void GuiTest::on_toolButton_2_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Unknwon Data File", QDir::homePath());
    ui->lineEdit_2->setText(file_name);
}

void GuiTest::on_toolButton_3_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Database File", QDir::homePath());
    ui->lineEdit_3->setText(file_name);
}

void GuiTest::on_toolButton_4_clicked(){
    output_location = QFileDialog::getExistingDirectory(this, "Select Output Directory", QDir::homePath());
    ui->lineEdit_4->setText(output_location);
}

void GuiTest::on_toolButton_5_clicked(){
    python_file = QFileDialog::getOpenFileName(this, "Python .exe File", QDir::rootPath());
    ui->lineEdit_6->setText(python_file);
}

void GuiTest::on_actionExit_triggered(){
    this->close();
}

/*************** GUI Interface **************/

void GuiTest::on_pushButton_13_clicked(){
    if (norm_push >= norm_size){
        QMessageBox::critical(this, "Warning", "Cannot add anymore values");
    } else {
        setSpinleftVisible(norm_push, true);
        setSpinrightVisible(norm_push, true);
        setLabelsVisible(norm_push, true);
        norm_push++;
    }
}


int GuiTest::SpinBoxChanged(QWidget* wSp){
    QSpinBox* sp= (QSpinBox*)wSp;                                   //now sp is a pointer to the QSpinBox that emitted the valueChanged signal
    int value = sp->value();                                        //and value is its value after the change
    return value;
}

void GuiTest::spinboxWrite(QWidget* e){
    int spinNum = SpinBoxChanged(e);
    //get the name of each spinbox this will help in identifying who's being manipulated
    QString value = e->objectName();

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

}

void GuiTest::on_pushButton_clicked(){
    QFile file("out.py");
    file.open(QIODevice::WriteOnly | QIODevice::Text);
    QTextStream out(&file);
    out << "from pysat.spectral.spectral_data import spectral_data\n"
           "from pysat.regression.pls_sm import pls_sm\n"
           "import pandas as pd\n"
           "outpath = r'C:\Users\User\Desktop\Output'\n"
           "db = r\"C:\Users\User\Desktop\full_db_mars_corrected_dopedTiO2_pandas_format.csv\"\n"
           "unknowndatacsv = r\"C:\Users\User\Desktop\lab_data_averages_pandas_format.csv\"\n"
           "maskfile = r\"C:\Users\User\Desktop\mask_minors_noise.csv\"\n"
           "data = pd.read_csv(db, header=[0, 1])\n"
           "data = spectral_data(data)\n"
           "unknown_data = pd.read_csv(unknowndatacsv, header=[0, 1])\n"
           "unknown_data = spectral_data(unknown_data)\n"
           "unknown_data.interp(data.df['wvl'].columns)\n"
           "data.mask(maskfile)\n"
           "unknown_data.mask(maskfile)\n"
           "def get_ranges(r0, r1, r2, r3):\n"
               "return [(r0, r1), (r1, r2), (r2, r3)]\n"
           "ranges3 = get_ranges(0, 350, 470, 1000)\n"
           "ranges3 = [(0, 350), (350, 470), (470, 1000)]\n"
           "ranges1 = [(0, 1000)]\n"
           "data3 = data\n"
           "data3.norm(ranges3)\n"
           "unknown_data3 = unknown_data\n"
           "unknown_data3.norm(ranges3)\n"
           "data1 = data\n"
           "data1.norm(ranges1)\n"
           "unknown_data1 = unknown_data\n"
           "unknown_data1.norm(ranges1)\n"
           "el = 'SiO2'\n"
           "nfolds_test = 6\n"
           "testfold_test = 4\n"
           "nfolds_cv = 5\n"
           "testfold_cv = 3\n"
           "compranges = [[-20, 50], [30, 70], [60, 100], [0, 120]]\n"
           "nc = 20\n"
           "data3.stratified_folds(nfolds=nfolds_test, sortby=('meta', el))\n"
           "data3_train = data3.rows_match(('meta', 'Folds'), [testfold_test], invert=True)\n"
           "data3_test = data3.rows_match(('meta', 'Folds'), [testfold_test])\n"
           "data1.stratified_folds(nfolds=nfolds_test, sortby=('meta', el))\n"
           "data1_train = data1.rows_match(('meta', 'Folds'), [testfold_test], invert=True)\n"
           "data1_test = data1.rows_match(('meta', 'Folds'), [testfold_test])\n"
           "ncs = [7, 7, 5, 9]\n"
           "traindata = [data3_train.df, data3_train.df, data1_train.df, data3_train.df]\n"
           "testdata = [data3_test.df, data3_test.df, data1_test.df, data3_test.df]\n"
           "unkdata = [unknown_data3.df, unknown_data3.df, unknown_data1.df, unknown_data3.df]\n"
           "sm = pls_sm()\n"
           "sm.fit(traindata, compranges, ncs, el, figpath=outpath)\n"
           "predictions_train = sm.predict(traindata)\n"
           "predictions_test = sm.predict(testdata)\n"
           "blended_train = sm.do_blend(predictions_train, traindata[0]['meta'][el])\n"
           "blended_test = sm.do_blend(predictions_test)\n"
           "sm.final(testdata[0]['meta'][el],\n"
                    "blended_test,\n"
                    "el=el,\n"
                    "xcol='Ref Comp Wt. %',\n"
                    "ycol='Predicted Comp Wt. %',\n"
                    "\figpath=outpath)\n";

    file.close();
    system(qPrintable(python_file + " " + output_location+"out.py"));
}

