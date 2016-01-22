public class SquareRoot {

	public static double sqrt( double x, double constraint ) {
		
		if ( x < 0 || constraint <= 0 || constraint >= 1) {
			throw new IllegalArgumentException();
		}
		else if (x == 0 || x == 1) {
			return x;
		}
		else {
			double range = constraint * x;
			double s;
			double left;
			double right;
			double upperBound = x + range;
			double lowerBound = x - range;

			if (x < 1) {
				s = 1;
				left = x;
				right = s;
			}
			else {
				s = 0;
				left = 0;
				right = x;
			}
			while (!(s * s <= x + range && s * s >= x - range)) {
				if (s * s <= x + range) {
					left = s;
					s = (left + right) / 2.0;
				}
				else {
					right = s;
					s = (left + right) / 2.0;
				}
			}

			return s;
		}
		
	}

}