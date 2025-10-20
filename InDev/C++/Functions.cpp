//Notes 
/*

Functions: a group of statements that is given a name, and 
called on during the program. Common syntax:

type name (parameter1, parameter2, ...) { statements }

type - type of value returned by the function

name - identifier by which the function can be called
parameters(as many as needed) - consists of a type followed
by an identifier, which each parameter separated by a comma.
Further:
Each looks like a regular variable declaration, and within
the function acts as a regular variable, local to the function.
Parameters allow passing arguments to the function, from the
location where it was called from.

statements - this is the functions body, a block of statements
surrounded by braces {} that specify what the function does

See function example for more:

See Function example 2 for more:

Void functions: When a function doesn't need to return a value
void is used, represent the absence oif value, a funtion
that just prints a message is an example

see void function for more:

Can also be used like this:

void printmessage(void) //used to indicate no parameters being
{ //called
    cout << "I'm a function!";
}

An empty pair of parentheses is always required, even if no
parameters are called


Mains return value: is the only function that is expected to 
end with an implicit return statement:

return 0;

All other functions must end with a proper return statement
that includes a return value, even if never used

There are a set of values that main can return. Zero is 
interpreted as the program ending successfully. Also:

EXIT_SUCCESS - program was succesful(defined in header <cstdlib>)
EXIT_FAILURE - program failed (also defined in header <cstdlib>)


Arguments passed by value and by reference: Up until now values
were passed as literals or as copies of variables. Whatever
occurs inside of the function leaves the original variables
unchanged.

We can now pass arguments by reference instead of by value.

See example code duplicate for more notes:


Efficiency considerations and const references: By creating
a copy of a large compound type we can run into issues
of overheads. See following:

string concatenate (string a, string b)
{
    return a+b;
}

If we have large strings doing the above function, it may mean
large quantities of date being copied and then added just
for the function call. 

If we instead use references, we can save a lot of time.
See:

string concatenate (string& a, string& b)
{
    return a+b;
}

Here the aliases of the strings are directly operated on, it
might mean the transfer of certain pointers(?), but it is
otherwise more efficient.

Functions with references are generally considered to modify
parameters, they typically do after all. We can go around this
by using const, to guarantee the reference parameters aren't
modified. See:

string concatenate(const string& a, const string& b)
{
    return a+b;
}

Here a and b are used as references but are forbidden from having
their values modified, this makes it efficient and safe.

In cases where the type is simple and short, passing by value
may still be quicker.


Inline functions: Calling a function causes a certain overhead,
for very short functions it may be better to insert the code
of the function where it is called. The specifier inline
informs the compiler that inline expansion is preferred
over the usual function call mechanism. This doesn't change
the functions behaviour it simply means the code generated
by the function shall be inserted at each point the function
is called, instead of being function called. See:

inline string concatenate (const string& a, const string& b
{
    return a+b;
}

This is the only time inline is specified, in the function
declaration.

Most compilers may optimise code to generate inline functions,
they do this automatically for efficiency even if not marked.
the commpiler may even ignore the specifier inline if it thinks
it may be quicker without.

Default values in parameters: Where functions have an extra
parameter, the function can include a default value, if the
function is called with fewer arguments.

See "Default values in functions" code for more:


Declaring function prototypes: Where functions are declared
after main, a proto function can be declared, less
information is passed on, and not necessarily all has to be
used, later when more information is passed to complete
the function. The parameter types are passed, the names
can be specified but don't need to, and don't need to match
those in the function definition.

See "function prototypes" code for more

The program is of course inefficient, however it serves as an
example for how functions can be declared before its definition.

//Recursivity: property of functions having to be called
by themselves. useful for tasks like sorting elements, or
calculating factorials.

to calculate factorials:

n! = n*(n-1)*(n-2)*(n-3)...*1

5! would be:

5! = 5*4*3*2*1=120

The code would look like the example "Factorial calculator",
see the code for more:

Within the definition it is ensured a is larger than 1  if not
we'd have an infinite recursive loop, so the function factorial
has a call for itself, but only when its argument is greater 
than 1

*/
//Code


//Function example 1:

/*
#include <iostream>
using namespace std;

int addition (int a, int b) //Addition is the function name
{ // a and b are parameters fetched from the program
    int r;
    r=a+b;
    return r; //returns a value back outside the function
    // and also ends the function, returning control to main
}

int main() 
{
    int z;
    z = addition (5,3); //Once addition is called, execution
    // of main is stopped, and only resumes once addition ends
    cout << "The result is " << z;
}
*/


//Function example 2:

/*
#include <iostream>
using namespace std;

int subtraction(int a, int b)
{
    int r;
    r=a-b;
    return r;
}

int main() 
{
    int x=5, y=3, z;
    z = subtraction (7,2); // used on demand within variable
    //declaration using literals
    cout << "The first result is " << z << '\n';
    cout << "The second result is " << subtraction (7,2) << '\n';
    cout << "The third result is " << subtraction (x,y) << '\n';
    z= 4 + subtraction (x,y); //used within variable declaration
    //using variables and also as an operand itself
    cout << "The fourth result is " << z << '\n';
}
*/

//Void functions :

/*
#include <iostream>
using namespace std;

void printmessage() 
{
    cout << "I'm a function!";
}

int main ()
{
    printmessage;
}
*/

//Duplicate:

//In this code an external variable will be accessed within
//the function, by passing from reference, the function
//duplicate duplicates the value of its three arguments,
//also causing the variables used as arguments to be modified
//by the call.

/*
#include <iostream>
using namespace std;

void duplicate(int& a, int& b, int& c) //to gain access
{//to its arguments, parameters are declared as references
    a*=2; //indicated by an & following its type
    b*=2;//The parameters are fetched and are now permanently
    c*=2;//modified. a,b and c are essentially aliases
}//for whatever arguments will be passed on. if no & was used
//Then a b and c would be doubled.
int main() 
{
    int x=1, y=3, z=7;
    duplicate (x,y,z); //Here the variables are fetched
    //and are duplicated into a,b and c in the function
    cout << "x=" << x << ", y=" << y << ", z=" <<z;//and
    return 0;//doubled
}
*/

// Default values in parameters:

/*
#include <iostream>
using namespace std;

int divide (int a, int b=2)
{
    int r;
    r=a/b;
    return(r);
}

int main() 
{
    cout << divide(12) <<'\n'; //Theres only one argument
    //passed, the default value 2 is assumed to be the second
    //parameter
    cout << divide(20,4) <<'\n';//here the default is ignored.
    return 0;
}
*/

//Function prototypes:

/*
#include <iostream>
using namespace std;

void odd(int x);//these are protofunctions, they contain everything
void even(int x); //needed to call them, their name, types of their
//arguments, and their return type(void). This allows us to
//place main before their definitions
int main() 
{
    int i;
    do{
        cout << "Please, enter number(0 to exit): ";
        cin >> i;
        odd(i);
    } while (i!=0);
    return 0;
}

void odd (int x)
{
    if ((x%2)!=0) cout << "It is odd.\n";
    else even (x);
}

void even (int x)
{
    if ((x%2)==0) cout << "It is even.\n";
    else odd (x);
}
*/

// Factorial calculator:

#include <iostream>
using namespace std;

long factorial(long a)
{
    if (a>1)
        return (a*factorial(a-1));
    else
        return 1;
}

int main() 
{
    long number = 9;
    cout << number << "! = " << factorial (number);
    return 0;
}