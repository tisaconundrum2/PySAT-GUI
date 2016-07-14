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
    void SetupNiceWindow();
    void Setup();
    void setLabelsVisible(int index, bool visible);
    void setSpinrightVisible(int index, bool visible);
    void setSpinleftVisible(int index, bool visible);
    void on_toolButton_clicked();
    void on_toolButton_2_clicked();
    void on_toolButton_3_clicked();
    void on_toolButton_4_clicked();
    void on_actionExit_triggered();
    void on_pushButton_13_clicked();
    int SpinBoxChanged(QWidget *wSp);
    void spinboxWrite(QWidget* i);
    void on_toolButton_5_clicked();
    void on_pushButton_clicked();
    void numberOfNewlines(int n);


private:
    Ui::GuiTest *ui;
};

#endif // GUITEST_H
