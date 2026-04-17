class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<pair<int, int>> stack;
        int max_area = 0;

        for (int i = 0; i < n; i++) {
            int idx_to_insert = i;
            while(!stack.empty() && heights[i] < stack.back().second) {
                pair<int, int> elt_removed = stack.back();
                stack.pop_back();

                int width = i - elt_removed.first;
                int height = elt_removed.second;

                max_area = max(max_area, width * height);

                // Trick: need to use the last removed value as the index to insert
                // this height into
                idx_to_insert = elt_removed.first;
            }
            stack.push_back(make_pair(idx_to_insert, heights[i]));
        }

        // Clean up the stack at the end by popping all the elements
        while (!stack.empty()) {
            pair<int, int> elt_removed = stack.back();
            stack.pop_back();

            int width = n - elt_removed.first;
            int height = elt_removed.second;
            max_area = max(max_area, width * height);
        }
        return max_area;
    }
};
