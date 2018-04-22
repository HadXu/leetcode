class Solution {
public:
    double myPow(double x, int n) {
        long long p;
        if(n<0){
            p = -n;
            x = 1/x;
        }else
            p = n;
        double res = 1.;
        while(p){
            if(p&1){
                res *= x;
            }
            x *= x;
            p >>=1;
        }
        return res;
    }
};

int main()
{
    return 0;
}