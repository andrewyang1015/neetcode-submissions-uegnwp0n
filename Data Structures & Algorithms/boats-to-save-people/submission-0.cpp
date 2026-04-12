class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int boats_needed = 0;
        sort(people.begin(), people.end());
        int light = 0, heavy = people.size() - 1;

        while (light < heavy) {
            if (people[light] + people[heavy] <= limit) {
                light++;
            }
            heavy--;
            boats_needed++;
        }
        
        // Odd person out needs a boat
        if (light == heavy) boats_needed++;
        
        return boats_needed;
    }
};