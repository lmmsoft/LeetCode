import java.time.LocalDate;

class Solution {

	public int dayOfYear(String date) {
		return LocalDate.parse(date).getDayOfYear();
	}
}

import java.util.Calendar;
class Solution2 {
    public int dayOfYear(String date) {
        Calendar cld = Calendar.getInstance();
        int[] time = Arrays.stream(date.split("-")).mapToInt(t -> Integer.parseInt(t)).toArray();
        cld.set(time[0], time[1] - 1, time[2]);
        return cld.get(Calendar.DAY_OF_YEAR);
    }
}
