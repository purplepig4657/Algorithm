package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class bitberry {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int count = Integer.parseInt(br.readLine());
		for(int i = 0; i < count; i++) {
			String[] input = br.readLine().split(" ");
			int values[] = new int[6];
			for(int j = 0; j < 6; j++) 
				values[j] = Integer.parseInt(input[j]);
			int bit = values[0], berry = values[1], coin = 0;
			if((bit / values[2]) >= 2) {
				coin += (berry / values[4]) * values[5] + ((bit / values[2]) / 2) * values[3];
				bit -= ((bit / values[2]) / 2) * values[2];
			} else {
				coin += (berry / values[4]) * values[5] + (bit / values[2]) * values[3];
				bit -= (bit / values[2]) * values[2];
			}
			int bitcoin_pre = bit <= coin ? bit : coin;
			int bitcoin_cur = 0;
			if(coin > bit) {
				while(true) {
					bit += values[2];
					coin -= values[3];
					bitcoin_cur = bit <= coin ? bit : coin;
					if(bitcoin_cur <= bitcoin_pre) 
						break;
					bitcoin_pre = bit <= coin ? bit : coin;
				}
			} else if(coin < bit) {
				while(true) {
					bit -= values[2];
					coin += values[3];
					bitcoin_cur = bit <= coin ? bit : coin;
					if(bitcoin_cur <= bitcoin_pre) 
						break;
					bitcoin_pre = bit <= coin ? bit : coin;
				}
			}
			System.out.println(bitcoin_pre);
		}
	}

}
