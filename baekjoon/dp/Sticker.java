/**
 * Baekjoon 9465 스티커
 *
 */

package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sticker {

    public static int solution(int n, int[][] sticker) {
        int answer = -1;
        int[][] dp = new int[2][n];

        for (int i = 0; i < n; i++) {
            if (i == 0) {
                dp[0][0] = sticker[0][0];
                dp[1][0] = sticker[1][0];
            } else if (i == 1) {
                dp[0][1] = dp[1][0] + sticker[0][1];
                dp[1][1] = dp[0][0] + sticker[1][1];
            } else {
                dp[0][i] = Math.max(Math.max(dp[1][i - 1], dp[0][i - 2]), dp[1][i - 2]) + sticker[0][i];
                dp[1][i] = Math.max(Math.max(dp[0][i - 1], dp[0][i - 2]), dp[1][i - 2]) + sticker[1][i];
            }
            answer = Math.max(Math.max(dp[0][i], dp[1][i]), answer);
        }

        return answer;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int testCase = 0; testCase < T; testCase++) {
            int n = Integer.parseInt(br.readLine());
            int[][] sticker = new int[2][n];
            String[] sticker_line1 = br.readLine().split(" ");
            String[] sticker_line2 = br.readLine().split(" ");
            for (int i = 0; i < n; i++) {
                sticker[0][i] = Integer.parseInt(sticker_line1[i]);
                sticker[1][i] = Integer.parseInt(sticker_line2[i]);
            }
            System.out.println(solution(n, sticker));
        }
    }
}
