package main

import (
	"fmt"
	"os/exec"
)

func main() {
	historyCmd := exec.Command("id")
	historyOut, err := historyCmd.Output()
	if err != nil {
		panic(err)
	}
	fmt.Println("> id")
	fmt.Println(string(historyOut))
}
