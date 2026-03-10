#include <bits/stdc++.h>
using namespace std;

int findIndex(string &str, string &pattern)
{
   int index = -1;
   int n = str.size(), m = pattern.size();

   for (int i = 0; i + m <= n; i++)
      if (str.substr(i, m) == pattern)
         index = i;

   return index;
}

int main()
{
   string str1 = "Delicate";
   string str2 = "cat";

   cout << findIndex(str1, str2) << endl;

   return 0;
}