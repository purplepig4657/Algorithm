package baekjoon;

import java.util.Scanner;
import java.util.ArrayList;

public class HideAndSeek {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int current = scanner.nextInt();
        int target = scanner.nextInt();

        if(current == target) {
            System.out.println(0);
            return;
        }

        ArrayList<Integer> bfs = new ArrayList<Integer>();
        boolean[] history = new boolean[100001];
        ArrayList<Integer> answer = new ArrayList<Integer>();
        int count = 0;

        bfs.add(current);
        history[current] = true;
        boolean isEnd = false;

        while(true) {
            int c = bfs.size();
            for(int i = 0; i < c; i++) {
                if(bfs.get(i) == target) {
                    isEnd = true;
                    answer.add(count);
                    break;
                }
            }
            if(isEnd) break;
            for(int i = 0; i < c; i++) {
                int a = bfs.get(0);
                if(a - 1 >= 0) {
                    if(!history[a - 1]) {
                        bfs.add(a - 1);
                        history[a - 1] = true;
                    }
                }
                if(a + 1 <= 100000) {
                    if(!history[a + 1]) {
                        bfs.add(a + 1);
                        history[a + 1] = true;
                    }
                }
                if(a * 2 <= 100000) {
                    if (!history[a * 2]) {
                        bfs.add(a * 2);
                        history[a * 2] = true;
                    }
                }
                bfs.remove(0);
            }
            count++;
        }
        System.out.println(count);
    }

}
