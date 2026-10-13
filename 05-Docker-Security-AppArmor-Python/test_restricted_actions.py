import docker

client = docker.from_env()
container = None

try:
    container = client.containers.run(
        "flask-apparmor",
        ports={"5000/tcp": 5000},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True,
    )

    print(f"Container started: {container.short_id}")

    tests = [
        ("Read /etc/passwd", ["cat", "/etc/passwd"]),
        ("Execute /bin/bash", ["/bin/bash", "-c", "echo executed"]),
    ]

    for description, command in tests:
        result = container.exec_run(command)
        print(f"\n{description}")
        print(f"Exit code: {result.exit_code}")
        print(result.output.decode(errors="replace"))

except docker.errors.DockerException as error:
    print(f"Docker operation failed: {error}")

finally:
    if container is not None:
        container.remove(force=True)
        print("\nContainer removed.")