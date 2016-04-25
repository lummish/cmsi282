//ChangerTestHarness.java
public class ChangerTestHarness {
	private int tests;
	private int passed;

	public ChangerTestHarness(){
		tests = 0;
		passed = 0;
	}

	public void can_make_change_for_test() {
		return;
	}

	public void can_make_change_once_test() {
		int[] denoms = {1,5,10,20};
		Changer c = new Changer(denoms);

		try {
			tests++;
			if (c.can_make_change_using_each_coin_once(16)) {				
				passed++;
			}
			tests++;
			if (c.can_make_change_using_each_coin_once(31)) {				
				passed++;
			}
			tests++;
			if (!c.can_make_change_using_each_coin_once(40)) {
				passed++;
			}
		}
		catch (Exception e) {
			System.out.println("Exception!");
		}
	}

	public static void main(String[] args) {
		ChangerTestHarness tester = new ChangerTestHarness();
		tester.can_make_change_once_test();
		System.out.println("Tests: " + tester.tests);
		System.out.println("Passed: " + tester.passed);
	}
}