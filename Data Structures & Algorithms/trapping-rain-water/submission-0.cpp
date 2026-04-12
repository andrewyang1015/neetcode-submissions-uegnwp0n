class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int left = 0, right = n - 1;
        int largest_from_left = 0, largest_from_right = 0;
        int trapped_water = 0;

        while (left < right) {
            largest_from_left = max(largest_from_left, height[left]);
            largest_from_right = max(largest_from_right, height[right]);

            if (largest_from_left <= largest_from_right) {
                left++;
                trapped_water += max(0, largest_from_left - height[left]);
            } else {
                right--;
                trapped_water += max(0, largest_from_right - height[right]);
            }
        }
        return trapped_water;
    }
};
