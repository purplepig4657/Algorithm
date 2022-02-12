package baekjoon;

import java.util.Scanner;

public class AscendingNumber {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt() - 1;
        if(N == 0) {
            System.out.println(10);
            return;
        }
        int[][] dp = new int[N][10];

        for(int i = 0; i < 10; i++) dp[0][i] = i + 1;

        for(int i = 1; i < N; i++ ) {
            dp[i][0] = dp[i - 1][0];
            for(int j = 1; j < 10; j++) {
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 10007;
            }
        }

        int answer = 0;
        for(int i = 0; i < 10; i++) answer += dp[N - 1][i] % 10007;

        System.out.println(answer % 10007);

    }
}
