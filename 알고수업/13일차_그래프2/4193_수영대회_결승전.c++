#include <iostream>
#include <vector>
#include <queue>
#include <sstream>

using namespace std;

const int dr[] = {-1, 0, 1, 0};
const int dc[] = {0, 1, 0, -1};

int solution() {
    // 입력
    int n;
    cin >> n;
    cin.ignore(); // 개행문자 처리

    vector<vector<int>> grid(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        string line;
        getline(cin, line);
        istringstream iss(line);
        for (int j = 0; j < n; ++j) {
            iss >> grid[i][j];
        }
    }

    string startLine, endLine;
    getline(cin, startLine);
    getline(cin, endLine);
    istringstream issStart(startLine), issEnd(endLine);

    int start[2], end[2];
    for (int i = 0; i < 2; ++i) {
        issStart >> start[i];
        issEnd >> end[i];
    }

    vector<vector<int>> visited(n, vector<int>(n, 1000));
    visited[start[0]][start[1]] = 0;

    // bfs 순회를 위해 처리
    queue<vector<int>> dq;
    dq.push({start[0], start[1], 0});

    while (!dq.empty()) {
        int r = dq.front()[0];
        int c = dq.front()[1];
        int time = dq.front()[2] + 1;
        dq.pop();

        for (int i = 0; i < 4; ++i) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                if (end[0] == nr && end[1] == nc) {
                    if (visited[nr][nc] > time) {
                        visited[nr][nc] = time;
                    }
                    continue;
                }

                if (grid[nr][nc] == 0) {
                    if (visited[nr][nc] > time) {
                        visited[nr][nc] = time;
                        dq.push({nr, nc, time});
                    }
                }

                // 소용돌이는 시작시간부터 2초동안 못 지나가고 1초동안 지나갈 수 있다
                if (grid[nr][nc] == 2) {
                    int nextTime = time;
                    while (nextTime % 3 != 0) {
                        nextTime++;
                    }
                    if (visited[nr][nc] > nextTime) {
                        visited[nr][nc] = nextTime;
                        dq.push({nr, nc, nextTime});
                    }
                }
            }
        }
    }

    if (visited[end[0]][end[1]] == 1000) {
        return -1;
    }
    return visited[end[0]][end[1]];
}

int main() {
    int testCases;
    cin >> testCases;
    for (int t_c = 1; t_c <= testCases; ++t_c) {
        cout << "#" << t_c << " " << solution() << endl;
    }
    return 0;
}
