#include <bits/stdc++.h>
using namespace std;

struct node
{
   int data;
   struct node *next = NULL;
};

node *head = NULL;

void insert(int data)
{
   struct node *newNode = new node;
   newNode->data = data;
   newNode->next = NULL;

   if (head == NULL)
      head = newNode;
   else
   {
      struct node *temp = head;
      while (temp->next != NULL)
         temp = temp->next;

      temp->next = newNode;
   }
}

void print()
{
   struct node *temp = head;

   while (temp != NULL)
   {
      cout << temp->data << " ";
      temp = temp->next;
   }
   cout << endl;
}

int main()
{
   int a[]{0, 1, 1, 2, 3, 5, 8, 13};

   for (int i = 0; i < 8; i++)
      insert(a[i]);

   cout << "linked list:" << endl;
   print();

   return 0;
}