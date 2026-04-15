class FreqStack {
private:
    unordered_map<int, int> frequencies;
    unordered_map<int, vector<int>> orderings_by_frequency;
    int max_frequency = 0;

public:
    FreqStack() {
        
    }
    
    void push(int val) {
        // Update frequency and max (as needed), add associated new frequency in ordering
        int prevFreq = frequencies[val];
        frequencies[val]++;
        max_frequency = max(max_frequency, frequencies[val]);

        orderings_by_frequency[prevFreq + 1].push_back(val);
    }
    
    // order[freq][-1] contains most recently added element for that frequency
    // Update max_frequency if we ran out of the most frequent element
    int pop() {
        int n = orderings_by_frequency[max_frequency].size();
        int val = orderings_by_frequency[max_frequency][n - 1];

        orderings_by_frequency[max_frequency].pop_back();
        frequencies[val]--;

        if (n - 1 == 0) max_frequency--;

        return val;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */