import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class SherlockAndTheBeast {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for (int i = 0; i < T; i++) {
			int N = sc.nextInt();	
			if (N == 1 || N==2 || N == 4 || N==7){
				System.out.println(-1); 
			} else {
				int numOf5 =  Math.floorDiv(N, 3);
				int mod3 = N%3;
				int transfer = 0;
				int subtractOne = 0;
				if (mod3 == 2) {
					transfer = 1;
				} else if(mod3 == 1){
					transfer = 2;
					subtractOne = 1;
				}
				numOf5 -= (transfer + subtractOne);
				numOf5 *= 3;
				int numOf3 =  transfer * 5;
				
				String str5 = new String(new char[numOf5]).replace("\0", "5");
				String str3 = new String(new char[numOf3]).replace("\0", "3");
				String combineStr = str5+str3;
				System.out.println(combineStr);
			}
			
		}
		
	}

}
