#include <bits/stdc++.h>
using namespace std;

class Stack
{
private:
   char *a;
   int top = -1;
   int maxSize;

public:
   Stack(int n)
   {
      a = new char[n];
      maxSize = n;
   }

   bool isFull()
   {
      return top + 1 == maxSize;
   }

   bool isEmpty()
   {
      return top == -1;
   }

   void push(char c)
   {
      top++;
      a[top] = c;
   }

   char pop()
   {
      char temp = a[top];
      top--;
      return temp;
   }

   char peek()
   {
      return a[top];
   }

   int size()
   {
      return maxSize;
   }
};

int main()
{
   char c;
   string s;
   cout << "Enter a string of paranthesis" << endl;
   cin >> s;
   Stack st(s.length());

   for (char c : s)
   {

      if (c == '{')
         st.push('{');
      else
      {
         if (!st.isEmpty())
            st.pop();
         else
         {
            cout << "InValid Paranthesis Expression" << endl;
            return 0;
         }
      }
   }

   st.isEmpty()
       ? cout << "Valid Paranthesis Expression" << endl
       : cout << "InValid Paranthesis Expression" << endl;

   return 0;
}