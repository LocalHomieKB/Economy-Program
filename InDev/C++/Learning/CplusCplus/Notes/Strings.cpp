#include <iostream>
using namespace std;
#include <string>

int main() {
    string mystring;
    mystring = "Learning strings in C++"; // could also be done with ("Learning strings") - without the equal sign
    // could also be done with {"Learning strings"} - also without the equal sign
    cout << mystring << endl;
    //strings can also be edited
    mystring = "New string";
    cout << mystring << endl;

    return 0;
}
