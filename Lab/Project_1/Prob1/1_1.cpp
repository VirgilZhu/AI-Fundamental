#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

int bfs(map<int, vector<int>>& neighbor, int start, int end) {
    if (start == end) return 0;
    
    queue<int> q;
    q.push(start);
    map<int, bool> visited;
    
    int distance = 0;
    while (!q.empty()) {
        int size = q.size();
        distance++;
        for (int i = 0; i < size; ++i) {
            int node = q.front();
            q.pop();
            visited[node] = true;
            for (auto& neighbor_node : neighbor[node]) {
                if (neighbor_node == end)
                    return distance;
                if (!visited[neighbor_node]) {
                    q.push(neighbor_node);
                }
            }
        }
    }
    return -1;
}

int main() {
    int n, m;
    cin >> n >> m;
    map<int, vector<int>> neighbor;
    
    for (int i = 1; i <= m; i++) {
        int x, y;
        cin >> x >> y;
        neighbor[x].push_back(y);
    }
    
    int result = bfs(neighbor, 1, n);
    cout << result << endl;
    
    return 0;
}
