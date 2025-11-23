#include <iostream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

int main()
{
    cout << "Enter the coefficients a, b and c. Written a b c: ";
    string coeff = "";
    getline(cin, coeff);
    double a = 0;
    double b = 0;
    double c = 0;
    istringstream iss(coeff);
    iss >> a >> b >> c;
    char bsign = '\0';
    char csign = '\0';

    if (b >= 0){
        bsign = '+';
    } else {
        bsign = '-';
    }
    if (c >= 0){
        csign = '+';
    } else {
        csign = '-';
    }

    cout << endl;
    cout << "The equation that you want to solve is: " << a << "x² " << bsign << " " << abs(b) << "x " << csign << " " << abs(c) << endl;

    double x1 = ( (-b+sqrt(b*b-4*a*c) )/double(2*a));
    double x2 = ( (-b-sqrt(b*b-4*a*c) )/double(2*a));
    if ( isnan(x1) and isnan(x2) ){
        cout << "The equation has no real answers!" << endl;
    } else if ( x1 == x2 ){
        cout << "The equation only has one answer and it is: " << x1 << endl;
    } else {
        cout << "The answers to the equation are: " << x1 << " and " << x2 << "." << endl;
    }
    return 0;
}
