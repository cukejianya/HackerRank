import java.io.*;
import java.util.*;

public class SherlockAndGCD {
	
	private static String findB(ArrayList<Integer> A){
		Collections.sort(A);
		// System.out.println(A);
		if (A.get(0) == 1) {
			return "YES";
		} else {	
			for(int i = 0; i < A.size(); i++) {
				for(int j = i+1; j < A.size(); j++){
					// System.out.println(A.get(i)+ " "+A.get(j));
					// System.out.println(gcd(A.get(i), A.get(j)));
					if (gcd(A.get(i), A.get(j)) == 1) {
						
						return "YES";
					}
				}
			}
		}
		return "NO";
	}
	
	public static int gcd(int x, int y) {
		int a = Math.max(x, y);
		int b = Math.min(x, y);
		int c = 0;
		while (a > 0) {
			c = a;
			a = b%a;
			b = c;
		}
		return b;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int i = 0; i < T; i++) {
			int N = sc.nextInt();
			ArrayList A = new ArrayList<Integer>();
			for(int j = 0; j < N; j++){
				A.add(sc.nextInt());
			}
			Set<Integer>set = new HashSet<Integer>();
			set.addAll(A);
			A.clear();
			A.addAll(set);
			// System.out.println(i+1+": "+A);
			System.out.println(findB(A));
		}
		
		

	}

}
