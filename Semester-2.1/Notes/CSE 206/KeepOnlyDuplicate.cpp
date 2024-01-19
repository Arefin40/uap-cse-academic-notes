#include <bits/stdc++.h>
using namespace std;

int main()
{
   int a[]{2, 0, 3, 0, 1, 0, 0, 1};
   int size = sizeof(a) / sizeof(a[0]);

   for (int i = 0; i < size; i++)
   {
      // optional optimization
      if (a[i] == INT_MIN)
         continue;

      bool duplicate = false;
      for (int j = i + 1; j < size; j++)
      {
         if (a[i] == a[j])
         {
            duplicate = true;
            a[j] = INT_MIN;
         }
      }
      if (!duplicate)
         a[i] = INT_MIN;
   }

   for (int i : a)
      if (i != INT_MIN)
         cout << i << " ";
   cout << endl;

   return 0;
}