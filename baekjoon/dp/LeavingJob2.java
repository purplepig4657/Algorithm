/**
 * Baekjoon 15486 퇴사 2
 *
 *
 */

package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class LeavingJob2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] dp = new int[N + 2];
        ArrayList<ArrayList<Integer>> pay = new ArrayList<>();
        ArrayList<ArrayList<Integer>> time = new ArrayList<>();

        for(int i = 0; i <= N + 1; i++) {
            pay.add(new ArrayList<Integer>());
            time.add(new ArrayList<Integer>());
        }

        for(int i = 1; i <= N; i++) {
            String[] input = br.readLine().split(" ");
            int timeValue = Integer.parseInt(input[0]);
            int payValue = Integer.parseInt(input[1]);
            int tmp = timeValue + i;
            if(tmp > N + 1) continue;
            pay.get(tmp).add(payValue);
            time.get(tmp).add(timeValue);
        }

        for(int i = 1; i <= N + 1; i++) {
            ArrayList<Integer> payList = pay.get(i);
            ArrayList<Integer> timeList = time.get(i);
            if(payList.size() == 0) {
                dp[i] = dp[i - 1];
                continue;
            }
            int max = 0;
            for(int j = 0; j < payList.size(); j++) {
                max = Math.max(max, dp[i - timeList.get(j)] + payList.get(j));
            }
            dp[i] = Math.max(dp[i - 1], max);
        }

        System.out.println(dp[N + 1]);


    }

}
