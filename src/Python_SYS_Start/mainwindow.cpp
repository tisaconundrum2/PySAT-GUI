#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFileDialog>
#include <QMessageBox>
#include <QDesktopServices>
#include <QUrl>
#include <QProcess>
#include <QDir>

//settin up global variables
QString workingDir;
QString pythonProcess;
QString file;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


/* Program to run a python file, how this should look in theory
 *
 *   |-------- Application Window --------|
 *   |                                    |
 *   |       | choose work directory |    | <- this part will be push button, and it will set up the directory
 *   |                                    |    by opening a new window to help us choose where anaconda3's python interp is
 *   |       | choose application|        | <- this part will setArguments and will run the actual python program
 *   |                                    |
 *   |       | choose your file |         | <- choose the pls_sm_test.py file
 *   |          | ok |                    | <- press ok to start your application
 *   |                                    |
 *   |____________________________________|
 */


void MainWindow::on_pushButton_clicked()//choose work directory button
{
    workingDir = QFileDialog::getExistingDirectory(this, "Open Working Directory", QDir::homePath());
    QDir::setCurrent(workingDir);
}


void MainWindow::on_pushButton_2_clicked()//choose application button
{
    pythonProcess = QFileDialog::getOpenFileName(this, "Open Application .exe", QDir::homePath());
}

void MainWindow::on_pushButton_4_clicked()//choose file button
{
    file = QFileDialog::getOpenFileName(this, "Open python working file", QDir::homePath());
}

void MainWindow::on_pushButton_3_clicked()//ok button
{
    system(qPrintable(pythonProcess + " " + file));
}

