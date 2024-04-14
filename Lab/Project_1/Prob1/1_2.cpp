#include <iostream>
#include <climits>

#define MAX_node 505

using namespace std;

int cost[MAX_node][MAX_node]{{0}};
int dist[MAX_node]{0};

void dijkstra(int start, int n)
{
    bool visited[MAX_node]{false};
    int i, j, k, min;
    for (i = 1; i <= n; i++) {
        dist[i] = cost[start][i];
        visited[i] = false;
    }
    visited[start] = true;

    for (i = 1; i <= n; i++) {
        min = INT_MAX;
        k = 0;
        for (j = 1; j <= n; j++) {
            if (!visited[j]) 
                if (dist[j] != 0 && dist[j] < min) {
                    min = dist[j];
                    k = j;
                } 
        }
        if (k == 0) break;
        
        for (j = 1; j <= n; j++) {
        	if (j == k) continue;
            if (!visited[j] && cost[k][j] < INT_MAX && cost[k][j] != 0) {
                if (dist[k] + cost[k][j] < dist[j] || !dist[j]) {
                    dist[j] = dist[k] + cost[k][j];
                }
            }
        }
        visited[k] = true;
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    
    for (int i = 0; i < m; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        if (cost[x][y] == 0 || cost[x][y] > z) cost[x][y] = z;
    }
    
	if (n == 1) cout << 0 << endl;
	else {
		dijkstra(1, n);
		if (!dist[n]) cout << -1 << endl;
    	else cout << dist[n] << endl;
	}
    return 0;
}