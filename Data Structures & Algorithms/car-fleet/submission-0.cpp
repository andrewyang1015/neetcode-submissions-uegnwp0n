class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> zipped;
        int n = position.size();

        for (int i = 0; i < n; i++) {
            zipped.push_back({position[i], speed[i]});
        }

        sort(zipped.begin(), zipped.end());
        vector<float> merged_cars;

        for (int i = zipped.size() - 1; i >= 0; i--) {
            float time_taken = static_cast<float>(target - get<0>(zipped[i])) / get<1>(zipped[i]);

            // Car only forms a new fleet if it goes faster than the fleet right behind it
            if (merged_cars.empty() || time_taken > merged_cars.back()) {
                merged_cars.push_back(time_taken);
            }
        }

        return merged_cars.size();
    }
};
