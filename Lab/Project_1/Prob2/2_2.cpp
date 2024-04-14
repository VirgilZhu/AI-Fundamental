#include <iostream>
#include <queue>
#include <unordered_map>

using namespace std;

int bfs(string start) {
    queue<string> q;
    unordered_map<string, int> dist;
    dist[start] = 0;
    
    q.push(start);
    string end = "12345678x";

    while (!q.empty()) {
        string status = q.front();
        q.pop();
        int distance = dist[status];
        if (status == end) return distance;
        
		int pos = status.find('x');
        int x = pos / 3, y = pos % 3;
        int dx[4] = {0, 0, -1, 1}, dy[4] = {-1, 1, 0, 0};

        for (int i = 0; i < 4; i++) {
            int a = x + dx[i], b = y + dy[i];
            if (a >= 0 && a <= 2 && b >= 0 && b <= 2) {
                int cur_pos = a * 3 + b;
                swap(status[pos], status[cur_pos]);                
                if (!dist.count(status)) {
                    dist[status] = distance + 1;
                    q.push(status);
                }
                swap(status[pos], status[cur_pos]);
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
        n++;
    }

    cout << bfs(input) << endl;

    return 0;
}