#include "pockercalculator.hh"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    PockerCalculator w;
    w.show();
    return a.exec();
}
