#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

bool isSolvable(string status) {
    int inversions = 0;
    for (int i = 0; i < 9; ++i) {
        if (status[i] == 'x') continue;
        for (int j = i + 1; j < 9; ++j) {
            if (status[j] != 'x' && status[j] < status[i]) ++inversions;
        }
    }
    return inversions % 2 == 0;
}

int eucDist(string status) {
    int distance = 0;
    string end = "12345678x";
    for (int i = 0; i < 9; ++i) {
        if (status[i] != 'x') {
            int cur_pos = i;
            int cur_x = cur_pos / 3, cur_y = cur_pos % 3;
            int end_pos = end.find(status[i]);
            int end_x = end_pos / 3, end_y = end_pos % 3;
            distance += sqrt((cur_x - end_x) * (cur_x - end_x) + (cur_y - end_y) * (cur_y - end_y));
        }
    }
    return distance;
}

struct Compare {
    bool operator()(const pair<string, int>& a, const pair<string, int>& b) {
        return a.second + eucDist(a.first) > b.second + eucDist(b.first);
    }
};

string AStar(string start) {
    if (!isSolvable(start)) return "unsolvable";

    priority_queue<pair<string, int>, vector<pair<string, int>>, Compare> pq;
    unordered_map<string, pair<string, char>> prev;
    unordered_map<string, int> distance;
    unordered_map<string, bool> visited;

    pq.push({start, 0});
    distance[start] = 0;
    visited[start] = false;
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
        char moves[4] = {'u', 'd', 'l', 'r'};

        for (int i = 0; i < 4; ++i) {
            int a = x + dx[i], b = y + dy[i];
            if (a >= 0 && a <= 2 && b >= 0 && b <= 2) {
                int cur_pos = a * 3 + b;
                string next_status = status;
                swap(next_status[pos], next_status[cur_pos]);
                int new_distance = cur_distance + 1;
                if (visited.find(next_status) == visited.end() || !visited[next_status] || (visited[next_status] && new_distance < distance[next_status])) {
                	visited[next_status] = false;
					pq.push({next_status, new_distance});
					prev[next_status].first = status;
                	prev[next_status].second = moves[i];
                	distance[next_status] = new_distance;
				}
				if (next_status == end) {
            		string solution = "";
            		while (next_status != start) {
                		solution += prev[next_status].second;
                		next_status = prev[next_status].first;
            		}
            		reverse(solution.begin(), solution.end());
            		return solution;
        		}
            }
        }
    }
    return "unsolvable";
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

    string solution = AStar(input);
    
    if (solution == "unsolvable") {
        cout << "unsolvable" << endl;
    } else {
        cout << solution << endl;
    }

    return 0;
}