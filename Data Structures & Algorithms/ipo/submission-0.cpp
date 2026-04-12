#include <ranges>
class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        // Only sorted by capital in ascending order
        auto compare_unavail = [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second > b.second;
        };

        // Only sorted by profits in descending order
        auto compare_avail = [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.first < b.first;
        };

        int total_capital = w;

        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(compare_unavail)> pq_unavail(compare_unavail);
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(compare_avail)> pq_avail(compare_avail);

        // Initial state, put everything into unavailable or available based on w threshold
        for (const auto& [p, c]: std::views::zip(profits, capital)) {
            if (total_capital >= c) {
                pq_avail.push(make_pair(p, c));
            } else {
                pq_unavail.push(make_pair(p, c));
            }
        }

        for (int i = 0; i < k; i++) {
            // Remove the best option from available and add to total capital
            if (!pq_avail.empty()) {
                pair<int, int> project = pq_avail.top();
                pq_avail.pop();

                total_capital += project.first;
            }

            // Add all newly available projects on
            while (!pq_unavail.empty() && total_capital >= pq_unavail.top().second) {
                pair<int, int> new_project = pq_unavail.top();
                pq_unavail.pop();
                pq_avail.push(new_project);
            }
        }

        return total_capital;
    }
};