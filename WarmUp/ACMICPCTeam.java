import java.io.*;
import java.util.*;

public class ACMICPCTeam {
	
	private static void maxFinder(ArrayList<String> ppl) {
		int maxTopics = 0;
		int numberOfMaxTeams = 0;
		for(int i = 0; i < ppl.size(); i++){
			for(int j = i+1; j < ppl.size(); j++){
				int topics = 0;
				for(int n = 0; n < ppl.get(i).length(); n++) {
					if(ppl.get(i).charAt(n) == '1' || ppl.get(j).charAt(n) == '1') {
						topics++;
					}
				}
				if(topics > maxTopics) {
					maxTopics = topics;
					numberOfMaxTeams = 1;
				} else if (topics == maxTopics){
					numberOfMaxTeams++;
				}
			}
		}
		
		System.out.println(maxTopics);
		System.out.println(numberOfMaxTeams);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
        int M = sc.nextInt();
		
        ArrayList<String> people = new ArrayList<String>();
        
        for(int i = 0; i < N; i++) {
        	people.add(sc.next());
        }
        
        maxFinder(people);
	}

}
