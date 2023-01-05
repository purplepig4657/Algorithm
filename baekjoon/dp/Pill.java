/**
 * Baekjoon 4811 알약
 *
 */

package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Pill {

    static long solution(int N) {
        long[][] dp = new long[N + 1][N + 1];
        for (int i = 0; i <= N; i++) dp[0][i] = 1;
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (j > i) break;
                dp[j][i] = dp[j - 1][i] + dp[j][i - 1];
            }
        }
        return dp[N][N];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder stringBuilder = new StringBuilder();
        while (true) {
            int N = Integer.parseInt(br.readLine());
            if (N == 0) break;
            stringBuilder.append(solution(N)).append("\n");
        }
        System.out.println(stringBuilder.toString());
    }
}
