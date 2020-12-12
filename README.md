# Introductory Docker 🐋

## Docker

Reference Page: https://docs.docker.com/reference/
Video Tutorial: https://www.youtube.com/watch?v=gAkwW2tuIqE&ab_channel=Fireship
<details>
<summary>What is Docker? What is it used for?</summary><br><b>
Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.
</b></details>

<details>
<summary>How are containers different from virtual machines (VMs)?</summary><br><b>

The primary difference between containers and VMs is that containers allow you to virtualize
multiple workloads on the operating system while in the case of VMs the hardware is being virtualized to
run multiple machines each with its own OS.

* Containers don't require an entire guest operating system as VMs
* It usually takes a few seconds to set up a container as opposed to VMs which can take minutes or at least more time than containers as there is an entire OS to boot and initialize as opposed to container where you mainly lunch the app itself
* Containers are isolated from each other, but not as concretely as virtual machines. It is possible for a malicious user to break into the host OS from a container and vice versa.
</b></details>

<details>
<summary>In which scenarios would you use containers and in which you would prefer to use VMs?</summary><br><b>

You should choose VMs when:
  * you need run an application which requires all the resources and functionalities of an OS
  * you need full isolation and security

You should choose containers when:
  * you need a lightweight solution
  * Running multiple versions or instances of a single application
</b></details>

<details>
<summary>Explain Docker architecture</summary><br><b>
</b></details>

<details>
<summary>Describe in detail what happens when you run `docker run hello-world`?</summary><br><b>

Docker CLI passes your request to Docker daemon.
Docker daemon downloads the image from Docker Hub
Docker daemon creates a new container by using the image it downloaded
Docker daemon redirects output from container to Docker CLI which redirects it to the standard output
</b></details>

<details>
<summary>What are `dockerd, docker-containerd, docker-runc, docker-containerd-ctr, docker-containerd-shim` ?</summary><br><b>

dockerd - The Docker daemon itself. The highest level component in your list and also the only 'Docker' product listed. Provides all the nice UX features of Docker.

(docker-)containerd - Also a daemon, listening on a Unix socket, exposes gRPC endpoints. Handles all the low-level container management tasks, storage, image distribution, network attachment, etc...

(docker-)containerd-ctr - A lightweight CLI to directly communicate with containerd. Think of it as how 'docker' is to 'dockerd'.

(docker-)runc - A lightweight binary for actually running containers. Deals with the low-level interfacing with Linux capabilities like cgroups, namespaces, etc...

(docker-)containerd-shim - After runC actually runs the container, it exits (allowing us to not have any long-running processes responsible for our containers). The shim is the component which sits between containerd and runc to facilitate this.

