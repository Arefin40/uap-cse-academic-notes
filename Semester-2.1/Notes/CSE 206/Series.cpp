#include <bits/stdc++.h>
using namespace std;

int item(int n)
{
   if (n <= 1)
      return 0;
   return 1 + item(n - 1) + item(n - 2) + item(n - 3);
}

int main()
{
   for (int i = 1; i < 10; i++)
      cout << item(i) << " ";
   cout << endl;
   return 0;
}