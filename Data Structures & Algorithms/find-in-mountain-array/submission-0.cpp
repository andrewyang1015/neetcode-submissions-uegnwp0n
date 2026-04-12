/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
private:
    unordered_map<int, int> cache;

    int get(int val, MountainArray &mountainArr) {
        if (cache.contains(val)) return cache[val];

        cache[val] = mountainArr.get(val);
        return cache[val];
    }

    int binarySearch(int low, int high, bool ascending, int target, MountainArray &mountainArr) {
        while (low <= high) {
            int mid = (low + high) / 2;
            int val = get(mid, mountainArr);
            if (val == target) {
                return mid;
            }
            if (ascending == (val < target)) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }

public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        // First find the peak of the mountain using binary search
        int n = mountainArr.length();
        int low = 0, high = n - 1;
        int peak_idx = -1;

        while (low <= high) {
            int mid = (high + low) / 2;
            int prev = get(mid - 1, mountainArr);
            int curr = get(mid, mountainArr);
            int next = get(mid + 1, mountainArr);

            if (prev < curr && curr > next) {
                peak_idx = mid;
                break;
            // Inreasing: peak is to the right
            } else if (prev < curr && curr < next) {
                low = mid;
            // Decreasing: peak is to the left
            } else if (prev > curr && curr > next) {
                high = mid;
            }
        }

        // Check both sides of the peak idx to see if mountainArr->get(idx) == target
        int res1 = binarySearch(0, peak_idx, true, target, mountainArr);
        if (res1 != -1) return res1;

        int res2 = binarySearch(peak_idx, n - 1, false, target, mountainArr);
        return res2;
    }
};