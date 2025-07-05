package main

import (
	"fmt"
	"os/exec"
)

func main() {
	// get last 10 lines of history
	historyCmd := exec.Command("fc", "-l", "-10")
	historyOut, err := historyCmd.Output()
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("> fc -l -10")
	fmt.Println(string(historyOut))
}
