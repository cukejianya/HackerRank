import java.io.*;
import java.util.*;
import java.math.*;

public class TaumAndBDay {
	
	public static BigInteger minCost(long B, long W, long X, long Y, long Z) {
		if (X < Z+Y && Y < Z+X) {
			BigInteger ans = BigInteger.valueOf(X*B + Y*W); 
			return ans;
		} else if (X < Y) {
			BigInteger ans = BigInteger.valueOf(X*B + (X+Z)*W);
			return ans;
		} else {
			BigInteger ans = BigInteger.valueOf((Y+Z)*B + Y*W);
			return ans;
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for (int i = 0; i < T; i++) {
			long B = sc.nextInt();
			long W = sc.nextInt();
			long X = sc.nextInt();
			long Y = sc.nextInt();
			long Z = sc.nextInt();
			System.out.println(minCost(B, W, X, Y, Z));
			
		}
	}

}
