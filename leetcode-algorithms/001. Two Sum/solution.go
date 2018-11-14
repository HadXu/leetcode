package main

import "fmt"

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i, v := range nums {
		if j, ok := m[target - v]; ok {             
			return []int{j, i}
		} else {
			m[v] = i
		}
	}
	return []int{-1, -1}
}

func main() {
	var nums = []int{2,7,11,15}
	var target int = 18
	res :=  twoSum(nums, target)
	fmt.Println(res)
}