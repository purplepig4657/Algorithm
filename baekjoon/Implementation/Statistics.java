import java.util.Scanner;
import java.util.Arrays;

public class Statistics {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		scanner.nextLine();

		int[] nums = new int[N];

		for (int i = 0; i < N; i++) {
			nums[i] = scanner.nextInt();
			scanner.nextLine();
		}
		
		scanner.close();

		double sum = 0;
		int[] table = new int[8001];
		int mode = -4001;
		int mode_index = -4001;
		int prev_mode_index = -4001;

		Arrays.sort(nums);

		for (int i = N - 1; i >= 0; i--) {
			sum += nums[i];
			table[nums[i] + 4000] += 1;
			if (mode <= table[nums[i] + 4000]) {
				if (mode == table[nums[i] + 4000]) {
					prev_mode_index = mode_index;
				} else {
					prev_mode_index = -4001;
				}
				mode = table[nums[i] + 4000];
				mode_index = nums[i];
			}
		}

		if (prev_mode_index != -4001) mode_index = prev_mode_index;

		System.out.println((int)Math.round(sum / N));
		System.out.println(nums[N / 2]);
		System.out.println(mode_index);
		System.out.println(nums[N - 1] - nums[0]);

	}
}

