/**
 * Baekjoon 1261 알고스팟
 *
 * */

package GraphSearch;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;

public class Algospot {

    public static int[][] map;
    public static int[][] answer;
    public static int[] dx = {1, -1, 0, 0};
    public static int[] dy = {0, 0, 1, -1};

    public static void bfs(int n, int m) {
        LinkedList<int[]> deque = new LinkedList<>();
        int[] initialNode = {0, 0};
        deque.addFirst(initialNode);
        answer[0][0] = 0;
        while (!deque.isEmpty()) {
            int[] node = deque.poll();
            int x = node[0]; int y = node[1];
            if (x == m - 1 && y == n - 1) return;
            for (int d = 0; d < 4; d++) {
                int nextX = x + dx[d];
                int nextY = y + dy[d];
                if (0 <= nextX && nextX < m && 0 <= nextY && nextY < n && answer[nextY][nextX] == -1) {
                    int[] nodeForAdd = {nextX, nextY};
                    if (map[nextY][nextX] == 0) {
                        answer[nextY][nextX] = answer[y][x];
                        deque.addFirst(nodeForAdd);
                    } else {
                        answer[nextY][nextX] = answer[y][x] + 1;
                        deque.offerLast(nodeForAdd);
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tmp = br.readLine().split(" ");
        int M = Integer.parseInt(tmp[0]);
        int N = Integer.parseInt(tmp[1]);
        map = new int[N][M];
        for (int i = 0; i < N; i++) {
            tmp = br.readLine().split("");
            for (int j = 0; j < M; j++) map[i][j] = Integer.parseInt(tmp[j]);
        }
        answer = new int[N][M];
        for (int i = 0; i < N; i++) Arrays.fill(answer[i], -1);
        bfs(N, M);
        System.out.println(answer[N - 1][M - 1]);
    }
}
