/**
 * Baekjoon 16194 카드 구매하기 2
 *
 */

package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class CardPurchasing2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] P = new int[N];
        int[] dp = new int[N + 1];
        String[] tmp = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            P[i] = Integer.parseInt(tmp[i]);
            dp[i + 1] = P[i];
        }
        for (int i = 1; i < N + 1; i++) {
            for (int j = 0; j < i; j++) {
                dp[i] = Math.min(dp[i - j] + dp[j], dp[i]);
            }
        }
        System.out.println(dp[N]);

    }
}
