import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class TheLoveLetterMystery {
	
	public static int operation(List<String> arr) {
		int arrSize = arr.size()-1;
		int operAmount = 0;
		for (int i = 0; i <= arrSize/2; i++) {
			int firstElm =  (int) arr.get(i).charAt(0);
			int lastElm = (int) arr.get(arrSize-i).charAt(0);
			operAmount = operAmount + Math.abs(firstElm-lastElm);
		}
		return operAmount; 
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		
		for (int i=0; i < T; i++) {
			String str = sc.next();
			List<String> arrStr = Arrays.asList(str.split(""));
			System.out.println(arrStr);
			int ans = operation(arrStr);
			System.out.println(ans);
		}
	}

}
