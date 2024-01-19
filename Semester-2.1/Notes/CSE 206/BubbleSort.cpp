#include <bits/stdc++.h>
using namespace std;

void BubbeSort(array<int, 9> &a)
{
   int temp, i, j;

   for (i = 0; i < a.size(); i++)
   {
      for (j = 0; j < a.size() - 1 - i; j++)
         if (a[j] > a[j + 1])
            swap(a[j], a[j + 1]);
   }
}

void printArray(array<int, 9> &a)
{
   for (int n : a)
      cout << n << " ";
   cout << endl;
}

int main()
{
   array<int, 9> a = {3, 4, 2, 1, 9, 8, 7, 6, 5};
   BubbeSort(a);
   printArray(a);
   return 0;
}