import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class LonelyInteger {
	
	public static int findInteger(List<Integer> arr) {
		int elm = arr.get(0);
		if(arr.size()==0) {
			return elm;
		}
		for(int i=0; i<arr.size(); i+=2) {
			elm = arr.get(i);
			if(i == arr.size()-1) {
				return elm;
			} else if (elm != arr.get(i+1)){
				return elm;
			}
		}
		return 0;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		List<Integer> intList = new ArrayList<Integer>();
		
		for(int i=0; i < N; i++) {
			intList.add(sc.nextInt());
		}
		
		Collections.sort(intList);
		
		int ans = findInteger(intList);
		
		System.out.print(ans);
		
	}

}
