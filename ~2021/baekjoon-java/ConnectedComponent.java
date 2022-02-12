package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class ConnectedComponent {

    static boolean[] visited;
    static int[][] map;
    static int N, M;

    static boolean dfs(int start) {
        boolean notVisited = false;

        if(!visited[start]) notVisited = true;
        for(int i = 0; i < N; i++) {
            if(map[start][i] == 1 && !visited[i]) {
                visited[i] = true;
                dfs(i);
            }
        }
        visited[start] = true;

        return notVisited;

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        visited = new boolean[N];
        map = new int[N][N];

        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            map[a][b] = 1;
            map[b][a] = 1;
        }

        int answer = 0;
        for(int i = 0; i < N; i++)
            if(dfs(i)) answer++;

        System.out.println(answer);


    }
}
