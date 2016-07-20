#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void isMissingData();
    void on_maskFileButton_clicked();
    void on_unknownDataButton_clicked();
    void on_fullDataBaseButton_clicked();
    void on_outPutLocationButton_clicked();
    void on_pythonButton_clicked();
    void setNormValuesVisible(int index, bool visible);
    void on_NormValuebutton_clicked(); //Norm Add Value
    int SpinBoxChanged(QWidget* wSp);
    void spinboxWrite(QWidget* e);
    void on_elementNameLine_editingFinished();
    void on_okButton_clicked();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
