#include <iostream>
using namespace std;

    /* Typed constant expressions:
        const double pi = 3.1415926;
        const char tab = '\t'
        
        These can then be used as a part of this*/

const double pi = 3.1415926;
const char tab = '\t';

int main()
{
    double r=5.0; //radius
    double circle;

    circle = 2 * pi * r;
    cout << circle;
    cout << tab;
}  //the result would be 31.4159

//To do the above preprocessor definitions also work:
// Take note, this occurs before the program, and no check of types or syntax occurs

