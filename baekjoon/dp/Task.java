/**
 * Baekjoon 2056 작업
 *
 */

package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Task {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] cost = new int[N];
        int[][] dependencies = new int[N][];
        for (int i = 0; i < N; i++) {
            String[] tmp = br.readLine().split(" ");
            cost[i] = Integer.parseInt(tmp[0]);
            int dependencyCount = Integer.parseInt(tmp[1]);
            int[] dependenciesList = new int[dependencyCount];
            for (int j = 0; j < dependencyCount; j++) dependenciesList[j] = Integer.parseInt(tmp[j + 2]);
            dependencies[i] = dependenciesList;
        }
        int answer = 0;
        int[] dp = new int[N];
        dp[0] = cost[0];
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < dependencies[i].length; j++) {
                dp[i] = Math.max(dp[dependencies[i][j] - 1], dp[i]);
            }
            dp[i] += cost[i];
            answer = Math.max(dp[i], answer);
        }

        System.out.println(answer);
    }
}
