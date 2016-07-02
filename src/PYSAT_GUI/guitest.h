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
    void on_toolButton_clicked();
    void on_toolButton_2_clicked();
    void on_toolButton_3_clicked();
    void on_toolButton_4_clicked();
    void on_actionExit_triggered();
    void on_pushButton_13_clicked();
    void on_pushButton_clicked();
//    QLabel* labels(int size);
//    QSpinBox* spinright(int size);
//    QSpinBox* spinleft(int size);

private:
    Ui::GuiTest *ui;
};

#endif // GUITEST_H
