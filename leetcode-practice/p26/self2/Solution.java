package p26.self2;

public class Solution {
    public int removeDuplicates(int[] nums) { // 1 <= nums.length <= 3 * 104
        int idx = 0;

        for (int i=0; i < nums.length-1; i++) {
            if(nums[i] != nums[i+1]) {
                nums[idx] = nums[i];
                ++idx;

                last = nums[i];
            }
        }

        return idx;
    }
}
