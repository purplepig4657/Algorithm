package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Coin1 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] tmp = br.readLine().split(" ");
        int n = Integer.parseInt(tmp[0]);
        int k = Integer.parseInt(tmp[1]);

        boolean[][] dp = new boolean[k + 1][k + 1];
        for(int i = 0; i < n; i++) dp[Integer.parseInt(br.readLine())][1] = true;

        // 다시 풀어라




    }
}
