//MajorityElementOpCounter.java
import java.util.Scanner;

public class MajorityElementOpCounter {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int opCount = 0;

		while (in.hasNextLine()) {
			in.nextLine();
			opCount++;
		}

		System.out.println(opCount - 2);		
	}
}