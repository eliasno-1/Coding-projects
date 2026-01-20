#include "pockercalculator.hh"
#include "ui_pockercalculator.h"

/*  This program makes the conversion from one alcoholic beverage to another.
 *  You can set a vol-% of a specified drink and the amount and it will calculate
 *  how many drinks of another specified vol-% and volume it matches with it's
 *  alcohol content. This was made for the fun of it and it does not glorify
 *  the use of alcohol. Alcohol is bad and it should be consumed with moderation!
 *
 * */

PockerCalculator::PockerCalculator(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::PockerCalculator)
{
    ui->setupUi(this);
}

PockerCalculator::~PockerCalculator()
{
    delete ui;
}


void PockerCalculator::on_btnReset_clicked()
{
    // we clear all the input boxes on button press
    ui->txtDrinkAmount->clear();
    ui->txtVolOfSingleDrink->clear();
    ui->txtVolFrom->clear();
    ui->txtEqualDrinks->clear();
    ui->txtVolPercTo->clear();
    ui->txtVolTarget->clear();
}


void PockerCalculator::on_btnConvert_clicked()
{
    // initialize variables
    double drinks = ui->txtDrinkAmount->text().toDouble();
    int vol_of_single_drink = ui->txtVolOfSingleDrink->text().toInt();
    double original_volume_percent = ui->txtVolFrom->text().toDouble();
    double new_volume_percent = ui->txtVolPercTo->text().toDouble();
    double target_volume = ui->txtVolTarget->text().toDouble();

    // calculate the new volume and how many drinks of specified volume it matches
    double pure_alcohol = drinks * vol_of_single_drink * (original_volume_percent / 100);
    double new_volume = pure_alcohol / (new_volume_percent / 100) ;
    double target_volume_in_drinks = new_volume / target_volume;

    // set the text labels
    ui->txtEqualDrinks->setText(QString::number(new_volume));
    ui->txtTargetamount->setText(QString::number(target_volume_in_drinks));

}

