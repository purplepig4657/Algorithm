/**
 * Baekjoon 5557 1학년
 *
 */

package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Freshman {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] numbers = new int[N];
        long[][] dp = new long[21][N];
        int targetNumber;
        String[] tmp = br.readLine().split(" ");
        for (int i = 1; i < N; i++) numbers[i] = Integer.parseInt(tmp[i - 1]);
        targetNumber = Integer.parseInt(tmp[N - 1]);
        dp[numbers[1]][1] = 1;
        for (int i = 2; i < N; i++) {
            for (int j = 0; j <= 20; j++) {
                if (dp[j][i - 1] > 0) {
                    int index1 = j + numbers[i];
                    int index2 = j - numbers[i];
                    if (0 <= index1 && index1 <= 20) dp[index1][i] += dp[j][i - 1];
                    if (0 <= index2 && index2 <= 20) dp[index2][i] += dp[j][i - 1];
                }
            }
        }
        System.out.println(dp[targetNumber][N - 1]);
    }
}
