1. dp[i][0] = i;
2. dp[0][j] = j;
3. dp[i][j] = dp[i - 1][j - 1], if word1[i - 1] = word2[j - 1];
4. dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1), otherwise.