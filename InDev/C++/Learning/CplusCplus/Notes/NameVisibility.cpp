//Name Visibility
/*

Entities such as variables functions and compound types need to be declared before being used in C++, the point in the program where this declaration
happens influences its visibility.

Global Scope - entity declared outside any block, its name is visible anywhere in the code.

Block scope - Entity declared within a block, such as a function or a selective statement. Only visible within the specific block in which it is declared.
^ - Variables with block scope are also known as local variables.

Local variable - Varaibles with block scope, e.g. variable declared in the body of a function, extends until the brace of the function

See example below:

int foo; //Global variable

int some_function()
{
    int bar; // Local variable
    bar = 0;
}

int other_function()
{
    foo = 1; // Works - foo is a global variable
    bar = 2; // wrong - bar is not visible from this function
}

//I honestly never knew this existed

Additionally, in each scope a name can only represent one entity, there cannot be two variables with the same name in the same scope. see below:

int some_function()
{
    int x;
    x=0;
    double x; //Doesn't work, name already used in this scope
    x =0.0;
}

To remember:
    Visibility of an entity with block scope extends until the end of the block, including inner blocks. An inner block because it is a different
    block can re-utilise a name existing in an outer scope to refer to a different entity. The name will refer to a different entity only within the 
    inner block, hiding the entity it names outside. While outside it, it will still refer to the original entity(?).

See "inner block scopes" code for more:

Because x was redefined, the value set for in the inner block, only applies for the length of the inner block, once that is exited out of, the original
outer block value is retained. the y value wasn't redefined, so its value for both inner and outer is 50.

//Namespaces:

Namespaces scope - This is a narrower scope, that allows organising the elements of programs into different logical scopes referred to by names.
See syntax:

namespace identifier
{
    named_entities
}

identifier - any valid identifier

named_entities - set of variables, types and functions that are included within the namespace

see below:

namespace myNamespace
{
    int a,b;
}

variables a and b are normal variables within the namespace scope of myNamespace, they can be accessed within this namespace normally, with their 
identifier, but if accessed from outside it, the scope operator(::) is required. e.g.:

myNamespace::a
myNamespace::b

See "Namespaces" code for more
*/

//Name visibility

/*
#include <iostream>
using namespace std;

int main() {
    int x =10;
    int y =20;
    {
        int x; //inner scope so this works
        x = 50; // sets value to inner x
        y = 50; // sets value to (outer) y
        cout << "inner block:\n";
        cout << "x: " << x << '\n';
        cout << "y: " << y << '\n';
    }
    cout << "outer block:\n";
    cout << "x: " << x << '\n';
    cout << "y: " << y << '\n';
    return 0;
}
*/

//Namespaces:

#include <iostream>
using namespace std;

namespace foo
{
    int value() {return 5; }
}

namespace bar
{
    const double pi = 3.1416;
    double value() { return 2*pi;}
}

int main() 
{
    cout << foo::value() << '\n';
    cout << bar::value() << '\n'; //(personal) These namespaces make so much sense
    cout << bar::pi << '\n'; //This is also accessed from within an namespace but its a variable and not a function.
    return 0;
}