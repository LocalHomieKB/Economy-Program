#include <iostream>
using namespace std;

int main() {
    int a, b, result; 
    cout << "Hello, World!" << endl;
    a = 5;
    b = 2;
    a = a+ 1;
    result = a-b;
    cout << "Result: " << result << endl;

    // Initialising variables
    // c like:
    int c = 3;
    // constructor:
    int d(4);
    // uniform initialisation (C++11):
    int e{5};

    //deduction:
    int foo = 0;
    auto bar = foo; // the same as int bar = foo;

    //decltype (C++11):
    int aba  = 0;
    decltype(aba) oba; // the same as int oba;
    return 0;
}