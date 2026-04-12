class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        int running_sum = 0;

        unordered_map<int, int>frequencies;
        frequencies[0] = 1;

        int total = 0;

        for (int i = 0; i < n; i++) {
            running_sum += nums[i];
            int target = running_sum - k;

            if (frequencies.contains(target)) {
                total += frequencies[target];
            }
            frequencies[running_sum]++;
        }
        
        return total;
    }
};