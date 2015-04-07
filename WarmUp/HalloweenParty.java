import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class HalloweenParty {
	
	
	public static void main(String[] arg){
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		long k, m;
		long ans;
		for(int i = 0; i < t; i++){
			k = sc.nextInt();
			m = (int) k/2;
			if (k%2==1){
				m++;
			}
			k =(int) k/2;
			ans = (m*k);
			// String stringAns = String.valueOf(ans);
			System.out.println(ans+" k: "+k+" m: "+m);
		}
		sc.close();
	}
}
