#include <iostream>
#include <vector>
#include <queue>

#define MAX_node 150001

using namespace std;

struct edge
{
    int v;      /* 边的终点 */
	int len;
};

struct node
{
    int dist, idx;
    bool operator>(const node& a) const		/* 为优先队列重载函数 */
    {
        return dist > a.dist;
    }
};

vector<edge> edges[MAX_node];
int dist[MAX_node];
bool visited[MAX_node]{false};
priority_queue<node, vector<node>, greater<node>> q;

void dijkstra(int start)
{
    dist[start] = 0;
    q.push({0, start});
    
    while (!q.empty()) {
        int idx = q.top().idx;
        q.pop();
        if (visited[idx]) continue;
        visited[idx] = true;
                
        for (auto& ed : edges[idx]) {
            int v = ed.v, len = ed.len;
            if (dist[v] > dist[idx] + len) {
                dist[v] = dist[idx] + len;
                q.push({dist[v], v});
            }
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    
    for (int i = 0; i < m; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        edge ed;
        ed.v = y;
        ed.len = z;
        edges[x].push_back(ed);
    }
    
    memset(dist, 0x3f, sizeof(dist));		/* 初始化所有边长为INT_MAX */

	if (n == 1) cout << 0 << endl;
	else {
		dijkstra(1);
		if (dist[n] == INT_MAX) cout << -1 << endl;
    	else cout << dist[n] << endl;
	}
    return 0;
}