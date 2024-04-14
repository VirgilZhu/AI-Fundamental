#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

struct Compare {
    bool operator()(const pair<string, int>& a, const pair<string, int>& b) {
        return a.second > b.second;
    }
};

int dijkstra(string start) {
    priority_queue<pair<string, int>, vector<pair<string, int>>, Compare> pq;
    unordered_map<string, int> distance;
    unordered_map<string, bool> visited;
    
    distance[start] = 0;
    visited[start] = false;
    pq.push({start, 0});
    string end = "12345678x";

    while (!pq.empty()) {
        string status = pq.top().first;
        int cur_distance = pq.top().second;
        pq.pop();
		
		if (visited[status]) continue;
		visited[status] = true;
		
        int pos = status.find('x');
        int x = pos / 3, y = pos % 3;
        int dx[4] = {0, 0, -1, 1}, dy[4] = {-1, 1, 0, 0};

        for (int i = 0; i < 4; ++i) {
            int a = x + dx[i], b = y + dy[i];
            if (a >= 0 && a <= 2 && b >= 0 && b <= 2) {
                int cur_pos = a * 3 + b;
                string next_status = status;
                swap(next_status[pos], next_status[cur_pos]);
                int new_distance = cur_distance + 1;
                if (visited.find(next_status) == visited.end() || !visited[next_status] || (visited[next_status] && new_distance < distance[next_status])) {
                    visited[next_status] = false;
					distance[next_status] = new_distance;
                    pq.push({next_status, new_distance});
                }
                if (next_status == end) {
           			return new_distance;
        		}
            }
        }
    }
    return -1;
}

int main() {
    string input = "";
    int n = 0;
    while (n < 9) {
        string c;
        cin >> c;
        input += c;
        ++n;
    }

    cout << dijkstra(input) << endl;

    return 0;
}
