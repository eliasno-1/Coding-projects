#ifndef MAINWINDOW_HH
#define MAINWINDOW_HH

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    double firstNum = 0;
    double secondNum = 0;
    double resultNum = 0;

private slots:
    void on_btnPlus_clicked();
    void on_btnMinus_clicked();
    void on_btnDivid_clicked();
    void on_btnTimes_clicked();

    void on_pushButton_clicked();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_HH
