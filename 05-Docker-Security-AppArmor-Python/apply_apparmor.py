import docker

client = docker.from_env()

IMAGE_NAME = "flask-apparmor"
PROFILE_NAME = "my-apparmor-profile"

try:
    print("Building Docker image...")
    client.images.build(path=".", tag=IMAGE_NAME)

    print("\nStarting container with AppArmor profile...")
    container = client.containers.run(
        IMAGE_NAME,
        ports={"5000/tcp": 5000},
        security_opt=[f"apparmor={PROFILE_NAME}"],
        detach=True,
    )

    print(f"Container started: {container.short_id}")

    info = client.api.inspect_container(container.id)
    print("Configured security options:",
          info["HostConfig"].get("SecurityOpt"))

except docker.errors.DockerException as error:
    print(f"Docker operation failed: {error}")

finally:
    if "container" in locals():
        container.remove(force=True)
        print("Container removed.")