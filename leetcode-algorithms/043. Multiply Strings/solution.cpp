string multiply(string num1, string num2) {
    auto l = num1.size() + num2.size();

    vector<int> v(l,0);

    for(int i=num1.size()-1;i>=0;i--)
        for(int j = num2.size()-1;j>=0;j--){
            int k = (num1[i]-'0') * (num2[j]-'0');
            int p1 = i+j;
            int p2 = i+j+1;
            int sum = k + v[p2];
            v[p1] += sum / 10;
            v[p2] = sum %10;
    }



    string s="";

    for(int k:v){
        if((s.size()==0 && k==0))
            continue;
        s.push_back(k+'0');
    }


    return s.size()==0?"0":s;
}
int main()
{
	return 0;
}