![alt text](https://i.stack.imgur.com/lAtSR.png "Docker Process")

</b></details>

<details>
<summary>Describe difference between cgroups and namespaces </summary><br><b>
cgroup: Control Groups provide a mechanism for aggregating/partitioning sets of tasks, and all their future children, into hierarchical groups with specialized behaviour.
namespace: wraps a global system resource in an abstraction that makes it appear to the processes within the namespace that they have their own isolated instance of the global resource.

In short:

Cgroups = limits how much you can use;
namespaces = limits what you can see (and therefore use)

Cgroups involve resource metering and limiting:
memory
CPU
block I/O
network

Namespaces provide processes with their own view of the system

Multiple namespaces: pid,net, mnt, uts, ipc, user

</b></details>

<details>
<summary>Describe in detail what happens when you run `docker pull image:tag`?</summary><br><b>
Docker CLI passes your request to Docker daemon. Dockerd Logs shows the process

docker.io/library/busybox:latest resolved to a manifestList object with 9 entries; looking for a unknown/amd64 match

found match for linux/amd64 with media type application/vnd.docker.distribution.manifest.v2+json, digest sha256:400ee2ed939df769d4681023810d2e4fb9479b8401d97003c710d0e20f7c49c6

pulling blob \"sha256:61c5ed1cbdf8e801f3b73d906c61261ad916b2532d6756e7c4fbcacb975299fb Downloaded 61c5ed1cbdf8 to tempfile /var/lib/docker/tmp/GetImageBlob909736690

Applying tar in /var/lib/docker/overlay2/507df36fe373108f19df4b22a07d10de7800f33c9613acb139827ba2645444f7/diff" storage-driver=overlay2

Applied tar sha256:514c3a3e64d4ebf15f482c9e8909d130bcd53bcc452f0225b0a04744de7b8c43 to 507df36fe373108f19df4b22a07d10de7800f33c9613acb139827ba2645444f7, size: 1223534

</b></details>


<details>
<summary>How do you run a container?</summary><br><b>
	
docker run
</b></details>

<details>
<summary>What `docker commit` does?. When will you use it?</summary><br><b>
	
Create a new image from a container’s changes
</b></details>

<details>
<summary>How would you transfer data from one container into another?</summary><br><b>
</b></details>

<details>
<summary>What happens to data of the container when a container exists?</summary><br><b>
</b></details>

<details>
<summary>Explain what each of the following commands do:

  * docker run
  * docker rm
  * docker ps
  * docker pull
  * docker build
  * docker commit</summary><br><b>
</b></details>

<details>
<summary>How do you remove old, non running, containers?</summary><br><b>
	
1. To remove one or more Docker images use the docker container rm command followed by the ID of the containers you want to remove.
2. The docker system prune command will remove all stopped containers, all dangling images, and all unused networks
3. docker rm $(docker ps -a -q) - This command will delete all stopped containers. The command docker ps -a -q will return all existing container IDs and pass them to the rm command which will delete them. Any running containers will not be deleted.
</b></details>

##### Dockerfile

<details>
<summary>What is Dockerfile</summary><br><b>
	
Docker can build images automatically by reading the instructions from a Dockerfile. A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.
</b></details>

<details>
<summary>What is the difference between ADD and COPY in Dockerfile?</summary><br><b>
	
COPY takes in a src and destination. It only lets you copy in a local file or directory from your host (the machine building the Docker image) into the Docker image itself.
ADD lets you do that too, but it also supports 2 other sources. First, you can use a URL instead of a local file / directory. Secondly, you can extract a tar file from the source directly into the destination.
Although ADD and COPY are functionally similar, generally speaking, COPY is preferred. That’s because it’s more transparent than ADD. COPY only supports the basic copying of local files into the container, while ADD has some features (like local-only tar extraction and remote URL support) that are not immediately obvious.
</b></details>

<details>
<summary>What is the difference between CMD and RUN in Dockerfile?</summary><br><b>
	
RUN lets you execute commands inside of your Docker image. These commands get executed once at build time and get written into your Docker image as a new layer.
CMD is the command the container executes by default when you launch the built image. A Dockerfile can only have one CMD.
You could say that CMD is a Docker run-time operation, meaning it’s not something that gets executed at build time. It happens when you run an image. A running image is called a container.
</b></details>

<details>
<summary>Do you perform any checks or testing related to your Dockerfile?</summary><br><b>

A common answer to this is to use [hadolint](https://github.com/hadolint/hadolint) project which is a linter based on Dockerfile best practices.
</b></details>

<details>
<summary>Explain what is Docker compose and what is it used for</summary><br><b>
	
Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

For example, you can use it to set up ELK stack where the services are: elasticsearch, logstash and kibana. Each running in its own container.
</b></details>

<details>
<summary>Describe the process of using Docker Compose</summary><br><br>

* Define the services you would like to run together in a docker-compose.yml file
* Run `docker-compose up` to run the services
</b></details>

<details>
<summary>Explain Docker interlock</summary><br><b>
</b></details>

<details>
<summary>Where can you store Docker images?</summary><br><b>
</b></details>

<details>
<summary>What is Docker Hub?</summary><br><b>
	
DockerHub is the storage for Docker image repositories (public and private)
https://hub.docker.com/ (CRUD Containers)
</b></details>

<details>
<summary>What is the difference between Docker Hub and Docker cloud?</summary><br><b>

Docker Hub is a native Docker registry service which allows you to run pull
and push commands to install and deploy Docker images from the Docker Hub.

Docker Cloud is built on top of the Docker Hub so Docker Cloud provides
you with more options/features compared to Docker Hub. One example is
Swarm management which means you can create new swarms in Docker Cloud.
</b></details>

<details>
<summary>What is Docker Repository?</summary><br><b>
</b></details>

<details>
<summary>Explain image layers</summary><br><b>
	
A Docker image is built up from a series of layers. Each layer represents an instruction in the image’s Dockerfile. Each layer except the very last one is read-only.
Each layer is only a set of differences from the layer before it. The layers are stacked on top of each other. When you create a new container, you add a new writable layer on top of the underlying layers. This layer is often called the “container layer”. All changes made to the running container, such as writing new files, modifying existing files, and deleting files, are written to this thin writable container layer. 
The major difference between a container and an image is the top writable layer. All writes to the container that add new or modify existing data are stored in this writable layer. When the container is deleted, the writable layer is also deleted. The underlying image remains unchanged.
Because each container has its own writable container layer, and all changes are stored in this container layer, multiple containers can share access to the same underlying image and yet have their own data state.
</b></details>

<details>
<summary>What best practices are you familiar related to working with containers?</summary><br><b>
</b></details>

<details>
<summary>How do you manage persistent storage in Docker?</summary><br><b>
</b></details>

<details>
<summary>How can you connect from the inside of your container to the localhost of your host, where the container runs?</summary><br><b>
</b></details>

<details>
<summary>How do you copy files from Docker container to the host and vice versa?</summary><br><b>
</b></details>

-Jenkins: https://www.jenkins.io/doc/book/installing/docker/
