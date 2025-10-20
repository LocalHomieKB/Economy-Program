/*  NOTES:

streams: entity where a program can either insert or extract characters to/from.
They are simply soure/destinations of character and occur one after another

4 common types:
cin (standard input stream) - self note, why not sin rather than cin?
cout (standard output stream)
cerr (standard error(output) stream)
clog (standard logging (output) stream)


cout:

the C++ stream object designed to access the screen is cout,
its used in conjuction with the insertion operator(<<).

examples:

cout <<"Output sentence"; /prints output sentence on screen
cout <<120; /prints the number 120 on screen
cout << x; / prints value of x on screen


You can also chain multiple insertions together:

cout << "This " << " is a " << "single C++ statement";

this would print out : This is a single C++ statement, though
spaces have to be taken awareness of.

Useful for combining literals and variables as in the following:

cout << "I am " << age << " years old and my zipcode is " << zipcode

with age = 24 and zipcode = 90064, this would print:
"I am 24 years old and my zipcode is 90064"

One thing that isn't done is line breaks.
To fix the following example:

cout << "This is a sentence.";
cout << "This is another sentence."

would print: "This is a sentence.This is another sentence"
Instead we can do:
cout << "First sentence.\n";
cout << "Second sentence.\nThird sentence.";

which would print:
First sentence
Second sentence
Third sentence

Or:

cout << "First sentence." << endl;
cout << "Second sentence." << endl;

which would print:

First sentence.
Second sentence.

The main difference between using \n or endl is that the streams
buffer is flushed, occuring a minor delay potentially. So endl
should only be used when flushing the stream would be a feature.
and \n when not
*/






#include <iostream>
using namespace std;
#include <string>

int main(){

    return 0;
}