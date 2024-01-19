#include <bits/stdc++.h>
using namespace std;

class Queue
{
private:
   int maxSize;
   int *a;
   int front = -1, rear = -1;

public:
   Queue(int size)
   {
      maxSize = size;
      a = new int[size];
   }

   bool isFull()
   {
      return rear == maxSize - 1;
   }

   bool isEmpty()
   {
      return front == -1 && rear == -1;
   }

   int enqueue(int n)
   {
      if (!isFull())
      {
         if (rear == -1)
            front = rear = 0;
         else
            rear++;
         a[rear] = n;
         return a[rear];
      }
      else
      {
         cout << "Queue Overflow!" << endl;
         return -1;
      }
   }

   int dequeue()
   {
      if (!isEmpty())
      {
         int temp = a[front];
         if (front == rear)
            front = rear = -1;
         else
            front++;
         return temp;
      }
      else
      {
         cout << "Queue Overflow!" << endl;
         return -1;
      }
   }

   void printItems()
   {
      if (!isEmpty())
      {
         cout << "Queue items: ";
         for (int i = front; i <= rear; i++)
            cout << *(a + i) << " ";
         cout << endl;
      }
      else
         cout << "No elements in the queue." << endl;
   }
};

int main()
{
   int size, option, n, item;
   cout << "Enter queue size: ";
   cin >> size;
   Queue q(size);

   while (true)
   {
      cout << "\nQueue operation:" << endl;
      cout << "1. Enqueue\n2. Dequeue\n3. Is empty?\n4. Is full?\n5. Print items\n0. exit" << endl;
      cout << "select: ";
      cin >> option;
      cout << endl;

      switch (option)
      {
      case 1:
         cout << "Enter a number: ";
         cin >> n;
         item = q.enqueue(n);
         if (item != -1)
            cout << item << " has been enqueued." << endl;

         break;
      case 2:
         item = q.dequeue();
         if (item != -1)
            cout << item << " has been dequeued." << endl;
         break;
      case 3:
         q.isEmpty()
             ? cout << "Queue is empty!" << endl
             : cout << "Queue is not empty!" << endl;
         break;
      case 4:
         q.isFull()
             ? cout << "Queue is full!" << endl
             : cout << "Queue is not full!" << endl;
         break;

      case 5:
         q.printItems();
         break;
      case 0:
         cout << "Operation ended." << endl;
         return 0;
      }
   }
}