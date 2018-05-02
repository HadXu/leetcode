class Solution {
public:
    void solveSudoku(vector<vector<char>>& B) { go(B); }
private:
    bool go(vector<vector<char>>& B){
        for (int i=0,N=(int)B.size(); i<N; ++i) for (int j=0; j<N; ++j){
            if (isdigit(B[i][j])) continue;
            for (int k='1'; k<='9'; ++k){
                if (!valid(B,i,j,k)) continue;
                B[i][j]=k;
                if (go(B)) return true;
                B[i][j]='.';
            }
            return false;
        }
        return true;
    }
    bool valid(vector<vector<char>>& B, int i, int j, char k){
        for (int x=0; x<B.size(); ++x)
            if (B[i][x]==k || B[x][j]==k) return false;
        for (int begX=(i>5)?6 : (i>2)?3 : 0,x=begX; x<begX+3; ++x)
            for (int begY=(j>5)?6 : (j>2)?3 : 0,y=begY; y<begY+3; ++y)
                if (B[x][y]==k) return false;
        return true;
    }
};

