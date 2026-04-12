class Solution {
public:
    int can_split(vector<int>& nums, int target_val, int subarrays_allotted) {
        int used_subarrays = 1;
        int value = 0;
        for (int num: nums) {
            if (value + num > target_val) {
                value = num;
                used_subarrays++;
            } else {
                value += num;
            }
        }
        return used_subarrays <= subarrays_allotted;
    }

    int splitArray(vector<int>& nums, int k) {
        int n = nums.size();
        auto i = max_element(nums.begin(), nums.end());
        int low = *i, high = accumulate(nums.begin(), nums.end(), 0);;
        int minimized_largest_split = 0;

        while (low < high) {
            int mid = (high + low) / 2;
            if (can_split(nums, mid, k)) {
                minimized_largest_split = mid;
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
        
    }
};