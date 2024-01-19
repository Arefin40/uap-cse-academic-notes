#include <bits/stdc++.h>
using namespace std;

const int N = 1000;
vector<int> g[N];
bool visited[N];
int level[N];

void BFS(int s)
{
   queue<int> q;
   q.push(s);
   visited[s] = true;

   while (!q.empty())
   {
      int node = q.front();
      q.pop();
      for (auto adjNode : g[node])
      {
         if (!visited[adjNode])
         {
            q.push(adjNode);
            visited[adjNode] = true;
            level[adjNode] = level[node] + 1;
         }
      }
   }
}

int main()
{
   int V, E, v1, v2;
   cin >> V >> E;

   for (int i = 0; i < E; i++)
   {
      cin >> v1 >> v2;
      g[v1].push_back(v2);
      g[v2].push_back(v1);
   }

   BFS(2);

   for (int i = 1; i <= V; i++)
      cout << i << " : " << level[i] << endl;

   return 0;
}