import java.util.Arrays;

public class Changer {
	private int[] denoms;
	public Changer(int[] denominations) {
		denoms = new int[denominations.length + 1]; //want to store zero as a denomination
		denoms[0] = 0;
		for (int i = 0; i < denominations.length; i++) {
			denoms[i + 1] = denominations[i];
		}
		Arrays.sort(denoms); //should make it simpler to minimize coin amounts in max_coins
	}

	public boolean can_make_change_for(int amount) { //need to check this method
		if (amount == 0) {
			return true;
		}
		boolean[][] grid = new boolean[denoms.length][amount + 1];
		grid[0][0] = true;

		for (int i = 1; i < denoms.length; i++) {
			for (int j = 0; j <= amount; j++) {
				if (j - denoms[i] < 0) {
					grid[i][j] = grid[i - 1][j];
				}
				else {
					if (j % denoms[i] == 0) {
						grid[i][j] = true;
					}
					else {
						grid[i][j] = grid[i - 1][j] || grid[i][j - denoms[i]];
					}
				}
			}
		}
		return grid[denoms.length - 1][amount];
	}

	public boolean can_make_change_using_each_coin_once(int amount) {
		if (amount == 0) {
			return true;
		}
		boolean[][] grid = new boolean[denoms.length][amount + 1];
		grid[0][0] = true;
		for (int i = 1; i < denoms.length; i++) {
			for (int j = 0; j <= amount; j++) {
				if (j - denoms[i] < 0) {
					grid[i][j] = grid[i - 1][j];
				}
				else {
					grid[i][j] = grid[i - 1][j] || grid[i - 1][j - denoms[i]];
				}
			}
		}
		
		return grid[denoms.length - 1][amount];
	}

	public boolean can_make_change_with_limited_coins(int amount, int max_coins) {
		if (amount == 0) {
			return true;
		}
		int[][] grid = new int[denoms.length][amount + 1];
		for (int i = 0; i < denoms.length; i++) {
			for (int j = 0; j <= amount; j++) {
				grid[i][j] = -1; //initialize to negative values for later checking
			}
		}
		grid[0][0] = 0;
		for (int i = 1; i < denoms.length; i++) {
			for (int j = 0; j <= amount; j++) {
				if (j - denoms[i] < 0) {
					grid[i][j] = grid[i - 1][j];
				}
				else {
					int add_coin = -1;
					int no_new_coin = -1;

					if (grid[i - 1][j - denoms[i]] >= 0) {
						if (grid[i][j - denoms[i]] >= 0) {
							//minimize number of coins (possible that current row number is min)
							add_coin = (grid[i - 1][j - denoms[i]] < grid[i][j - denoms[i]] ? 
									    grid[i - 1][j - denoms[i]] : grid[i][j - denoms[i]]); 
							add_coin++;
						}
						else {
							add_coin = grid[i - 1][j - denoms[i]] + 1;
						}
						
					} 
					if (j % denoms[i] == 0) {
						//if current coin can be added multiple times (greedy, will minimize coin amt)
						add_coin = j / denoms[i]; 
					} 
					else {
						no_new_coin = grid[i - 1][j];
					}

					if (add_coin >= 0 && no_new_coin >= 0) {
						//set grid position to minimum coin value for that sum
						grid[i][j] = (add_coin < no_new_coin ? add_coin : no_new_coin); 
					}

					else {
						//if one option is impossible, return the possible one
						grid[i][j] = (add_coin > no_new_coin ? add_coin : no_new_coin); 
					}
				}
			}
		}
		//print_int_grid(grid, amount, denoms); //for testing purposes 
		return grid[denoms.length - 1][amount] <= max_coins;
	}

	public static void print_boolean_grid(boolean[][] grid, int amount, int[] denoms) {
		for (int i = 0; i <= amount; i++) {
			if (i == 0) {
				System.out.print("   ");
			}
			System.out.print(i + " ");
		}
		System.out.println();
		for (int i = 0; i < denoms.length; i++) {
			System.out.print(i + ": ");
			for (int j = 0; j <= amount; j++) {
				if (grid[i][j]) {
					System.out.print("T ");	
				}
				else {
					System.out.print("F ");
				}
			}
			System.out.println();
		}
	}

	public static void print_int_grid(int[][] grid, int amount, int[] denoms) {
		for (int i = 0; i <= amount; i++) {
			if (i == 0) {
				System.out.print("   ");
			}
			System.out.format("%02d ", i);
		}
		System.out.println();
		for (int i = 0; i < denoms.length; i++) {
			System.out.print(i + ": ");
			for (int j = 0; j <= amount; j++) {
				System.out.format("%02d ", grid[i][j]);
			}
			System.out.println();
		}
	}
	public static void main(String[] args) {
		int[] denoms = {2,4,9};

		Changer c = new Changer(denoms);
		
		System.out.println(c.can_make_change_for(0));
		System.out.println(c.can_make_change_for(12));
		System.out.println(c.can_make_change_for(5));

		int[] denoms2 = {5,10};
		Changer c2 = new Changer(denoms2);

		c2.can_make_change_with_limited_coins(35, 6);
		c2.can_make_change_with_limited_coins(55, 6);
		c2.can_make_change_with_limited_coins(65, 6);


	}
}