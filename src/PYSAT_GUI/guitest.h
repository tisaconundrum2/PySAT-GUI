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
    void setSizeOfWindow();
    void setupQSpinWidgets();
    void setupOutFile();
    void setNormValuesVisible(int index, bool visible);
    void on_maskFileButton_clicked();
    void on_unknownDataButton_clicked();
    void on_fullDataBaseButton_clicked();
    void on_outPutLocationButton_clicked();
    void on_actionExit_triggered();
    void on_NormValuebutton_clicked();
    int SpinBoxChanged(QWidget *wSp);
    void spinboxWrite(QWidget* i);
    void on_pythonButton_clicked();
    void on_okButton_clicked();
    void on_nfolds_test_valueChanged(int arg1);
    void on_elementNameLine_textChanged(const QString &arg1);

private:
    Ui::GuiTest *ui;
};

#endif // GUITEST_H
