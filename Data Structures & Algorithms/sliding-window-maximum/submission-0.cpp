class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        deque<int> s;
        for (int i = 0; i < k; i++) {
            while (!s.empty() && s[s.size() - 1] < nums[i]) {
                s.pop_back();
            }
            s.push_back(nums[i]);
        }
        
        vector<int> res(n - k + 1, 0);
        res[0] = s[0];

        // Each window we will remove the left value
        // then keep popping until the stack is monotonic decreasing again
        // then get s[0] for res
        for (int right = k; right < n; right++) {
            int left = right - k;
            // Remove left if it's the maximum
            if (nums[left] == s[0]) s.pop_front();

            // Adding the right elt in the window
            while (!s.empty() && s[s.size() - 1] < nums[right]) {
                s.pop_back();
            }
            s.push_back(nums[right]);

            res[left + 1] = s[0];
        }
        return res;
    }
};
