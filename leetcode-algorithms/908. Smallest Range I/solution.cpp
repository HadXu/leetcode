class Solution {
public:
    int smallestRangeI(vector<int>& A, int K) {
        int a = A[0], b = A[0];
        for (int i : A) 
            a = max(a, i), b = min(b, i);
        return max(0, a - b - 2 * K);
    }
};