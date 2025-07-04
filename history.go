package main

import (
	"fmt"
	"os/exec"
)

func main() {
	// get last 10 lines of history
	historyCmd := exec.Command("bash", "-c", "history 10")
	historyOut, err := historyCmd.Output()
	if err != nil {
		panic(err)
	}
	fmt.Println("> history 10")
	fmt.Println(string(historyOut))
}
