import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class CutTheSticks {
	public static void cutting(List<Integer> arr){
		int elm;
		int smallest;
		while(arr.size() > 0) {
			System.out.println(arr.size()+" "+arr);
			smallest = arr.get(0);
			for(int i = 0; i < arr.size(); i++){
				elm = arr.get(i) - smallest;
				arr.set(i, elm);
				if (arr.get(i) == 0) {
					arr.remove(i);
					i--;
				}
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		List<Integer> listSticks = new ArrayList<Integer>();
		
		for (int i=0; i<N; i++) {
			listSticks.add(sc.nextInt());
		}
		Collections.sort(listSticks);
		cutting(listSticks);
	}
}
