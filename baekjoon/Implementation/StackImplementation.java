import java.util.*;

public class StackImplementation {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		scanner.nextLine();

		String[] command_name = new String[N];
		int[] command_arg = new int[N];

		for (int i = 0; i < N; i++) {
			String line = scanner.nextLine();
			String[] items = line.split(" ");
			if (items.length > 1) 
				command_arg[i] = Integer.parseInt(items[1]);
			command_name[i] = items[0];
		}

		scanner.close();

		Stack<Integer> s = new Stack<>();

		for (int i = 0; i < N; i++) {
			if (command_name[i].equals("push")) {
				s.push(command_arg[i]);
			} else if (command_name[i].equals("pop")) {
				if (s.empty()) {
					System.out.println(-1);
				} else {
					System.out.println(s.pop());
				}
			} else if (command_name[i].equals("size")) {
				System.out.println(s.size());
			} else if (command_name[i].equals("empty")) {
				System.out.println(s.empty() ? 1 : 0);
			} else if (command_name[i].equals("top")) {
				if (s.empty()) {
					System.out.println(-1);
				} else {
					System.out.println(s.peek());
				}
			}
		}
	}
}

