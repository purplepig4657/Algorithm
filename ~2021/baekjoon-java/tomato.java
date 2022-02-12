package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class tomato {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] str = br.readLine().split(" ");
		
		int row_value = Integer.parseInt(str[0]);
		int column_value = Integer.parseInt(str[1]);
		
		int[][] tomato = new int[column_value][row_value];
		int[][] delta = new int[column_value][row_value];
		
		for(int i = 0; i < tomato.length; i++) {
			str = br.readLine().split(" ");
			int[] replace = new int[str.length];
			for(int j = 0; j < tomato[i].length; j++) {
				replace[j] = Integer.parseInt(str[j]);
			}
			tomato[i] = replace.clone();
			
		}
		
		for(int i = 0; i < tomato.length; i++) 
			delta[i] = tomato[i].clone();
		
		boolean isChanged = false;
		boolean isExist = false;
		int time = 0;
		ArrayList<String> change = new ArrayList<String>();
		
		for(int i = 0; i < tomato.length; i++) {
			for(int j = 0; j < tomato[i].length; j++) {
				if(tomato[i][j] == 0 && !isExist) {
					isExist = true;
				}
				
				if(tomato[i][j] == 1) {
					if(i - 1 >= 0) {
						if(tomato[i - 1][j] == 0) {
							delta[i - 1][j] = 1;
							change.add(Integer.toString(i - 1) + "," + Integer.toString(j));
							isChanged = true;
						}
					}
					if(i + 1 <= tomato.length - 1) {
						if(tomato[i + 1][j] == 0) {
							delta[i + 1][j] = 1;
							change.add(Integer.toString(i + 1) + "," + Integer.toString(j));
							isChanged = true;
						}
					}
					if(j + 1 <= tomato[i].length - 1) {
						if(tomato[i][j + 1] == 0) {
							delta[i][j + 1] = 1;
							change.add(Integer.toString(i) + "," + Integer.toString(j + 1));
							isChanged = true;
						}
					}
					if(j - 1 >= 0) {
						if(tomato[i][j - 1] == 0) {
							delta[i][j - 1] = 1;
							change.add(Integer.toString(i) + "," + Integer.toString(j - 1));
							isChanged = true;
						}
					}
				}
			}
		}
		if(!isChanged) {
			if(isExist) {
				System.out.println(-1);
				return;
			}
			
			System.out.println(time);
			return;
		}
		isChanged = false;
		isExist = false;
		time++;
		for(int i = 0; i < delta.length; i++) 
			tomato[i] = delta[i].clone();
		
		while(true) {
			int size = change.size();
			for(int k = 0; k < size; k++) {
				int i = Integer.parseInt(change.get(k).split(",")[0]);
				int j = Integer.parseInt(change.get(k).split(",")[1]);
				if(i - 1 >= 0) {
					if(tomato[i - 1][j] == 0) {
						delta[i - 1][j] = 1;
						if(!change.contains(Integer.toString(i - 1) + "," + Integer.toString(j)))
							change.add(Integer.toString(i - 1) + "," + Integer.toString(j));
						isChanged = true;
					}
				}
				if(i + 1 <= tomato.length - 1) {
					if(tomato[i + 1][j] == 0) {
						delta[i + 1][j] = 1;
						if(!change.contains(Integer.toString(i + 1) + "," + Integer.toString(j)))
							change.add(Integer.toString(i + 1) + "," + Integer.toString(j));
						isChanged = true;
					}
				}
				if(j + 1 <= tomato[i].length - 1) {
					if(tomato[i][j + 1] == 0) {
						delta[i][j + 1] = 1;
						if(!change.contains(Integer.toString(i) + "," + Integer.toString(j + 1)))
							change.add(Integer.toString(i) + "," + Integer.toString(j + 1));
						isChanged = true;
					}
				}
				if(j - 1 >= 0) {
					if(tomato[i][j - 1] == 0) {
						delta[i][j - 1] = 1;
						if(!change.contains(Integer.toString(i) + "," + Integer.toString(j - 1)))
							change.add(Integer.toString(i) + "," + Integer.toString(j - 1));
						isChanged = true;
					}
				}
			}
			
			
			if(!isChanged) {
				for(int i = 0; i < tomato.length; i++) {
					for(int j = 0; j < tomato[i].length; j++) {
						if(tomato[i][j] == 0 && !isExist) {
							isExist = true;
							break;
						}
					}
					if(isExist) break;
				}
				if(isExist) {
					System.out.println(-1);
					break;
				}
				
				System.out.println(time);
				break;
			}
			
			isChanged = false;
			isExist = false;
			time++;
			for(int i = 0; i < delta.length; i++) 
				tomato[i] = delta[i].clone();
			
		}
		
	}

}
