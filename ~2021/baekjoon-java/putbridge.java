package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class putbridge {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int count = Integer.parseInt(br.readLine());
		for(int i = 0; i < count; i++) {
			String[] input = br.readLine().split(" ");
			int n = Integer.parseInt(input[1]);
			int r = Integer.parseInt(input[0]);
			long answer = 1;
			long temp = 1;
			for(int j = 1; j < n + 1; j++) {
				temp *= j;
			}
			answer *= temp;
			temp = 1;
			for(int j = 1; j < r + 1; j++) {
				temp *= j;
			}
			answer /= temp;
			temp = 1;
			for(int j = 1; j < n - r + 1; j++) {
				temp *= j;
			}
			answer /= temp;
			System.out.println(answer);
		}

	}

}
