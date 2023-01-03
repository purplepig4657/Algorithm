/**
 * Baekjoon 2240 자두나무
 *
 */

package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class PlumTree {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tmp = br.readLine().split(" ");
        int T = Integer.parseInt(tmp[0]);
        int W = Integer.parseInt(tmp[1]);
        int[][] plum = new int[2][T];
        int[][] dp = new int[2][T + 1];
        for (int i = 0; i < T; i++) plum[Integer.parseInt(br.readLine()) - 1][i] = 1;
        for (int stage = 0; stage <= W; stage++) {
            for (int sec = 1; sec <= T; sec++) {
                int tree = stage % 2;
                int otherTree = (stage + 1) % 2;
                dp[tree][sec] = Math.max(dp[tree][sec - 1], dp[otherTree][sec - 1]) + plum[tree][sec - 1];
            }
        }
        System.out.println(Math.max(dp[0][T], dp[1][T]));
    }
}
