class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> s;
        int i=0;
        for(int p : pushed){
            s.push(p);
            while(s.size() && s.top() == popped[i])
                s.pop(),i += 1;
        }
        return s.empty();
    }
};