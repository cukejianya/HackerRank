import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class ChocolateFeast {
	public static int chocoAmount(int N, int C, int M) {
		N = (int)Math.floor(N/C);
		int totalCoco = N;
		while (M<=N) {
			totalCoco++;
			N-=(M-1);
		}
		return totalCoco;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int N,C,M;
		 for (int i = 0; i < T; i++){
			 N = sc.nextInt();
			 C = sc.nextInt();
			 M = sc.nextInt();
			 System.out.println(chocoAmount(N,C,M));
		 }
	}
}
