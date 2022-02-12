package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Package {

    static class Information implements Comparable<Information> {
        public int first, last, amount;

        Information(int first, int last, int amount) {
            this.first = first;
            this.last = last;
            this.amount = amount;
        }

        public int compareTo(Information info) {
            if(!(first - info.first == 0)) return first - info.first;
            else return -1 * (last - info.last);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tmp = br.readLine().split(" ");
        int N = Integer.parseInt(tmp[0]);
        int C = Integer.parseInt(tmp[1]);
        int M = Integer.parseInt(br.readLine());
        ArrayList<Information> pieces1 = new ArrayList<>(M);
        ArrayList<Information> pieces2 = new ArrayList<>(M);

        for(int i = 0; i < M; i++) {
            tmp = br.readLine().split(" ");
            int[] nums = new int[3];
            for(int j = 0; j < 3; j++) nums[j] = Integer.parseInt(tmp[j]);
            pieces1.add(new Information(nums[0], nums[1], nums[2]));
            pieces2.add(new Information(nums[0], nums[1], nums[2]));
        }
        Collections.sort(pieces1);
        Collections.sort(pieces2);

        int[] sum = new int[N];
        for(int i = 0; i < M; i++) {
            Information info = pieces1.get(i);
            for(int j = info.first; j <= info.last - 1; j++) sum[j] += info.amount;
        }
        for(int i = 1; i < N; i++) sum[i] -= C;

        for(int i = 0; i < M; i++) {
            Information info = pieces1.get(i);
            int max = 0;
            for(int j = info.first; j <= info.last - 1; j++) max = Math.max(max, sum[j]);
            if(max > 0) {
                if(info.amount >= max) {
                    for(int j = info.first; j <= info.last - 1; j++) sum[j] -= max;
                    info.amount -= max;
                } else {
                    for(int j = info.first; j <= info.last - 1; j++) sum[j] -= info.amount;
                    info.amount = 0;
                }
            }
        }

        int answer1 = 0;
        for(int i = 0; i < M; i++) {
            Information info = pieces1.get(i);
            answer1 += info.amount;
        }

        sum = new int[N];
        for(int i = 0; i < M; i++) {
            Information info = pieces2.get(i);
            for(int j = info.first; j <= info.last - 1; j++) sum[j] += info.amount;
        }

        for(int i = 1; i < N; i++) {
            if(sum[i] > C) {
                int remain = sum[i] - C;
                while(remain > 0) {
                    Information info = pieces2.get(0);
                    for(int j = 0; j < M; j++) {
                        info = pieces2.get(j);
                        if(i == info.first && info.amount > 0) break;
                    }
                    if(info.amount >= remain) {
                        for(int j = info.first; j <= info.last - 1; j++) sum[j] -= remain;
                        info.amount -= remain;
                        remain = 0;
                    } else {
                        for(int j = info.first; j <= info.last - 1; j++) sum[j] -= info.amount;
                        remain -= info.amount;
                        info.amount = 0;
                    }
                }
            }
        }

        int answer2 = 0;
        for(int i = 0; i < M; i++) {
            Information info = pieces2.get(i);
            answer2 += info.amount;
        }

        System.out.println(Math.max(answer1, answer2));


    }
}
