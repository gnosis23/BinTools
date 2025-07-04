package main

import (
	"fmt"
	"os/exec"
)

func main() {
	// get last 10 lines of history
	historyCmd := exec.Command("bash", "-c", "id")
	historyOut, err := historyCmd.Output()
	if err != nil {
		panic(err)
	}
	fmt.Println("> id")
	fmt.Println(string(historyOut))
}
