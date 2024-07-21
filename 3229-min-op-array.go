package main

import (
	"fmt"
)

func restoreMatrix(rowSum []int, colSum []int) [][]int {

	rSum := func(r []int) int {
		sum := 0
		for _, v := range r {
			sum += v
		}
		return sum
	}

	cSum := func(m [][]int, cIndex int) int {
		sum := 0
		for _, v := range m {
			sum += v[cIndex]
		}
		return sum
	}

	// init with 0s
	res := make([][]int, len(rowSum))
	for i := range res {
		res[i] = make([]int, len(rowSum))
	}

	// index impl
	for i, _ := range rowSum {
		if rowSum[i] < colSum[i] {
			res[i][i] = rowSum[i]
			rowSum[i] = 0
		} else if colSum[i] < rowSum[i] {
			res[i][i] = colSum[i]
			colSum[i] = 0
		} else {
			res[i][i] = rowSum[i]
			rowSum[i] = 0
		}
	}

	for i, v := range rowSum {
		if v != 0 {
			if colSum[i+1] > 0 && i < len(colSum)-1 {
				tempMax := colSum[i+1]
				tempIndex := i + 1
				for j := i + 1; j < len(colSum); j++ {
					if tempMax < colSum[j] {
						tempMax = colSum[j]
						tempIndex = j
					}
				}

				val := rowSum[i] - rSum(res[i])
				for val+cSum(res, tempIndex) != colSum[tempIndex] {
					val--
				}
				res[i][tempIndex] = val
				colSum[tempIndex] = 0
			} else {
				if rSum(res[i]) != rowSum[i] {
					res[i][i-1] = rowSum[i] - rSum(res[i])
				}
			}
		}
		if colSum[i] != 0 {
			if rowSum[i+1] > 0 && i < len(colSum)-1 {
				tempMax := rowSum[i+1]
				tempIndex := i + 1
				for j := i + 1; j < len(colSum); j++ {
					if tempMax < rowSum[j] {
						tempMax = rowSum[j]
						tempIndex = j
					}
				}
				val := colSum[i] - cSum(res, i)

				for val+rSum(res[tempIndex]) != rowSum[tempIndex] {
					val -= 1
				}
				res[tempIndex][i] = val
				rowSum[tempIndex] = 0
			} else {
				if cSum(res, i) != colSum[i] {
					res[i-1][i] = colSum[i] - cSum(res, i)
				}
			}
		}
	}

	return res

}

func main() {

	// t1 := []int{10, 4, 1}
	// t2 := []int{5, 4, 6}
	t1 := []int{8, 6, 8}
	t2 := []int{5, 7, 10}

	fmt.Println(restoreMatrix(t2, t1))
}
