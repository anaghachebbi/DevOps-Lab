# Exercise 8: Hello World Jenkins Job

## Objective

Create and execute a Freestyle Jenkins job that retrieves a shell script from GitHub and prints a message.

## Tools Used

- Jenkins
- Docker
- Git
- GitHub
- Bash

## Implementation

1. Created a public GitHub repository named `devops-sample-code`.
2. Added `hello-world.sh` containing a Hello World message.
3. Pushed the script to GitHub.
4. Configured a Freestyle Jenkins job named `HelloWorld`.
5. Configured Git source control to retrieve the repository.
6. Added the build command `sh hello-world.sh`.
7. Executed the job successfully.

## Output

```text
Hello, Jenkins!
Finished: SUCCESS
```

## Screenshots

See the `screenshots` folder for evidence of the GitHub repository, Git commit, Jenkins configuration, and successful build.
