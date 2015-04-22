import java.io.*;
import java.util.*;

public class ManasaAndStones {

	public static void stoneCount(int N, int a, int b) {
		String maxStone = "";
		int min = Math.min(a, b);
		int max = Math.max(a, b);
		if(max != min) {
			for (int i = 0; i < N; i++) {
				int stone = (i*max) + ((N-1-i)*min);
				if (i < N-1) { 
					maxStone += stone +" ";
				} else {
					maxStone += stone;
				}
			}
		} else {
			int stone = (N-1)*min;
			maxStone += stone;
		}
		System.out.println(maxStone); 
	}
	
	public static void main(String arg[]) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for (int i = 0; i < T; i++) {
			int N = sc.nextInt();
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			stoneCount(N, a, b);
		}
		
		sc.close();
	}
}
