packer {
  required_plugins {
    docker = {
      version = ">= 0.0.7"
      source  = "github.com/hashicorp/docker"
    }
  }
}

source "docker" "ubuntu" {
  image  = "ubuntu:latest"
  commit = true
}

build {
  name    = "learn-packer"
  sources = ["source.docker.ubuntu"]

  provisioner "shell" {
    inline=[
      "apt-get update",
      "apt-get install -y python3",
      "apt-get install -y git",
      "apt-get autoremove -y",
      "apt-get clean -y",
      "rm -rf /var/lib/apt/lists/*"
    ]
  }

  post-processor "docker-tag" {
    repository = "imuser/packer"
    tags = ["latest"]
  }
  post-processor "docker-push" {
    login          = true
    login_username = "imuser"
    login_password = "Ram@123456"
  }
}
