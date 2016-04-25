public class Changer {
	private int[] denoms;
	public Changer(int[] denominations) {
		denoms = new int[denominations.length + 1]; //want to store zero as a denomination
		denoms[0] = 0;
		for (int i = 0; i < denominations.length; i++) {
			denoms[i + 1] = denominations[i];
		}
	}

	public boolean can_make_change_for(int amount) {
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
		return false;
	}

	public static void print_grid(boolean[][] grid, int amount, int[] denoms) {
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
	public static void main(String[] args) {
		int[] denoms = {2,4,9};

		Changer c = new Changer(denoms);
		
		System.out.println(c.can_make_change_for(0));
		System.out.println(c.can_make_change_for(12));
		System.out.println(c.can_make_change_for(5));

	}
}