#include <QDesktopServices>
#include "guitest.h"
#include "ui_guitest.h"
#include <QString>
#include <QFile>
#include <QDir>
#include <QMessageBox>
#include <QFileDialog>
#include <QFileInfo>

GuiTest::GuiTest(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::GuiTest)
{
    ui->setupUi(this);
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

bool fileExists(QString path) {
    QFileInfo check_file(path);
    // check if file exists and if yes: Is it really a file and no directory?
    return check_file.exists() && check_file.isFile();
}

void GuiTest::on_pushButton_clicked()
{
    if (!fileExists("C:/Users/User/Anaconda3/python.exe")){
        QMessageBox::StandardButton reply= QMessageBox::warning(this,
                                                                "Warning",
                                                                "Python doesn't seem to exist on your system, please download it",
                                                                QMessageBox::Ok);
        if (reply == QMessageBox::Ok){
            QString link = "https://www.continuum.io/downloads";
            QDesktopServices::openUrl(QUrl(link));
        }
    }
}

