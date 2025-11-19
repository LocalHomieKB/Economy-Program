/*Notes

Jump statements: allow altering the flow of a program by 
performing jumps to specific locations.

Break statement: these leave a loop, even if the condition is
not fulfilled. Can be used to end an infinite loop or force
to end it before its natural end.

See "break loop" for more


The continue statement: causes the program to skip the rest
of the loop in the current iteration, as if the end of the
statement block had been reached, causing it to jump to the
start of the following iteration.

See "continue loop" for more


Goto statement: Makes an absolute jump to another point in the
program. This ignores nesting level, and doesn't cause any
automatic stack unwinding. A feature to use with care,
preferably within the same block of statements, especially
in the presence of local variables.

Destination point = label, used as an argument for the goto
statement. Made of a valid identifier followed by a colon

See "go to loop" for more:


//

*/

//Code


//Break loop:

/*
#include <iostream>
using namespace std;

int main ()
{
    for (int n=10; n>0; n--)
    {
        cout << n << ", ";
        if (n==3)
        {
            cout << "countdown aborted!";
            break;
        }
    }
}
*/


//Continue loop:


/*
#include <iostream>
using namespace std;

int main ()
{
    for (int n=10; n>0; n--){
        if (n==5) continue; //all that happens is the number 5
        cout << n << ", ";// is skipped
    }
    cout << "liftoff1\n";
}
*/


// go to loop:

#include <iostream>
using namespace std;

int main ()
{
    int n=10;
mylabel:
    cout << n << ", ";
    n==;
    if (n>0) goto mylabel;
    cout << "liftoff!\n";
}