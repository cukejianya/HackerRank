import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class CavityMap {
	
	public static void findCavity(ArrayList<ArrayList<Integer>> arr) {
		for(int i = 1; i < arr.size() - 1; i++) {
			ArrayList<Integer> row = arr.get(i);
			for (int j = 1; j < arr.get(i).size() - 1; j++) {
				
				boolean top = arr.get(i-1).get(j) < arr.get(i).get(j);
				boolean bottom = arr.get(i+1).get(j) < arr.get(i).get(j); 
				boolean right = arr.get(i).get(j+1) < arr.get(i).get(j);
				boolean left = arr.get(i).get(j-1) < arr.get(i).get(j);
				
				if (top && bottom && right && left) {
					row.set(j, 99);
				}
			}
		}
		
		// System.out.println(arr);
		
		for(int i = 0; i < arr.size() ; i++) {
			ArrayList printRow = arr.get(i);
			String strRow = "";
			for (int j = 0; j < arr.get(i).size(); j++) {
				if ((int) printRow.get(j) == 99) {
					strRow += "X";
				} else {
					strRow += printRow.get(j).toString();
				}
			}
			System.out.println(strRow);
		}
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		ArrayList<ArrayList<Integer>> map = new ArrayList<>();
		for(int i = 0; i < T; i++) {
			BigInteger scNum = sc.nextBigInteger();
			BigInteger ten = new BigInteger("10");
			ArrayList<Integer> row = new ArrayList<>();
			while(scNum.signum() == 1) {
				BigInteger[] divAndRem = scNum.divideAndRemainder(ten);
				scNum = divAndRem[0];
				row.add(0, divAndRem[1].intValue());
			}
			map.add(row);
		}
		findCavity(map);
//		System.out.println(map.get(1).get(2));
		sc.close();
	}

}
