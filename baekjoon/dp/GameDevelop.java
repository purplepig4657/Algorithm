/**
 * Baekjoon 1516 게임 개발
 *
 */

package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class GameDevelop {

    static int[] topologySort(int N, int[][] dependencies, int[] enterCount) {
        ArrayList<Integer> result = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < N; i++) if (enterCount[i] == 0) queue.offer(i);
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int dependencyNode : dependencies[node]) {
                enterCount[dependencyNode - 1]--;
                if (enterCount[dependencyNode - 1] == 0) queue.offer(dependencyNode - 1);
            }
            result.add(node);
        }
        return result.stream().mapToInt(Integer::intValue).toArray();
    }

    static int[] solution(int N, int[][] dependencies, int[] cost, int[] sortedNodes) {
        int[] dp = new int[N];
        for (int i = sortedNodes.length - 1; i >= 0; i--) {
            int node = sortedNodes[i];
            if (dependencies[node].length == 0) {
                dp[node] = cost[node];
                continue;
            }
            for (int j = 0; j < dependencies[node].length; j++)
                dp[node] = Math.max(dp[dependencies[node][j] - 1], dp[node]);
            dp[node] += cost[node];
        }
        return dp;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] dependencies = new int[N][];
        int[] cost = new int[N];
        int[] enterCount = new int[N];  // Topology Sort Part
        for (int i = 0; i < N; i++) {
            int[] tmp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            cost[i] = tmp[0];
            int[] dependency = Arrays.copyOfRange(tmp, 1, tmp.length - 1);
            for (int d : dependency) enterCount[d - 1]++;
            dependencies[i] = dependency;
        }

        int[] sortedNodes = topologySort(N, dependencies, enterCount);
        int[] answers = solution(N, dependencies, cost, sortedNodes);
        for (int answer : answers) System.out.println(answer);
    }
}
