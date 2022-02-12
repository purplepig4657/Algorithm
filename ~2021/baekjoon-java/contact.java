package baekjoon;

import java.util.Scanner;

public class contact {
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int loop = scanner.nextInt();
		scanner.nextLine(); // clear buffer
		
		String[] signal = new String[loop];
				
		for(int i = 0; i < signal.length; i++) { // input signal
			signal[i] = scanner.nextLine();
		}
		
		scanner.close();
		
		main: for(int i = 0; i < signal.length; i++ ) {
			boolean case1 = false, case2 = false, cog = false;
			int count = 0;
			
			for(int j = 0; j < signal[i].length(); j++) {
				if(signal[i].charAt(j) == '1') {
					if(!case1 && !case2) {
						case1 = true;
						continue;
					}
					if(case1 && !cog && count < 2) {
						System.out.println("NO");
						continue main;
					} else if(case1 && !cog && count >= 2) {
						cog = true;
						count = 0;
					}
					if(case1 && cog) {
						if(j + 1 < signal[i].length() && j + 2 < signal[i].length()) {
							if(signal[i].charAt(j + 1) == '0' && signal[i].charAt(j + 2) != '1') {
								case1 = false;
								cog = false;
								continue;
							} else if(signal[i].charAt(j + 1) == '0' && signal[i].charAt(j + 2) != '0') {
								cog = false;
								continue;
							}
						}
						
						//continue;
					}
					if(case2) {
						case2 = false;
						continue;
					}
				}
				
				if(signal[i].charAt(j) == '0') {
					if(!case1 && !case2) {
						case2 = true;
						continue;
					}
					if(case1 && !cog) {
						count++;
						continue;
					}
					if(case2) {
						System.out.println("NO");
						continue main;
					}
				}
				
			}
			System.out.println("YES");
		}
	}

}

/*
 * 
10010111
011000100110001
0110001011001
*/
