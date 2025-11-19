//  NOTES:

/*

    Flow control statements: these serve to specify what has
    to be done by the program, when, and under which conditions.
    These typically require (sub)statements as part of its 
    syntax. These may be either a simple c++ statement. 
    Or a compound statement.
    
    Compound statement: A group of statements each terminated
    by its own semicolon, but all grouped together in a block.
    enclosed in curly braces: {}:
    {statement1; statement2; statement3; }
    This whole block is considered a single statement.

selection statements:

    if: used to execute statements slash block if and only if
    a condition is fulfilled. Syntax:

    if (condition) statement

    If condition is true its executed, if not it is ignored.
    example:

    if (x == 100)
        cout << "x is 100";

    if x is not exactly 100 it is ignored.

    For multiple statements to be executed enclose in braces as
    follows:

    if (x == 100)
    {  
        cout << "x is ";
        cout << x;    
    }

    This code could also be written as follows, worsening
    readibility:

    if (x == 100) { cout << "x is "; cout << x; }


    Else: used to introduce an alternate statement when condition
    is not fulfilled. syntax:

    if (condition) statement1 else statement2

    This means condition 1 is executed if condition is true,
    if not, statement 2 is executed. Example:

    if (x == 100)
        cout << "x is 100";
    else
        cout << "x is not 100";

    By combining several else and ifs, multiple conditions can
    be checked. Example:

    if (x > 0)
        cout << "x is positive";
    else if (x < 0)
        cout << "x is negative";
    else
        cout << "x is 0";


    Iteration statements(loops): loops repeat a statement
    a certain number of times, or while a condition is 
    fulfilled. And whose keywords are while, do and for.

    While: Its syntax:

    while (expression) statement

    repeats a statement while expression is true. If after any
    execution of statement expression is no longer true, the 
    loop ends, and the program continues after the loop.
    For example see "countdown while code"

    Do while: The difference between this and a typical while
    loop is that the condition is evaluated after rather
    than before the execution of the statement. This means
    it will be executed at least once, even if the condition
    wasn't ever fulfilled. See "echo machine" for example code.

    for loop: Designed to iterate a number of times. Its syntax:

    for (initialisation; condition; increase) statement;

    breakdown as follows:
    1: initalisation: generally a counter variable, sets to some
    initial value, executed a single time, at the beginning
    2: condition: this is checked, if true it continues, otherwise
    the loop ends and statement is skipped.
    3: statement: this is executed, either a single statement
    or a block
    4: increase: this is executed and the loop goes back to condition
    5: end: next statement after loop continues

    For more on for loops see "better countdown with for loops"

    Commas what are they good for loops: Commas can be used
    inside of the for block of conditions, its an expression
    separator, and can separate multiple expressions where
    one is generally expected. This can be used to hold two
    counter variables for example, initialising and increasing
    both example:

    for () n=0, i=100 ; n!=i ; ++n, --i ) //note the n and i
    {
        ...
    }

    if the loop doesn't modify n or i it will be executed 50
    times.

    See "echo chamber" for more


    Range based for loop: The syntax is as follows:

    for (declaration : range) statement;

    this kind of loop iterates over all the elements in range,
    where declaration declares a variable able to take the value
    of an element in this range. Ranges are sequences of elements
    including arrays, containers and any other type suupporting
    the functions begin and end. Strings for example.

    for more see "range based for loop using strings"

    Notes on the code: Within the for loop compound code, the
    char variable is declared(a type of string), this variable
    c in the statement block to represent the value of each in
    the elements in the range. This loop is automatic and does
    not require the explicit declaration of any counter variable

    "auto" can also be used, and deduces the type needed. 
    Example:

    for (auto c : str)
        cout << "[" << c << "]";

    Here the type of c is deduced at the type of the elements in str
    
*/

//Code


//Custom countdown using while
/*
#include <iostream>
using namespace std;

int main()
{
    int n = 10;

    while (n>0) {
        cout << n << ", ";
        --n;
    }

    cout << "liftoff!\n";
}

//every time n is printed it gets smaller by one. eventually
//it will hit 0 and thus the loop ends, the main code follows.
*/


//echo machine

/*
#include <iostream>
#include <string>
using namespace std;

int main ()
{
    string str;
    do{
        cout << "Enter text: ";
        getline (cin,str);
        cout << ("You entered; ") << str << "\n";
    } while (str != "goodbye"); // very different to python
}
*/

//This code repeats what the user types until they type goodbye
//it then repeats goodbye, the do loop breaks, and then the 
//program ends.


//better countdown with for loops

/*
#include <iostream>
using namespace std;

int main()
{
    for (int n=10; n>0; n--){
        cout << n << ", ";
    }
    cout << "liftoff!\n"; //this code seems very condensed
} //particularly in comparison to python
*/

// the three fields are optional, can be left empty, but
//semicolons are always required. the loop (;n<10;) is one
//without initialisation or increase,(equivalent to a while loop)
//The loop (;n<10;++n) is one with increase but no initalisation
//(Maybe variable was initialised earlier). A loop with no condition
//is equivalent to an infinite loop, with true as its condition
//permanently


//Range based for loops:

/*
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string str {"Hello!"};
    for (char c : str)
    {
        cout << "[]" << c << "]";
    }
    cout << "\n";
}
*/

