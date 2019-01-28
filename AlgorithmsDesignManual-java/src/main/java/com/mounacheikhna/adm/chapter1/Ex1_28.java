package com.mounacheikhna.adm.chapter1;

import static org.junit.Assert.assertArrayEquals;

public class Ex1_28 {

    // division using substraction
    // int[] = {Q, R} (Quotient and Remainder)
    public int[] divide(int N, int D) {
        if (D == 0) {
            System.out.println("Division by zero error");
            return new int[]{0, 0};
        }
        if (D < 0) {
            int[] res = divide(N, -D);
            return new int[]{-res[0], res[1]};
        }
        if (N < 0) {
            int[] res = divide(-N, D);
            int Q = res[0];
            int R = res[1];
            if (R == 0) return new int[]{-Q, R};
            else return new int[]{-Q - 1, D - R};
        } else {
            return dividePos(N, D);
        }
    }

    private int[] dividePos(int N, int D) {
        int Q = 0, R = N;
        while (R >= D) {
            Q++;
            R -= D;
        }
        return new int[]{Q, R};
    }

    public static void main(String[] args) {
        Ex1_28 sol = new Ex1_28();
        assertArrayEquals(new int[]{2, 0}, sol.divide(4, 2));
        assertArrayEquals(new int[]{2, 1}, sol.divide(5, 2));
        assertArrayEquals(new int[]{-3, 1}, sol.divide(-5, 2));
        assertArrayEquals(new int[]{-2, 1}, sol.divide(5, -2));
    }

}
