#ifndef POCKERCALCULATOR_HH
#define POCKERCALCULATOR_HH

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class PockerCalculator; }
QT_END_NAMESPACE

class PockerCalculator : public QMainWindow
{
    Q_OBJECT

public:
    PockerCalculator(QWidget *parent = nullptr);
    ~PockerCalculator();

private slots:
    void on_btnReset_clicked();

    void on_btnConvert_clicked();

private:
    Ui::PockerCalculator *ui;
};
#endif // POCKERCALCULATOR_HH
