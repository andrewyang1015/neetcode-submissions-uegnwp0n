class Solution {
public:
    string minWindow(string s, string t) {
        int n = s.length();
        int m = t.length();
        unordered_map<char, int> t_ct, window_ct;
        int matches = 0;

        for (int i = 0; i < m; i++) t_ct[t[i]]++;

        int left = 0;
        pair<int, int> boundaries = {-1, -1};

        for (int right = 0; right < n; right++) {
            char r = s[right];
            window_ct[r]++;

            // Matching technique
            if (t_ct.count(r) && window_ct[r] == t_ct[r]) matches++;

            while (left <= right && matches == t_ct.size()) {
                int window = right - left + 1;

                int og_left = boundaries.first, og_right = boundaries.second;

                if ((og_left == -1 && og_right == -1) || (og_left != -1 && og_right != -1 && window < og_right - og_left + 1)) {
                    boundaries = {left, right};
                }

                // Shrink left and update matching
                char l = s[left];
                if (t_ct.count(l) && window_ct[l] == t_ct[l]) matches--;
                window_ct[l]--;
                left++;
            }  
        }

        if (boundaries.first == -1 && boundaries.second == -1) return "";

        int window = boundaries.second - boundaries.first + 1;
        return s.substr(boundaries.first, window);
    }
};
