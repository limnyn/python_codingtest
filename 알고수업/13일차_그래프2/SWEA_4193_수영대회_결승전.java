import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayDeque;

public class SWEA_4193_수영대회_결승전 {
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    static int solution(BufferedReader br) throws IOException {
        // 입력
        int n = Integer.parseInt(br.readLine());
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        StringTokenizer stStart = new StringTokenizer(br.readLine());
        int[] start = {Integer.parseInt(stStart.nextToken()), Integer.parseInt(stStart.nextToken())};

        StringTokenizer stEnd = new StringTokenizer(br.readLine());
        int[] end = {Integer.parseInt(stEnd.nextToken()), Integer.parseInt(stEnd.nextToken())};

        int[][] visited = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                visited[i][j] = 1000;
            }
        }
        visited[start[0]][start[1]] = 0;

        // bfs 순회를 위해 처리
        ArrayDeque<int[]> dq = new ArrayDeque<>();
        dq.offer(new int[]{start[0], start[1], 0});

        while (!dq.isEmpty()) {
            int[] current = dq.poll();
            int r = current[0];
            int c = current[1];
            int time = current[2] + 1;

            for (int i = 0; i < 4; i++) {
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
                            dq.offer(new int[]{nr, nc, time});
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
                            dq.offer(new int[]{nr, nc, nextTime});
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

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(br.readLine());
        for (int t_c = 1; t_c <= testCases; t_c++) {
            System.out.println("#" + t_c + " " + solution(br));
        }
    }
}
