#include <iostream>
#include <string>
#include <format>

using namespace std;


int common(int num1, int num2){
    int divider = 2;
    int common = 1;
    while ( (num1 % divider == 0) and (num2 % divider == 0) ){
        num1 /= divider;
        num2 /= divider;
        common *= divider;
    }
    for ( divider = 3; divider < 100; divider += 2 ){
        while ( (num1 % divider == 0) and (num2 % divider == 0) ){
            num1 /= divider;
            num2 /= divider;
            common *= divider;
            //cout << "löytää " << divider << endl;
        }
    //cout << divider << endl;
    }
    return common;
}
string simplify(int numer, int de){
    int highest_common = common(numer, de);
    //cout << "The highest common maker is: " << highest_common << endl;
    numer /= highest_common;
    de /= highest_common;
    string de_str = to_string(de);
    string numer_str = to_string(numer);
    if ( de_str == "1"){
        return numer_str;
    } else {
        return numer_str + "/" + de_str;
    }
}
int main()
{
    cout << "Enter a numerator: ";
    string numerato = "";
    cin >> numerato;
    cout << endl;
    string denominato = "";
    cout << "Enter a denominator: ";
    cin >> denominato;

    int numerator = stoi((numerato));
    int denominator = stoi((denominato));
    cout << endl;
    if ( denominator == 0){
        cout << "The denominator must be something other than zero!";
    } else {
        cout << "Your fraction, simplified: " << simplify(numerator, denominator);
    }
    cout << endl;
    return 0;
}
