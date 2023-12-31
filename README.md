# Advent of Code 2023
This is my first time participating in the [Advent of Code](https://adventofcode.com/2023). I decided to use Python to go through all the challenges. Because I considered that this was more a educational space rather than a contest, all the solutions that I posted here are versions that I worked on afterwards (so it may be that the code is not the original one).

## How to run the solutions
I used Python 3.11.2 for this contest and Visual Studio Code as the IDE. The solutions are written in a way that they can be launched from the terminal by using the following command:
`python main.py <input file> <part of the challenge> <additional arguments>`

However, I ran the solutions by using a `launch.json` file inside the IDE like this one:
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "cwd": "${fileDirname}",
            "console": "integratedTerminal",
            "args": ["", <input file>, <part of the challenge>, ...],
            "justMyCode": true
        }
    ]
}
```

I also created some tests to verify the output of the examples (not the actual solution). The `settings.json` for Visual Studio Code is the following:
```
{
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./tests",
        "-p",
        "test_*.py"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.unittestEnabled": true
}
```
