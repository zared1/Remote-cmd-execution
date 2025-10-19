# Remote Command Execution

A simple Python TCP client that connects to a remote host, sends a command, and prints the server’s response. **For educational purposes only** — do not run on unauthorized machines.

## Features

* Connects to a remote host via TCP
* Sends a single command provided as a command-line argument
* Receives and prints output from the server

## How to Run

1. Make sure a TCP server is running on the target host and port.
2. Run the client script with the command to execute:

```bash
python code.py <command>
# Example:
python code.py "whoami"
```

3. The server’s response will be printed in the console.

## Notes

* Only one command is sent per execution.
* **Do not** use this against unauthorized machines — it may be illegal.
