package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Queue;

public class DFSAndBFS {

    static int[][] map;
    static int N, M, V;
    static boolean[] visited;

    static void dfs(int start) {
        visited[start] = true;
        System.out.print((start + 1) + " ");

        for(int i = 0; i < N; i++) {
            if(map[start][i] == 1 && !visited[i]) {
                dfs(i);
            }
        }
    }

    static void bfs() {
        boolean[] visited = new boolean[N];

        Queue<Integer> queue = new LinkedList<>();
        visited[V - 1] = true;
        queue.add(V - 1);

        do {
            int current = queue.poll();
            System.out.print((current + 1) + " ");
            for(int i = 0; i < N; i++) {
                if(map[current][i] == 1 && !visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        } while(!queue.isEmpty());

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        map = new int[N][N];

        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            map[a][b] = 1;
            map[b][a] = 1;
        }

        visited = new boolean[N];

        dfs(V - 1);
        System.out.println();
        bfs();

    }
}
