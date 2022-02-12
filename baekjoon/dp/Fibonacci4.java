/**
 * Baekjoon 10826 피보나치 수 4
 *
 *
 */

package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Fibonacci4 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        br.close();
        if(n == 0) {
            System.out.println(0);
            return;
        }

        BigInteger[] dp = new BigInteger[n + 1];
        dp[0] = BigInteger.ZERO;
        dp[1] = BigInteger.ONE;

        for(int i = 2; i <= n; i++)
            dp[i] = dp[i - 1].add(dp[i - 2]);

        System.out.println(dp[n]);
    }


}
