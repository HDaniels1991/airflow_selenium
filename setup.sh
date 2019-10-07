# Setup Environment

# 24.09.2019: Successfully tried and tested on Ubuntu 18.04.

# This script installs docker engine with user permissions and docker-compose.

# Install docker engine:
# Uninstall docker
sudo apt-get remove docker docker-engine docker.io containerd runc
# Install using the repository
# 1. Update the apt package index:
sudo apt-get update
# 2. Install packages to allow apt to use a repository over HTTPS:
sudo apt-get install \
	apt-transport-https \
	ca-certificates \
    	curl \
	gnupg-agent \
    	software-properties-common
# 3. Add Docker’s official GPG key:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# 4. Set up the stable repository
sudo add-apt-repository \
	"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
      	$(lsb_release -cs) \
 	stable"
# Install docker engine community:
# 1. Update the apt package index:
sudo apt-get update
# 2. Install the latest version of Docker Engine
sudo apt-get install docker-ce docker-ce-cli containerd.io
# Verify that docker is installed:
sudo docker run hello-world

# Add user to docker group
sudo usermod -aG docker $USER

# Install docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Activate permission changes
#newgrp docker
