public class MajorityElement {
	
	public static Integer[] major(Object[] ar, int start, int end) {
		System.out.println("running major..."); //used to determine time complexity

		int sz = end - start;

		if (sz > 1) {

			int mid = start + (sz / 2);
			Integer[] left = major(ar, start, mid);
			Integer[] right = major(ar, mid, start + sz);
							
				if (left[0] == null && right[0] == null) 

					return new Integer[] {null, (Integer) 0};
				
				else {

					if (left[0] == null && right[0] != null) 

						return new Integer[] {right[0], (Integer) 1};
					
					else if (right[0] == null && left[0] != null) 

						return new Integer[] {left[0], (Integer) 1};

					else {
						
						if (left[0] != right[0]) 

							if (left[1] == right[1])

								return new Integer[] {null, (Integer) 0};

							else
								
								if (left[1] == 2)

									return new Integer[] {left[0], (Integer) 1};
								
								else
									
									return new Integer[] {right[0], (Integer) 1};
						
						else 
						
							return new Integer[] {left[0], (Integer) 2};

					}
				}
		}

		else return new Integer[] {(Integer) ar[start], (Integer) 1};
	}
	public static void printAr(Object[] ar, int st, int end) {

		for (int i = st; i < end; i++) System.out.print(ar[i] + " ");

		System.out.println();
	
	}

	public static void printOut(Object[] ar) {
		System.out.println(ar.length);
		System.out.print("I/P: ");
		printAr(ar, 0, ar.length);
		
		Integer[] maj = major(ar, 0, ar.length);
		String res = "";
		
		if (maj[1].equals((Integer) 2)) {
			res += maj[0];
		}
		
		else {
			int count = 0;
			
			for (int i = 0; i < ar.length; i++) {
				if (ar[i] == maj[0]) count++;
			}
			
			if (count > ar.length/2) res += maj[0];
			else res += "none";
		}
		
		System.out.println("O/P: " + res);
	}
	public static void main(String[] args) {

		Integer[] in = new Integer[args.length];

		for (int i = 0; i < args.length; i++) {
			in[i] = Integer.parseInt(args[i]); 
		}

		printOut(in);
		
	}
}