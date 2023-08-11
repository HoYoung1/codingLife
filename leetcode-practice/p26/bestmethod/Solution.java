package p26.bestmethod;

public class Solution {
    public int removeDuplicates(int[] nums) {
        int idx = 0;

        for (int i=0; i < nums.length; i++) {
            if(nums[i] != nums[i]) {
                nums[idx] = nums[i];
                ++idx;

                last = nums[i];
            }
        }

        return idx;
    }
}
