package main

import (
	"fmt"
	"os/exec"
)

func main() {
	unameCmd := exec.Command("uname", "-a")
	unameOut, err := unameCmd.Output()
	if err != nil {
		panic(err)
	}
	fmt.Println("> uname -a")
	fmt.Println(string(unameOut))
}
