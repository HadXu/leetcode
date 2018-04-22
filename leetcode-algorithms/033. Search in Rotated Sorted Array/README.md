Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).


# 解决方案


开始没有想出来，后来看了俄罗斯的一个大神的思想，特别奇妙

Let’s say nums looks like this: ```[12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]```

1. If target is let’s say 14, then we adjust nums to this, where “inf” means infinity:

    ```[12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]```

2. If target is let’s say 7, then we adjust nums to this:

    ```[-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]```


这样处理以后，就直接能够使用二分法了。


