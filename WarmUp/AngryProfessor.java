import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


public class AngryProfessor {
	
	public static String cancelClass(ArrayList<Integer> arr, int num){
		int count = 0;
		for(int j = 0; j < arr.size(); j++) {
			if(arr.get(j) <= 0) {
				count++;
			}
		}
		if (count < num) {
			return "Yes";
		} else {
			return "No";
		}
	}
	
	public static void main(String[] arg) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		int N;
		int a;
		ArrayList<Integer> studentsTime = new ArrayList<Integer>();
		for(int i=0; i < T; i++) {
			N = sc.nextInt();
			a = sc.nextInt();
			for(int j=0; j < N; j++){
				studentsTime.add(sc.nextInt());
			}
			System.out.println(cancelClass(studentsTime, a));
			studentsTime.clear();
		}
		
	}
}
