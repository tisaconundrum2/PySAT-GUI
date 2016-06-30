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
    int width = rec.width();
    this->resize(this->width(), height*0.9);
    qDebug() << height << width;
    //#########################################################################################

    //#####TODO: add the ability to show buttons for normalization these are a bunch of lists that parse
    //    each item and then will be setVisibile to false so they aren't there until you click a button
    auto labels = {ui->norm_label_2,
                   ui->norm_label_3,
                   ui->norm_label_4,
                   ui->norm_label_5,
                   ui->norm_label_6,
                   ui->norm_label_7,
                   ui->norm_label_8};
    auto spinright = {ui->norm_spinBox_2,
                      ui->norm_spinBox_3,
                      ui->norm_spinBox_4,
                      ui->norm_spinBox_5,
                      ui->norm_spinBox_6,
                      ui->norm_spinBox_7,
                      ui->norm_spinBox_8};
    auto spinleft = {ui->norm_spinBox_10,
                     ui->norm_spinBox_11,
                     ui->norm_spinBox_12,
                     ui->norm_spinBox_13,
                     ui->norm_spinBox_14,
                     ui->norm_spinBox_15,
                     ui->norm_spinBox_16};

    for (auto label : labels) label->setVisible(false);
    for (auto spinr : spinright) spinr->setVisible(false);
    for (auto spinl : spinleft) spinl->setVisible(false);
    //#########################################################################################
}

GuiTest::~GuiTest()
{
    delete ui;
}

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
        QLabel* labels[7] = {ui->norm_label_2,
                       ui->norm_label_3,
                       ui->norm_label_4,
                       ui->norm_label_5,
                       ui->norm_label_6,
                       ui->norm_label_7,
                       ui->norm_label_8};
        QSpinBox* spinright[7] = {ui->norm_spinBox_2,
                          ui->norm_spinBox_3,
                          ui->norm_spinBox_4,
                          ui->norm_spinBox_5,
                          ui->norm_spinBox_6,
                          ui->norm_spinBox_7,
                          ui->norm_spinBox_8};
        QSpinBox* spinleft[7] = {ui->norm_spinBox_10,
                         ui->norm_spinBox_11,
                         ui->norm_spinBox_12,
                         ui->norm_spinBox_13,
                         ui->norm_spinBox_14,
                         ui->norm_spinBox_15,
                         ui->norm_spinBox_16};

        labels[push]->setVisible(true);
        spinright[push]->setVisible(true);
        spinleft[push]->setVisible(true);
        push++;
    }
}
