package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class FlippingCoin {

    static int flipCoinRow(byte[][] f) {
        byte[][] c = new byte[f.length][f.length];
        for(int i = 0; i < f.length; i++)
            System.arraycopy(f[i], 0, c[i], 0, f.length);
        boolean tf = false;
        int mid = c.length / 2;
        int row = 0;

        for(int i = 0; i < c.length; i++) {
            int count = 0;
            for(int j = 0; j < c.length; j++) {
                count = c[i][j] == 1 ? count + 1 : count;
                if(count > mid) {
                    tf = true;
                    row = i;
                    break;
                }
            }
            if(tf) break;
        }
        if(tf) {
            for(int i = 0; i < c.length; i++)
                c[row][i] = (byte) (c[row][i] == 1 ? 0 : 1);
            int a = flipCoinRow(c);
            int b = flipCoinColumn(c);
            if(a <= b) return a;
            else return b;
        } else {
            for(int i = 0; i < c.length; i++)
                for(int j = 0; j < c.length; j++)
                    row = c[i][j] == 1 ? row + 1 : row;
            System.out.println(row);
            return row;
        }
    }

    static int flipCoinColumn(byte[][] f) {
        byte[][] c = new byte[f.length][f.length];
        for(int i = 0; i < f.length; i++)
            System.arraycopy(f[i], 0, c[i], 0, f.length);
        boolean tf = false;
        int mid = c.length / 2;
        int column = 0;

        for(int i = 0; i < c.length; i++) {
            int count = 0;
            for(int j = 0; j < c.length; j++) {
                count = c[j][i] == 1 ? count + 1 : count;
                if(count > mid) {
                    tf = true;
                    column = i;
                    break;
                }
            }
            if(tf) break;
        }
        if(tf) {
            for(int i = 0; i < c.length; i++)
                c[i][column] = (byte) (c[i][column] == 1 ? 0 : 1);
            int a = flipCoinRow(c);
            int b = flipCoinColumn(c);
            if(a <= b) return a;
            else return b;
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

        int a = flipCoinRow(c);
        int b = flipCoinColumn(c);

        if(a <= b) System.out.println(a);
        else System.out.println(b);
    }

}
