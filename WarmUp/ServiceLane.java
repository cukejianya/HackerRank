import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class ServiceLane {
	
	public static int vehicleFinder(int in, int out, List<Integer> wd) {
		int lgWid = 3;
		for(int i = in; i <= out; i++) {
			if(wd.get(i) == 1) {
				return (int) 1;
			} else if (wd.get(i) < lgWid) {
				lgWid = 2;
			}
		}
		return lgWid;
	}
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int T = sc.nextInt();
		
		List<Integer> width = new ArrayList<Integer>();
		for(int k = 0; k < N; k++) {
			width.add(sc.nextInt());
		}
		
		int entry = sc.nextInt();
		int exit = sc.nextInt();
		
		int typeOfVehicle = vehicleFinder(entry, exit, width);
		
		System.out.println(typeOfVehicle);
		
		sc.close();
	}
}
