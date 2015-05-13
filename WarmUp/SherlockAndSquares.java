import java.io.*;
import java.util.*;


public class SherlockAndSquares {
	
	private static int findSquares(long A, long B) {
		int extra = 0;
		if(Math.sqrt(A) == (int) Math.sqrt(A)) {
			extra++;
		}
		int a = (int) Math.floor(Math.sqrt(A));
		int b = (int) Math.floor(Math.sqrt(B));
		return b-a+extra;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int i = 0; i < T; i++) {
			long A = sc.nextLong();
			long B = sc.nextLong();
			System.out.println(findSquares(A, B));
		}
	}

}
