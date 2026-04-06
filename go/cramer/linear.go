package main

import "fmt"

func main() {
	var variables_amount int
	var equations_amount int
	fmt.Println("Welcome to Cramer linear systems calculator")
	fmt.Println("How many variables do you have?")
	fmt.Scanln(&variables_amount)
	fmt.Println("How many equations do you have?")
	fmt.Scanln(&equations_amount)
	fmt.Printf("We gonna have %v equations and %v variables \n", equations_amount, variables_amount)

	matrix_a := make([][]float64, equations_amount)
	matrix_b := make([]float64, variables_amount)
	matrix_c := make([]float64, equations_amount)

	for line := 0; line < equations_amount; line++ {
		matrix_a[line] = make([]float64, variables_amount)
		fmt.Printf("\n Equation n %v:\n", line)
		for column := 0; column < variables_amount; column++ {
			var value float64
			fmt.Printf("\tx[%v]*", column)
			fmt.Scan(&value)
			matrix_a[line][column] = value
		}
		var result float64
		fmt.Print("\t= ")
		fmt.Scan(&result)
		matrix_c[line] = result
	}
	fmt.Println("---------")
	fmt.Printf("A \t= %v \n", matrix_a)
	fmt.Printf("B \t= %v \n", matrix_b)
	fmt.Printf("C \t= %v \n", matrix_c)
	det_a := det(matrix_a)
	fmt.Printf("det(A) \t= %v \n", det_a)

	fmt.Println("---------------")
	fmt.Println("Lets calculate partial determinant")
	set_matrix_xn := make([][][]float64, variables_amount)
	det_xn := make([]float64, variables_amount)
	for xi := 0; xi < variables_amount; xi++ {
		set_matrix_xn[xi] = make([][]float64, equations_amount)
		//	Deep copy of matrix_a
		for line := 0; line < equations_amount; line++ {
			set_matrix_xn[xi][line] = make([]float64, equations_amount)
			for col := 0; col < variables_amount; col++ {
				set_matrix_xn[xi][line][col] = matrix_a[line][col]
			}
		}
		//	Then copy matrix_c into a col
		for line := 0; line < equations_amount; line++ {
			set_matrix_xn[xi][line][xi] = matrix_c[line]
		}
		fmt.Printf("x%v \t= %v \n", xi, set_matrix_xn[xi])
		det_xn[xi] = det(set_matrix_xn[xi])
		fmt.Printf("det(%v) \t= %v \n", xi, det_xn[xi])
	}
	fmt.Println("---------------")
	fmt.Println("Lets get values for the variables")
	set_xn_values := make([]float64, variables_amount)
	for n := 0; n < variables_amount; n++ {
		result := det_xn[n] / det_a
		set_xn_values[n] = result
		fmt.Printf("x%v \t= %v \n", n, result)
	}
}

func det(matrix [][]float64) float64 {
	i_len := len(matrix[0])
	j_len := len(matrix)

	var total float64 = 0

	for i := 0; i < i_len; i++ {
		var line_product float64 = 1.0
		for j := 0; j < j_len; j++ {
			index := (i + j) % i_len
			line_product *= matrix[j][index]
		}
		total += line_product
	}

	for i := 0; i < i_len; i++ {
		var line_product float64 = 1.0
		for j := 0; j < j_len; j++ {
			index := (i_len + i - j) % i_len
			line_product *= matrix[j][index]
		}
		total -= line_product
	}

	return total
}


