class Solution {
public:
    int binarySearch(vector<int>& arr, int target) {
        int n = arr.size() - 1;
        // Corner case when target bigger than everything
        if (target >= arr[n]) return n;

        int low = 0, high = n;
        while (low < high) {
            int mid = (high + low) / 2;

            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        // Manual correction
        if (low > 0 && abs(arr[low - 1] - target) <= abs(arr[low] - target)) low--;
        return low;
    }

    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int n = arr.size();
        int start = binarySearch(arr, x);
        
        int left = start, right = start;
        for (int i = 0; i < k - 1; i++) {
            if (left == 0) {
                right++;
                continue;
            }
            if (right == n - 1) {
                left--;
                continue;
            }

            if (abs(arr[left - 1] - x) <= abs(arr[right + 1] - x)) {
                left--;
            } else {
                right++;
            }
        }

        return vector<int>(arr.begin() + left, arr.begin() + right + 1);
    }
};