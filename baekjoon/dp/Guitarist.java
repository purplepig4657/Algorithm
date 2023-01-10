/**
 * Baekjoon 1495 기타리스트
 *
 */

package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Guitarist {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N, S, M;
        int[] tmp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] volume = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        N = tmp[0]; S = tmp[1]; M = tmp[2];
        boolean[][] dp = new boolean[N + 1][M + 1];

        dp[0][S] = true;
        for (int i = 1; i <= N; i++) {
            for (int k = 0; k <= M; k++) {
                if (dp[i - 1][k]) {
                    if (k + volume[i - 1] <= M) dp[i][k + volume[i - 1]] = true;
                    if (k - volume[i - 1] >= 0) dp[i][k - volume[i - 1]] = true;
                }
            }
        }

        int answer = -1;
        for (int i = M; i >= 0; i--) {
            if (dp[N][i]) {
                answer = i;
                break;
            }
        }
        System.out.println(answer);

    }
}
