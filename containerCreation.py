import docker
client = docker.from_env()
client.containers.run("ryan7971/syscore:ubuntu", \
	stdin_open = True, tty = True, name = "C_NAME",\
	volumes = {"/home/ryan/serverless/apicaching": \
		{'bind': '/root/apicaching', 'mode': 'rw'}})

# volumes 
# 'bind': the path to mount the volume inside the container
# 'mode': Either 'rw' to mount the volume read/write, or 'ro' to mount it read-only
