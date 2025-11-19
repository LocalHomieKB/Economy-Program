/*Operators:

    Assignment (=)

    x=5;
    5 is assigned to x, assignment ALWAYS occurs from right to left

    x = y;
    assigns x the value contained in y
    This only includes the value at time of operation, any changes thereafter dont matter

    These also function this way:
    y = 2 + (x=5);
    this is the same as:
    x = 5;
    y = 2 + x;

    x = y = z = 5;
    this assigns 5 to all three

    Regular arithmetic operators follow..

    increment and decrement(++ --):
    ++x; is also equal to:
    x+=1;
    x=x+1;

    Their order matters:
    ++x affects the final value, while x++ affects the initial value
    example:
    x = 3;
    y ++x;
    // x contains 4, y contains 4

    x = 3;
    y = x++;
    // x contains 4, y contains 3



    Comparatives:
    (7 == 5)     // evaluates to false
    (5 > 4)      // evaluates to true
    (3 != 2)     // evaluates to true
    (6 >= 6)     // evaluates to true
    (5 < 5)      // evaluates to false
    These are self explanatory^

    This can also be used for variables
    a = 2, b=3, c=6
    (a == 5)
    (a*b >= c)
    (b+4 > a*c)
    ((b=2) == a)

    
    Logical operators:
    !:
    Whatever the answer is, it flips it
    !(5 == 5) //evaluates false, since the expression to the right is true
    !true   //evaluates to false

    &&(and) yields true if both operands are true, false otherwise
    e.g. a = true b = true a&&b would result in true
    if a = false b = true a&&b would result in false

    ||(or) yields true if either operand is true
    
    examples:
    ((5 == 5) && (3>6)) -- false is the answer
    ((5 == 5) || (3 > 6) ) -- true is the answer

    Short circuit evaluation:
    C++ evaluates from left to right, for &&, if the left side isn't true, then it doesn't evaluate the right side
    for ||, if the left side is true it doesn't evaluate the right.
    This is important in cases where ++ is used, as this action won't occur under these conditions

    
    Conditional ternary operator(?):

    evaluates an expression, and returns one value if its true, or another if its false.
    example:

    7==5 ? 4:3 evaluates to 3 since 7 is not equal to 5
    7==5+2 ? 4:3 evaluates to 4 since 7 is equal to 5+2
    5>3 ? a:b evaluates to a since 5 is greater than 3
    a>b ? a:b evaluates to whichever is greater a or b


    Comma operator(,)
    a = (b=3, b+2);
    This would first assign 3 to be, then assign b+2 to a


    Bitwise operators...


    Explicit type casting operator:

    converting a value of a given type to another type
    precede the expression to be converted by the new type in ()

    int i;
    float f = 3.14;
    i = (int)f;

    converted into int 3.14 which would be 3

    i = int(f); // also valid

    
    sizeof:

    accepts one parameter, either type or variable, returns size in bytes

    x = sizeof(char);

    x is assigned 1 as char has size of one byte

    value returned by sizeof is setermined before program execution


    Order of operators:

    When an expression has multiple operators, their order has to be considered

    examples:

    x = 5 + 7 & 2;
    x = 5 + (7&2);  x = 6
    x = (5+7) & 2;  x = 0

    The first one is because & has precedence over +, rest self explanatory

    Full order of operators:
    scope ::
    postfix ++ --, (), [], . ->
    prefix ++ --, ~ !, + -, & *, new delete, sizeof, (type) (done right to left)
    pointer-to-member .*, ->* (access pointer)
    arithmetic: scaling *, /, % 
    arithmetic: addition +, -
    bitwise shift <<, >>
    relational <, >, <=, >=
    equality: ==, !=
    and: &
    exclusive or: ^
    inclusive or: |
    conjuction: && (logical and)
    disjunction: || (logical or)
    assignment level expressions: =, *=, /=, %=, +=, -=, >>=, 
    <<=, &=, ^=, |=, ?: (right to left)
    Sequencing : ,

    Whenever an expression has two operators with the same precedence level
    grouping determines which one is evaluated first, (left to right for all except specified)
*/