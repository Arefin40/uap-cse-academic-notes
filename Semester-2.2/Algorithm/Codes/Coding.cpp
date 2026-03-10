#include <bits/stdc++.h>
using namespace std;

#define endl "\n"

void solve()
{
   int p, x, y;
   bool u = 0, d = 0, l = 0, r = 0;
   vector<int> v;

   cin >> p;
   while (p--)
   {
      cin >> x >> y;

      if (y != 0)
         y > 0 ? u = 1 : d = 1;

      if (x != 0)
         x < 0 ? l = 1 : r = 1;
   }

   if (u && d && l && r)
      cout << "NO" << endl;
   else
      cout << "YES" << endl;
}

int main()
{
   int t;
   cin >> t;

   while (t--)
      solve();

   return 0;
}