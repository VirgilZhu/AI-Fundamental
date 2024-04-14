#include <iostream>
#include <unordered_map>
#include <stack>

using namespace std;

bool isEndState(const string& status, const string& end) {
    return status == end;
}

int dfs(string start) {
    unordered_map<string, int> graph;
    string end = "12345678x";
    stack<pair<string, int>> s;

    if (isEndState(start, end)) return 0;

    s.push({start, 0});
    graph[start] = 0;

    while (!s.empty()) {
        string status = s.top().first;
        int depth = s.top().second;
        s.pop();

        if (isEndState(status, end)) return depth;

        int pos = status.find('x');
        int x = pos / 3, y = pos % 3;
        int dx[4] = {0, 0, -1, 1}, dy[4] = {-1, 1, 0, 0};

        for (int i = 0; i < 4; i++) {
        	if (isEndState(status, end)) return depth;
        	
            int a = x + dx[i], b = y + dy[i];
            if (a >= 0 && a <= 2 && b >= 0 && b <= 2) {
                int cur_pos = a * 3 + b;
                swap(status[pos], status[cur_pos]);
                if (!graph.count(status)) {
                    graph[status] = depth + 1;
                    s.push({status, depth + 1});
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

	if (dfs(input) != -1) cout << 1 << endl;
	else cout << 0 << endl;

    return 0;
}
