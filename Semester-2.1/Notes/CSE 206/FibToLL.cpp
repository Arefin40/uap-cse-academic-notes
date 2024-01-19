#include <bits/stdc++.h>
using namespace std;

struct node
{
   int data;
   struct node *next;
};

struct node *head = NULL;

void insert(int item)
{
   struct node *newNode = new node;
   newNode->data = item;
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

void display()
{
   struct node *ptr = head;

   printf("\nprinting values . . . . .\n");
   while (ptr != NULL)
   {
      printf("%d -> ", ptr->data);
      ptr = ptr->next;
   }
}

int main()
{
   int a[]{0, 1, 1, 2, 3, 5, 8, 13, 21, 34};

   for (int i = 0; i < 10; i++)
      insert(a[i]);

   display();

   return 0;
}