#include <bits/stdc++.h>
using namespace std;

struct node
{
   int data;
   struct node *next;
   struct node *prev;
};

struct node *head;
struct node *temp;

void beginsert(int data)
{

   struct node *newNode = new node;
   newNode->data = data;
   newNode->next = head;
   newNode->prev = NULL;
   if (head != NULL)
   {
      head->prev = newNode;
   }
   head = newNode;

   printf("\nNode inserted");
}

void endInsert(int data)
{
   struct node *newNode = new node;
   newNode->data = data;
   newNode->next = NULL;
   if (head == NULL)
   {
      beginsert(data);
   }
   else
   {
      temp = head;
      while (temp->next != NULL)
      {
         temp = temp->next;
      }
      newNode->prev = temp;
      temp->next = newNode;
   }
}

void insertat(int index, int Data)
{

   struct node *newNode;

   if (index == 0)
   {
      beginsert(Data);
   }

   else
   {

      newNode->data = Data;
      int count = 0;

      while (count < index)
      {
         temp = temp->next;
         count++;
      }

      newNode->next = temp->prev->next;
      newNode->prev = temp->prev;
      temp->prev->next = newNode;
      temp->prev = newNode;
   }
}
void delationAtFirst()
{
   if (head != NULL)
   {
      node *temp = head;
      head = head->next;
      head->prev = NULL;
      free(temp);
   }
}
void delationAtEnd()
{
   if (head != NULL)
   {
      node *temp = head;
      while (temp->next != NULL)
      {

         temp = temp->next;
      }

      temp->prev->next = NULL;
      free(temp);
   }
}

void delationAt(int index)
{
   if (index == 0)
      delationAtFirst();
   else if (head != NULL)
   {
      node *temp = head;
      int count = 0;
      while (count < index)
      {

         temp = temp->next;
         count++;
      }

      temp->prev->next = temp->next;
      free(temp);
   }
}

void print()
{
   struct node *ptr = head;

   printf("\nprinting values . . . . .\n");
   while (ptr != NULL)
   {
      printf("%d -> ", ptr->data);
      ptr = ptr->next;
   }
}

void searchByValue(int value)
{
   temp = head;
   int found = 0;
   int i = 0;
   while (temp != NULL)
   {
      if (temp->data == value)
      {
         found = 1;
         break;
      }
      i++;
   }
   if (found)
   {
      cout << i << endl;
   }
   else
      cout << "Not found" << endl;
}

void searchByPosition(int position)
{
}

void printInReverseNode()
{
   struct node *ptr = head;
   while (ptr->next != NULL)
   {
      ptr = ptr->next;
   }
   printf("\nprinting values . . . . .\n");
   while (ptr != NULL)
   {
      printf("%d -> ", ptr->data);
      ptr = ptr->prev;
   }
}

int main()
{
   int choice = 0;
   int index, newElement, data;

   while (1)
   {
      printf("\n\n*********Main Menu*********\n");
      printf("\nChoose one option from the following list ...\n");
      printf("\n===============================================\n");
      printf("\n1.Insert in beginning\n2.Insert in ending\n3.Insert At\n4.Delation at first\n5.Delation at end\n6.Delation at\n7.Show\n8.Search by Value\n9.Print in reverse order\n 10.Exit\n");
      printf("\nEnter your choice?: ");
      scanf("%d", &choice);

      switch (choice)
      {
      case 1:
         cout << "Enter value: ";
         cin >> data;
         beginsert(data);
         break;

      case 2:

         cout << "Enter value: ";
         cin >> data;

         endInsert(data);
         break;

      case 3:
         printf("Enter index: ");
         scanf("%d", &index);
         printf("Enter elemrnt: ");
         scanf("%d", &newElement);

         insertat(index, newElement);
         break;
      case 4:
         delationAtFirst();
         break;
      case 5:
         delationAtEnd();
         break;
      case 6:
         printf("Enter position: ");
         scanf("%d", &index);
         delationAt(index);
         break;
      case 7:
         print();
         break;
      case 8:
         int value;
         printf("Enter value: ");
         scanf("%d", &value);
         searchByValue(value);
         break;
      case 9:

         printInReverseNode();
         break;
      case 10:

         return 0;
         break;

      default:
         printf("Please enter valid choice..");
      }
   }

   return 0;
}