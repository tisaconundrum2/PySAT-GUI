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
    void setLabelAndSpinVisible(int index, bool visible);
    void on_maskFileButton_clicked();
    void on_unknownDataButton_clicked();
    void on_fullDataBaseButton_clicked();
    void on_outPutLocation_clicked();
    void on_pythonButton_clicked();
    void on_NormAddValuebutton_clicked();
    int getSpinValue();
    void getSpinboxValue(QWidget* e);
    void on_okButton_clicked();

private:
    Ui::GuiTest *ui;
};

#endif // GUITEST_H
