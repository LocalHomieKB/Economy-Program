//Notes 
/*
In C++ two different functions can have the  same name  if
their parameters are different, either because they
have a different number of parameters or because
any of their parameters are of a different type.

See "overloading functions" code for more.

An overloaded function must have at least one parameter
of a different type, return type is not enough.

Function templates: Wheref functions have different types
but the exact same body, function templates can be used
The difference is template is used preceding, and template
parameters in angle-brackets are used, see below:

template <class SomeType>
SomeType sum (SomeType a, SomeType b)
{
    return a+b;
}

SomeType is a generic type, and it can be used for the type
of parameters, the return type, or to declare new 
variables of this type. It is a generic type determined
the moment the template is instantiated.

Instantiating a template is done by calling the function
template, using the same syntax as calling a regular function
but specifying the template arguments in angle brackets.

To call the sum function above, you can call it with the
code below:

x = sum<int>(10,20);

int could be any number of instantiations, this example
replaces each occurence of SomeType with int. So you could 
imagine that what was the protofunction, could now be
visualised as:

int sum(int a, int b)
{
    return a+b;
}

See "function template code" for more. Notes on the code
follow:

Here T is used instead of SomeType, it is functionally
the same, T is a common template parameter for generic
types. Sum was used for two different types, the compiler
called the appropriate one each time.

Because T is also used as a local variable of that
generic type within the sum, it means the variable
will be of the same type as parameters a and b, and the
type returned by the function.

In this specific case, it is also enough to write:

k = sum(i,j); instead of k =sum<int>(i,j);

As the generic type T was used as a parameter for sum, 
meaning the data type is automatically determined. If 
sum is called with arguments of different types
the compiler may not be able to deduce the type of T 
automatically.

See "function templates 2 code", notes for it follow:

In the example two generic types of T and U are used.
Thanks to this, when two different numbers of 10 and 10.0
are used the compiler knows to define one as int and the
other as double.


Non-type template arguments:

Template parameters can not only include types 
introduced by class or typename, but can also
include expressions of a particular type.

See "template arguments" code for more, notes follow here:

The second argument of fixed_multiply function temmplate
is of type int, it looks like a regular function parameter
and can be used like one.

The main difference is, the value of template parameters
is determined on compile-time to generate a different
instantiation of the function fixed_multiply, thus the value
of that argument is never passed during runtime. The two
calls to the function, call two versions of it, one that
always multiplies by two, and one that always multiplies
by three. For the same reason, the second template
argument needs to be a constant expression, it cannot be
passed a variable.
*/
//Code


//Overloading functions:

/*
#include <iostream>
using namespace std;

int operate (int a, int b)
{
    return (a*b);
}
//These two functions have entirely different operations
//they perform, this is bad practice, but it proves
//that the same name with different parameter types
//can perform different operations, for actual use
//use similar operations for the same name
double operate (double a, double b)
{
    return (a/b);
}

int main() 
{
    int x=5,y=2; //When this type is passed the compiler knows
    //to use the operate with two int parameters
    double n=5.0,m=2.0; //when this type is passed
    //the compiler knows to use operate with two doubles
    cout << operate(x,y) << '\n';
    cout << operate (n,m) << 'n';
    return 0;
}
*/

//Function Template:

/*
#include <iostream>
using namespace std;

template <class T>
T sum (T a, T b)
{
    T result;
    result = a + b;
    return result;
}

int main() 
{
    int i =5, j =6, k;
    double f=2.0, g=0.5, h;
    k=sum<int>(i,j);
    h=sum<double>(f,g);
    cout << k << '\n';
    cout << h << '\n';
    return 0;
}
*/

//Function templates 2:

/*
#include <iostream>
using namespace std;

template <class T, class U>
bool are_equal (T a, U b)
{
    return (a==b);
}

int main() 
{
    if (are_equal(10,10.0))
        cout << "x and y are equal\n";
    else   
        cout << "x and y are not equal\n";
    return 0;
}
*/

//Template arguments:

#include <iostream>
using namespace std;

template <class T, int N>
T fixed_multiply(T val)
{
    return val * N;
}

int main() 
{
    std::cout << fixed_multiply<int,2>(10) << '\n';
    std::cout << fixed_multiply<int,3>(10) <<'\n';
}