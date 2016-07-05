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
    void setLabelsVisible(int index, bool visible);
    void setSpinrightVisible(int index, bool visible);
    void setSpinleftVisible(int index, bool visible);
    void on_toolButton_clicked();
    void on_toolButton_2_clicked();
    void on_toolButton_3_clicked();
    void on_toolButton_4_clicked();
    void on_actionExit_triggered();
    void on_pushButton_13_clicked();
    void on_norm_spinBox_valueChanged(int arg1);
    void on_norm_spinBox_2_valueChanged(int arg1);
    void on_norm_spinBox_3_valueChanged(int arg1);
    void on_norm_spinBox_4_valueChanged(int arg1);
    void on_norm_spinBox_5_valueChanged(int arg1);
    void on_norm_spinBox_6_valueChanged(int arg1);
    void on_norm_spinBox_7_valueChanged(int arg1);
    void on_norm_spinBox_8_valueChanged(int arg1);
    void on_norm_spinBox_9_valueChanged(int arg1);
    void on_norm_spinBox_10_valueChanged(int arg1);
    void on_norm_spinBox_11_valueChanged(int arg1);
    void on_norm_spinBox_12_valueChanged(int arg1);
    void on_norm_spinBox_13_valueChanged(int arg1);
    void on_norm_spinBox_14_valueChanged(int arg1);
    void on_norm_spinBox_15_valueChanged(int arg1);
    void on_norm_spinBox_16_valueChanged(int arg1);

private:
    Ui::GuiTest *ui;
};

#endif // GUITEST_H
