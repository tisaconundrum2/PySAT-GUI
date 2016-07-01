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

int push = 0;
//###### Setup GUI Here


GuiTest::GuiTest(QWidget *parent) :
    QMainWindow(parent), ui(new Ui::GuiTest){
    ui->setupUi(this);

    //######TODO: fix sizing issue, this will allow any computer to have a nicely sized window
    QRect rec = QApplication::desktop()->screenGeometry();
    int height = rec.height();
    this->resize(this->width(), height*0.9);
    //#########################################################################################

    //#####TODO: add the ability to show buttons for normalization these are a bunch of lists that parse
    //    each item and then will be setVisibile to false so they aren't there until you click a button
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
     */

    int size = 6;
    QLabel* labl[size] = {labels(size)};
    QSpinBox* spinr[size] = {spinright(size)};
    QSpinBox* spinl[size] = {spinleft(size)};
    for (int i = 0; i < 6; i++){
        labl[i]->setVisible(false);
        spinr[i]->setVisible(false);
        spinl[i]->setVisible(false);
    }
    //#########################################################################################
}

QLabel* GuiTest::labels(int size){
    QLabel* labels[size] = {ui->norm_label_2,
                         ui->norm_label_3,
                         ui->norm_label_4,
                         ui->norm_label_5,
                         ui->norm_label_6,
                         ui->norm_label_7,
                         ui->norm_label_8};
    return labels[size];
}

QSpinBox* GuiTest::spinright(int size){
    QSpinBox* spinright[size] = {ui->norm_spinBox_2,
                              ui->norm_spinBox_3,
                              ui->norm_spinBox_4,
                              ui->norm_spinBox_5,
                              ui->norm_spinBox_6,
                              ui->norm_spinBox_7,
                              ui->norm_spinBox_8};
    return spinright[size];
}

QSpinBox* GuiTest::spinleft(int size){
    QSpinBox* spinleft[size] = {ui->norm_spinBox_10,
                             ui->norm_spinBox_11,
                             ui->norm_spinBox_12,
                             ui->norm_spinBox_13,
                             ui->norm_spinBox_14,
                             ui->norm_spinBox_15,
                             ui->norm_spinBox_16};
    return spinleft[size];
}

GuiTest::~GuiTest()
{
    delete ui;
}

/*************** GUI Interface **************
 *     |-----------------------------------|
 *     |   Maskfile                        | <- on_toolButton_clicked  ; this will open a dialog to look for the .csv mask file
 *     |   Unknown Data                    | <- on_toolButton_2_clicked; this will open a dialog to look for the .csv unknown data file
 *     |   Full Database                   | <- on_toolButton_3_clicked; this will open a dialog to look for the .csv full database file
 *     |   Output Location                 | <- on_toolButton_4_clicked; this will open a dialog to look for a directory that you'd like
 *     |                                   |                             to output your images to
 *     |                                   |
 *     .                                   .
 *     |-----------------------------------|
 *
 */

void GuiTest::on_toolButton_clicked()
{
    const QString &file_name = QFileDialog::getOpenFileName(this, "Open New File", QDir::homePath());
    ui->lineEdit->setText(file_name);
}

void GuiTest::on_toolButton_2_clicked()
{
    const QString &file_name = QFileDialog::getOpenFileName(this, "Open New File", QDir::homePath());
    ui->lineEdit_2->setText(file_name);
}

void GuiTest::on_toolButton_3_clicked()
{
    const QString &file_name = QFileDialog::getOpenFileName(this, "Open New File", QDir::homePath());
    ui->lineEdit_3->setText(file_name);
}

void GuiTest::on_toolButton_4_clicked()
{
    const QString &file_name = QFileDialog::getExistingDirectory(this, "Open New Directory", QDir::homePath());
    ui->lineEdit_4->setText(file_name);
}

void GuiTest::on_actionExit_triggered()
{
    this->close();
}

void GuiTest::on_pushButton_13_clicked()
{
    if (push > 6){
        QMessageBox::critical(this, "Warning", "Cannot add anymore values");
    } else {
        QLabel* labl[7] = {labels()};
        QSpinBox* spinr[7] = {spinright()};
        QSpinBox* spinl[7] = {spinleft()};
        push++;
    }
}

void GuiTest::on_pushButton_clicked()
{

}
