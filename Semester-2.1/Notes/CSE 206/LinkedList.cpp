#include <bits/stdc++.h>
using namespace std;

struct node
{
   int data;
   struct node *next;
};

struct node *head = NULL;

void beginsert(int item)
{
   struct node *ptr = new node;
   ptr->data = item;
   ptr->next = head;
   head = ptr;
   printf("\nNode inserted");
}

void endInsert(int item)
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

void delationAtFirst()
{
   if (head != NULL)
   {
      node *temp = head;
      head = head->next;
      free(temp);
   }
}

void delationAtEnd()
{
   if (head != NULL)
   {
      node *previous, *temp = head;
      while (temp->next != NULL)
      {
         previous = temp;
         temp = temp->next;
      }
      previous->next = NULL;
      free(temp);
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
   int choice = 0;
   int item;

   while (1)
   {
      printf("\n\n*********Main Menu*********\n");
      printf("\nChoose one option from the following list ...\n");
      printf("\n===============================================\n");
      printf("\n1.Insert in beginning\n2.Insert in ending\n3.Delation at first\n4.Delation at end\n5.Show\n6.Exit\n");
      printf("\nEnter your choice?: ");
      scanf("%d", &choice);

      switch (choice)
      {
      case 1:
         printf("\nEnter value: ");
         scanf("%d", &item);
         beginsert(item);
         break;

      case 2:
         printf("\nEnter value: ");
         scanf("%d", &item);
         endInsert(item);
         break;

      case 3:
         delationAtFirst();
         break;

      case 4:
         delationAtEnd();
         break;

      case 5:
         display();
         break;

      case 6:
         exit(0);

      default:
         printf("Please enter valid choice..");
      }
   }

   return 0;
}