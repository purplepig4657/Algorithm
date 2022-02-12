package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class FlippingCoin2 {

    static long start;
    static boolean isLong = false;
    static int proc = 2000000000;

    static int flipCoinRow(byte[][] c) {
        boolean tf = false;
        int mid = c.length / 2;
        int row = 0;
        int answer = c.length * c.length;

        if((System.currentTimeMillis() - start) / 1000 >= 8)
            return 2000000000;

        for(int i = 0; i < c.length; i++) {
            int count = 0;
            for(int j = 0; j < c.length; j++) {
                count = c[i][j] == 1 ? count + 1 : count;
                if(count > mid) {
                    row = i;
                    byte[][] p = new byte[c.length][c.length];
                    for(int k = 0; k < c.length; k++)
                        System.arraycopy(c[k], 0, p[k], 0, c.length);
                    for(int k = 0; k < c.length; k++)
                        p[row][k] = (byte) (c[row][k] == 1 ? 0 : 1);
                    int a = flipCoinRow(p);
                    int b = flipCoinColumn(p);
                    if(a <= b) {
                        if(a <= proc)
                            proc = a;
                    }
                    else {
                        if(b <= proc)
                            proc = b;
                    }
                    tf = true;
                    break;
                }
            }
        }
        if(tf) {
            return answer;
        } else {
            for(int i = 0; i < c.length; i++)
                for(int j = 0; j < c.length; j++)
                    row = c[i][j] == 1 ? row + 1 : row;
            System.out.println(row);
            return row;
        }
    }

    static int flipCoinColumn(byte[][] c) {
        boolean tf = false;
        int mid = c.length / 2;
        int column = 0;
        int answer = c.length * c.length;

        if((System.currentTimeMillis() - start) / 1000 >= 8)
            return 2000000000;

        for(int i = 0; i < c.length; i++) {
            int count = 0;
            for(int j = 0; j < c.length; j++) {
                count = c[j][i] == 1 ? count + 1 : count;
                if(count > mid) {
                    column = i;
                    byte[][] p = new byte[c.length][c.length];
                    for(int k = 0; k < c.length; k++)
                        System.arraycopy(c[k], 0, p[k], 0, c.length);
                    for(int k = 0; k < c.length; k++)
                        p[k][column] = (byte) (c[k][column] == 1 ? 0 : 1);
                    int a = flipCoinRow(p);
                    int b = flipCoinColumn(p);
                    if(a <= b) {
                        if(a <= proc)
                            proc = a;
                    }
                    else {
                        if(b <= proc)
                            proc = b;
                    }
                    tf = true;
                    break;
                }
            }
        }
        if(tf) {
            return answer;
        } else {
            for(int i = 0; i < c.length; i++)
                for(int j = 0; j < c.length; j++)
                    column = c[i][j] == 1 ? column + 1 : column;
            System.out.println(column);
            return column;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        String[] s = new String[n];
        byte[][] c = new byte[n][n];

        for(int i = 0; i < n; i++) {
            s = br.readLine().split("");
            for(int j = 0; j < n; j++)
                c[i][j] = (byte) (s[j].equals("H") ? 0 : 1);
        }

        start = System.currentTimeMillis();

        int a = flipCoinRow(c);
        int b = flipCoinColumn(c);

        if(a <= b) {
            if(a <= proc)
                proc = a;
        }
        else {
            if(b <= proc)
                proc = b;
        }

        System.out.println();
        System.out.println(proc);
    }

}
