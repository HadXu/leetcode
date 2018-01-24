# Longest Substring Without Repeating Characters

> 初始看来 还是有点难度的，思想就是使用两个指针,i和j,j来控制子串的头，i控制子串的尾，理想状态下i是一直++，但是由于重复字符的出现，因此j需要更新，注意点，j一直向前更新，也就是j比以前的j大。Python使用同理，只不过简单了一点。