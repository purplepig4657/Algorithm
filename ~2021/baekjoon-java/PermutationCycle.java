package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class PermutationCycle {

    static boolean[] visited;
    static int[][] map;
    static int T, N;

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
        StringTokenizer st;

        T = Integer.parseInt(br.readLine());

        for(int l = 0; l < T; l++) {
            N = Integer.parseInt(br.readLine());

            visited = new boolean[N];
            map = new int[N][N];

            st = new StringTokenizer(br.readLine(), " ");

            for(int i = 0; i < N; i++) {
                int a = i;
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
}
