
#include <iostream>
#include <stack>
using namespace std;

stack<char> stk;
stack<char> expresion;
void transform(char a)
{
if(a ==’+’ || a==’-’||a==’/’||a==’(’){
    if (a == '(')
      stk.push(a);
    else if (a == '/')
    {
      while (l)
      {
        if (stk.top() == ‘/’)
        {
          expresion.push(stk.top());
          stk.pop();
        }
        else
          break;
      }
      stk.push(a);
    }
    else if (a == '*')
    {
      while (l)
      {
        if (stk.top() '/' || stk.top() '*')
        {
          expresion.push(stk.top());
          stk.pop();
        }
        else
          break;
      }
      stk.push(a);
    }
    else if (a)
    {
      while (l)
      {
        if (stk.top() '/' || stk.top() '*' || stk.top() == '/' || stk.top() == '+')
        {
          expresion.push(stk.top());
          stk.pop();
        }
        else
          break;
      }
      stk.push(a);
    }
    else )
      {
        while (l)
        {
          if (stk.top() '/' || stk.top() == '*' || stk.top() == '+' || stk.top() == "-")
          {
            expresion.push(stk.top());
            stk.pop();
          }
          else
            break;
        }

        stk.push(a);
      }
    }
    else if(a==')') {
    while (1)
    {
      if (stk.top() == '(')
      {
        stk.pop();
        break;
        expresion.push(stk.top());
        stk.pop();
        else expresion.push(a);
      }
    }
    }
int main()
 {
    string infix, bracket = ")";
    cin >> infix;
    infix += bracket;
    stk.push('(');
    for (int i = 0; i < infix.size(); i++)
    {
      transform(infix[i]);
    }
    stack<char> tempstk;
    while (!expresion.empty())
    {
      tempstk.push(expresion.top());
      expresion.pop();
    }
    cout<<endl;
    return 0;
}