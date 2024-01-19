#include <bits/stdc++.h>
using namespace std;

class CircularQueue
{
private:
   int *a, size;
   int front = -1, rear = -1;

public:
   CircularQueue(int sz)
   {
      a = new int[sz];
      size = sz;
   }

   bool isEmpty()
   {
      return front == -1;
   }

   bool isFull()
   {
      return (front == 0 && rear == size - 1) || (front == rear + 1);
   }

   void enque(int n)
   {
      if (!isFull())
      {
         if (front == -1 && rear == -1)
            front = rear = 0;
         else if ((rear + 1) == size)
            rear = 0;
         else
            rear++;
         a[rear] = n;
      }
      else
         cout << "Queue Overflow" << endl;
   }

   int dequeue()
   {
      if (!isEmpty())
      {
         int temp = a[front];
         if (front == rear)
            front = rear = -1;
         else if (front == size - 1)
            front = 0;
         else
            front++;
         return temp;
      }
      else
      {
         cout << "Queue underflow" << endl;
         return -1;
      }
   }

   void printItem()
   {
      if (!isEmpty())
      {
         if (rear >= front)
         {
            for (int i = front; i <= rear; i++)
               cout << a[i] << " ";
            cout << endl;
         }
         else
         {
            for (int i = front; i < size; i++)
               cout << a[i] << " ";
            for (int i = 0; i <= rear; i++)
               cout << a[i] << " ";

            cout << endl;
         }
      }
   }
};

int main()
{
   int size, option, n;
   cout << "Enter size: ";
   cin >> size;

   CircularQueue cq(size);

   while (true)
   {
      cout << "\nCircular Queue Operation:" << endl
           << "1. Enquqe\n2. Dequeue\n3. IsEmpty?\n4. IsFull?\n5. Print items\n0. Exit" << endl;
      cout << "select: ";
      cin >> option;
      cout << endl;

      switch (option)
      {
      case 1:
         cout << "Enter a number: ";
         cin >> n;
         cq.enque(n);
         break;

      case 2:
         n = cq.dequeue();
         if (n != -1)
            cout << n << " has been dequeued." << endl;
         break;

      case 3:
         if (cq.isEmpty())
            cout << "Queue is empty." << endl;
         else
            cout << "Queue is not empty." << endl;
         break;

      case 4:
         if (cq.isFull())
            cout << "Queue is full." << endl;
         else
            cout << "Queue is not full." << endl;
         break;

      case 5:
         cq.printItem();
         break;

      case 0:
         cout << "Operation closed" << endl;
         return 0;
      }
   }

   return 0;
}