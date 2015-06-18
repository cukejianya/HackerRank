import java.io.*;
import java.util.*;

public class FillingJar {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		long total = 0;
		for (int i = 0; i < M; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int k = sc. nextInt();
			total += (1+b-a)*100;
		}
		long average = (long) Math.floor(total/N);
		System.out.println(average);
	}

}
