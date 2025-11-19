/*  NOTES:

Standard input is default, cin is the
stream object assigned to it

cin is used alongside extraction operator
for input operations.

extraction operator >>

used as following:

int age;
cin >> age;

You can separate cin with space, tab or a newline
by doing this you can do this:
cin >> a >> b;

this will ask the user for two separate inputs in one line


Strings and cin:

You can extract straight from cin for strings, this is limited
to one word however

string mystring;
cin >> mystring;

in order to extract more use getline(cin with strings code)

stringstream:

This is used to treat a string as a stream. Useful to 
convert strings to numerical values and vice versa

string mystr ("1204");
int myint;
stringstream(mystr) >> myint;

this asks for a string, attaches 1204 to mystr. then a variable
of int is introduced. This is then used to extract
from a stringstream constructed from the string. It stores 
1204 in a variable called myint

see code "stringstreams" for more. 

*/

//Basic cin program:

/*
#include <iostream>
using namespace std;

int main()
{
    int i;
    cout << "Please enter an integer value: ";
    cin >> i; //Asks for the int i(without forcing an int input)
    cout << "The value you entered is " << i;
    cout << " and its double is " << i*2 << ".\n";
    return 0;
}

*/
//an issue with this program occurs when a type other than int
//is typed

//cin with strings

/*
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string mystr;
    cout << "What's your name? ";
    getline (cin, mystr);
    cout << "Hello " << mystr << ".\n";
    cout << "What is your favourite team? ";
    getline (cin, mystr);
    cout << "I like " << mystr << " too!\n";
    return 0;
}
*/

//Unless you seriously have a reason not to, use getline rather
// than straight from cin

// stringstreams:

/*
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main ()
{
    string mystr;
    float price  =0;
    int quantity=0;

    cout << "Enter price: ";
    getline (cin,mystr);
    stringstream(mystr) >> price;
    cout << "Enter quantity: ";
    getline (cin,mystr);
    stringstream(mystr) >> quantity;
    cout << "Total price: " << price*quantity << endl;
    return 0; 
}
*/

/*
    instead of grabbing numeric values straight from cin,
    we get lines of input and then extract the values into
    price and quantity. Apparently this is better, though
    i'm not sure why. */