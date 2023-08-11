package p26.self;

public class Solution {
    public int removeDuplicates(int[] nums) { // 1 <= nums.length <= 3 * 104
        int idx = 0;
        int last = -101; // -100 <= nums[i] <= 100

        for (int i=0; i < nums.length; i++) {
            if(nums[i] != last) {
                nums[idx] = nums[i];
                ++idx;

                last = nums[i];
            }
        }

        return idx;
    }
}
