/**
 * Baekjoon 13549 숨바꼭질 3
 *
 * */

package GraphSearch;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;

public class HideAndSeek3 {

    public static int[] answer;

    public static void bfs(int n, int k) {
        LinkedList<Integer> deque = new LinkedList<>();
        answer[n] = 0;
        deque.addFirst(n);
        while (!deque.isEmpty()) {
            int current = deque.poll();
            if (current == k) return;
            if (current * 2 <= 200000 && answer[current * 2] == -1) {
                deque.addFirst(current * 2);
                answer[current * 2] = answer[current];
            }
            if (current > 0 && answer[current - 1] == -1) {
                deque.offerLast(current - 1);
                answer[current - 1] = answer[current] + 1;
            }
            if (current < 200000 && answer[current + 1] == -1) {
                deque.offerLast(current + 1);
                answer[current + 1] = answer[current] + 1;
            }
        }

    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();

        answer = new int[200001];
        Arrays.fill(answer, -1);

        bfs(N, K);
        System.out.println(answer[K]);

    }
}
