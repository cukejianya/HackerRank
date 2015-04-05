import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

	public class MaxXor {
	/*
	 * Complete the function below.
	 */

	    static int maxXor(int l, int r) {
	        List<Integer> xorList = new ArrayList<Integer>();
	        List<Integer> xorOutputArr = new ArrayList<Integer>();
	        if (l == r) {
	        	return 0;
	        }
	        for (int i = l; i <= r;i++ ) {
	            for (int j = i+1; j <= r; j++) {         
                    double binL = binary(i);
                    double binR = binary(j);
                    // System.out.println(i +" binary: "+binL);
                    // System.out.println(j +" binary: "+binR);
                    int length = (int) Math.log10(binR)+1;
                    // System.out.println("Length: "+length);
                    xorOutputArr.clear();
                    for (int n = length-1; n >= 0; n--) {
                        int testL = (int) (binL/Math.pow(10, n));
                        int testR = (int) (binR/Math.pow(10, n));
                        binL = binL - testL * Math.pow(10, n);
                        binR = binR - testR * Math.pow(10, n);
                        // System.out.println("testL: "+testL);
                        // System.out.println("testR: "+testR);
                        if (testL != testR) {
                        	xorOutputArr.add(1);
                        } else {
                        	xorOutputArr.add(0);
                        }
                        // System.out.println("Output Array: "+xorOutputArr);
                    }
                    int xorOutPut = decimal(xorOutputArr);
                    xorList.add(xorOutPut);
	            }
	            
	        }
	        Collections.sort(xorList);
	        int lastElmId = xorList.size()-1;
	        // System.out.println(xorList);
	        return xorList.get(lastElmId);
	        
	    }
	    
	    static int decimal(List<Integer> arr) {
	    	int retNum = 0;
	    	for (int i = 0; i< arr.size(); i++){
	    		// System.out.println("Array index: "+arr.get(i));
	    		if (arr.get(i) == 1) {
	    			retNum = retNum + (int) Math.pow(2, arr.size()-i-1);
	    			// System.out.println("The "+(i+1)+"th retNum: "+retNum);
	    		}
	    	}
	    	return retNum;
	    }
	    
	    static double binary(int n) {
	        double binNum = 0;
	        int i = 0;
	        while(n>0) {
	            if(n%2==0) {
	                n = n/2;
	                
	            } else {
	                binNum = binNum + Math.pow(10,i);
	                n = n-1;
	                n = n/2;
	            }
	            i++;
	        }
	        return binNum;
	    } 
	    public static void main(String[] args) {
	        Scanner in = new Scanner(System.in);
	        int res;
	        int _l;
	        _l = Integer.parseInt(in.nextLine());
	        
	        int _r;
	        _r = Integer.parseInt(in.nextLine());
	        
	        res = maxXor(_l, _r);
	        System.out.println(res);

	        
	    }
	}

