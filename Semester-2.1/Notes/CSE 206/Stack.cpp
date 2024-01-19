#include <bits/stdc++.h>
using namespace std;

class Stack
{
private:
   int *a;
   int capacity = 10;
   int top = -1;

public:
   Stack(int _size_)
   {
      capacity = _size_;
      a = new int[_size_];
   }

   int size()
   {
      return top + 1;
   }

   bool isFull()
   {
      return top == capacity - 1;
   }

   bool isEmpty()
   {
      return top == -1;
   }

   int peek()
   {
      return a[top];
   }

   bool isPeek(int n)
   {
      return a[top] == n;
   }

   int push(int n)
   {
      if (!isFull())
      {
         top += 1;
         a[top] = n;
         return a[top];
      }
      else
      {
         cout << "Stack overflow!" << endl;
         return -1;
      }
   }

   int pop()
   {
      if (!isEmpty())
      {
         int item = a[top];
         top -= 1;
         return item;
      }
      else
      {
         cout << "Stack underflow!" << endl;
         return -1;
      }
   }

   void printAll()
   {
      if (!isEmpty())
      {
         cout << "\nStack items:" << endl;
         for (int i = 0; i <= top; i++)
            cout << *(a + i) << " ";
         cout << endl;
      }
      else
         cout << "No items left in the stack!" << endl;
   }
};

int main()
{
   int sz, n, item, option;

   cout << "Enter stack size: ";
   cin >> sz;
   Stack st(sz);

   while (true)
   {
      cout << "\nStack operation:\n1. Push item\n2. Pop item\n3. View Top\n4. Check if the stack is full?\n5. Check if the stack is empty?\n0. Exit" << endl;
      cout << "select: ";
      cin >> option;

      cout << endl;

      switch (option)
      {
      case 1:
         cout << "Enter a number: ";
         cin >> n;
         st.push(n);
         st.printAll();
         break;

      case 2:
         st.pop();
         st.printAll();
         break;

      case 3:
         if (st.peek() != -1)
            cout << "Top item: " << st.peek() << endl;
         else
            cout << "No element in Stack." << endl;
         break;

      case 4:
         if (st.isFull())
            cout << "Stack is full." << endl;
         else
            cout << "Stack is not full." << endl;
         break;

      case 5:
         if (st.isEmpty())
            cout << "Stack is empty." << endl;
         else
            cout << "Stack is not empty." << endl;
         break;

      case 0:
         cout << "Program terminated!" << endl;
         return 0;
      }
   }

   return 0;
}