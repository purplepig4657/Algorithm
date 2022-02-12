package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class JiminLamp {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] tmp;
        tmp = br.readLine().split(" ");

        int N = Integer.parseInt(tmp[0]);
        int M = Integer.parseInt(tmp[1]);

        int[][] lamp = new int[N][M];

        for(int i = 0; i < N; i++) {
            tmp = br.readLine().split("");
            for(int j = 0; j < M; j++)
                lamp[i][j] = Integer.parseInt(tmp[j]);
        }

        int K = Integer.parseInt(br.readLine());

        int max = 0;
        for(int i = 0; i < N; i++) {
            int c = 0;
            for(int j = 0; j < M; j++)
                if(lamp[i][j] == 0)
                    c++;
            if(c > K || K % 2 != c % 2)
                continue;
            int count = 0;
            for(int j = i; j < N; j++) {
                boolean isEqual = true;
                for(int k = 0; k < M; k++) {
                    if(lamp[i][k] != lamp[j][k]) {
                        isEqual = false;
                        break;
                    }
                }
                if(!isEqual)
                    continue;
                count++;
            }
            max = Math.max(max, count);
        }

        System.out.println(max);
    }

}
