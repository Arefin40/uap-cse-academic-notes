#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> g;
vector<int> color;

void printAdjacencyList(int E)
{
   for (int i = 0; i < E; i++)
   {
      cout << i << " => ";
      for (auto adjNode : g[i])
         cout << adjNode << " ";
      cout << endl;
   }
}

bool isBipartite(int s)
{
   queue<int> q;
   q.push(s);
   color[s] = 0;

   while (!q.empty())
   {
      int node = q.front();
      q.pop();

      for (auto adjNode : g[node])
      {
         if (color[adjNode] == -1)
         {
            q.push(adjNode);
            color[adjNode] = !color[node];
         }
         else if (color[adjNode] == color[node])
            return false;
      }
   }
   return true;
}

int main()
{
   int N, E, u, v;
   cin >> N >> E;
   g = vector<vector<int>>(N);
   color = vector<int>(N, -1);

   for (int i = 0; i < E; i++)
   {
      cin >> u >> v;
      g[u].push_back(v);
      g[v].push_back(u);
   }

   isBipartite(0)
       ? cout << "Bipartite" << endl
       : cout << "Not Bipartite" << endl;

   return 0;
}