#include "mainwindow.hh"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_btnPlus_clicked()
{
    firstNum = ui->lineFirst->text().toDouble();
    secondNum = ui->lineSecond->text().toDouble();
    resultNum = firstNum + secondNum;
    ui->lineResult->setText(QString::number(resultNum));
}


void MainWindow::on_btnMinus_clicked()
{
    firstNum = ui->lineFirst->text().toDouble();
    secondNum = ui->lineSecond->text().toDouble();
    resultNum = firstNum - secondNum;
    ui->lineResult->setText(QString::number(resultNum));
}

void MainWindow::on_btnDivid_clicked()
{
    firstNum = ui->lineFirst->text().toDouble();
    secondNum = ui->lineSecond->text().toDouble();
    resultNum = firstNum / secondNum;
    ui->lineResult->setText(QString::number(resultNum));
}

void MainWindow::on_btnTimes_clicked()
{
    firstNum = ui->lineFirst->text().toDouble();
    secondNum = ui->lineSecond->text().toDouble();
    resultNum = firstNum * secondNum;
    ui->lineResult->setText(QString::number(resultNum));
}

void MainWindow::on_pushButton_clicked()
{
    ui->lineFirst->clear();
    ui->lineSecond->clear();
}

