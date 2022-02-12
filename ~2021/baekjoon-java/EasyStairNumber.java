package baekjoon;

import java.util.Scanner;

public class EasyStairNumber {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();

        int[][] stair = new int[10][N + 1];

        stair[0][1] = 0;
        for(int i = 1; i < 10; i++)
            stair[i][1] = 1;

        for(int i = 2; i <= N; i++) {
            for(int j = 0; j < 10; j++) {
                if(j == 0)
                    stair[j][i] = stair[j + 1][i - 1] % 1000000000;
                else if(j == 9)
                    stair[j][i] = stair[j - 1][i - 1] % 1000000000;
                else
                    stair[j][i] = (stair[j + 1][i - 1] + stair[j - 1][i - 1]) % 1000000000;
            }
        }

        long answer = 0;
        for(int i = 0; i < 10; i++)
            answer += stair[i][N];
        System.out.println(answer % 1000000000);
    }

}
