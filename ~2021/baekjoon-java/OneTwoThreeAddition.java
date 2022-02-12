package baekjoon;

import java.util.Scanner;

public class OneTwoThreeAddition {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();

        for(int loop = 0; loop < T; loop++) {
            int n = scanner.nextInt();
            if(n == 1) {
                System.out.println(1);
                continue;
            } else if(n == 2) {
                System.out.println(2);
                continue;
            } else if(n == 3) {
                System.out.println(4);
                continue;
            }

            int[] dp = new int[n];
            dp[0] = 1;
            dp[1] = 2;
            dp[2] = 4;

            for(int i = 3; i < n; i++)
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];

            System.out.println(dp[n - 1]);
        }

    }
}
