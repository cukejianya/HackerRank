import java.io.*;
import java.util.*;

public class FindDigits {
	
	public static int finding(long num) {
		String strNum = Long.toString(num);
		int digitsDiv = 0;
		for(int j = 0; j < strNum.length(); j++) {
			int digit = Integer.parseInt(Character.toString(strNum.charAt(j))); 
			if (digit == 0) {
				
			} else if (num%digit == 0) {
				digitsDiv++;
			}
		}
		return digitsDiv;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int i = 0; i < T; i++) {
			long N = sc.nextLong();
			System.out.println(finding(N));
		}
		sc.close();
	}
}
