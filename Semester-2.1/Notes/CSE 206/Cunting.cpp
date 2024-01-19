#include <bits/stdc++.h>
using namespace std;

int main()
{
   int a[]{1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1};
   int size = sizeof(a) / sizeof(a[0]);

   int count = 0;
   for (int i = 0; i < size; i++)
   {
      if (a[i] == 1)
         count++;
   }

   cout << count << endl;
   return 0;
}