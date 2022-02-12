package baekjoon;

import java.util.Scanner;

public class WaterBottle {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int K = scanner.nextInt();

        final int[] P = new int[25];
        int[] bc = new int[25];

        for(int i = 0; i < P.length; i++) {
            P[i] = (int)Math.pow(2, i);
        }

        int i = 0;
        while(N != 0) {
            if(N == P[i] && i != 0) {
                bc[i] += N / P[i];
                N -= (N / P[i]) * P[i];
                i = 0;
                continue;
            } else if(N < P[i] && i != 0) {
                bc[i - 1] += N / P[i - 1];
                N -= (N / P[i - 1]) * P[i - 1];
                i = 0;
                continue;
            }
            i++;
        }
        int sum = 0;
        for(i = 0; i < bc.length; i++)
            if(bc[i] == 1)
                sum++;
        if(sum <= K) {
            System.out.println(0);
            return;
        }
        int t = 0;
        sum = 0;
        for(i = bc.length - 1; i >= 0; i--) {
            if(bc[i] == 1 && K > 0) {
                K--;
                t = i;
            } else if(bc[i] == 1 && K == 0) {
                sum += P[i];
            }
        }

        System.out.println(P[t] - sum);

    }

}
