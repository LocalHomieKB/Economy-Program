//Notes 
/*

Main is the only function that is expected to end with an 
implicit return statement:

return 0;

All other functions must end with a proper return statement
that includes a return value, even if never used

There are a set of values that main can return. Zero is 
interpreted as the program ending successfully. Also:

EXIT_SUCCESS - program was succesful(defined in header <cstdlib>)
EXIT_FAILURE - program failed (also defined in header <cstdlib>)
*/
//Code

#include <iostream>
using namespace std;

int main() 
{
    return 0;
}