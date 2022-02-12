package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

public class HyeongTaekHotel {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int C = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        int[][] cost = new int[N][2];
        int[] dp = new int[C + 100 + 1];
        Arrays.fill(dp, 100001);
        dp[0] = 0;

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for(int j = 0; j < 2; j++)
                cost[i][j] = Integer.parseInt(st.nextToken());
        }

        for(int i = 0; i < C + 100 + 1; i++) {
            for(int j = 0; j < N; j++) {
                if(i + cost[j][1] <= C + 100)
                    dp[i + cost[j][1]] = Math.min(dp[i + cost[j][1]], dp[i] + cost[j][0]);
            }
        }
        int answer = 100001;
        for(int i = C; i < C + 100 + 1; i++)
            answer = Math.min(answer, dp[i]);
        System.out.println(answer);

    }

}
