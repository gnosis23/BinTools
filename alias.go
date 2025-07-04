package main

import (
	"fmt"
	"os/exec"
)

func main() {
	aliasCmd := exec.Command("/usr/bin/alias")
	aliasOut, err := aliasCmd.Output()
	if err != nil {
		panic(err)
	}
	fmt.Println("> alias")
	fmt.Println(string(aliasOut))
}
