#ifndef GUITEST_H
#define GUITEST_H

#include <QMainWindow>
#include <QLabel>
#include <QSpinBox>
namespace Ui {
class GuiTest;
}

class GuiTest : public QMainWindow
{
    Q_OBJECT

public:
    explicit GuiTest(QWidget *parent = 0);
    ~GuiTest();

private slots:
    void setupQSpinWidgets();
    void setSizeOfWindow();
    void setupOutFile();
    void setNormValuesVisible(int index, bool visible);
    void on_maskFileButton_clicked();
    void on_unknownDataButton_clicked();
    void on_fullDataBaseButton_clicked();
    void on_outPutLocationButton_clicked();
    void on_pythonButton_clicked();
    void on_NormValuebutton_clicked();
     int SpinBoxChanged(QWidget* wSp);
    void spinboxWrite(QWidget* e);
    void on_elementNameLine_editingFinished();
    void on_nfolds_test_valueChanged(int arg1);
    void on_okButton_clicked();
    void on_actionExit_triggered();


private:
    Ui::GuiTest *ui;
};

#endif // GUITEST_H
