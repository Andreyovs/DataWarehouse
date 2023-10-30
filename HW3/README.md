(base) dev@cd-dev-001:~/Documents/Otus/DataWarehouse$ terraform -v
    Terraform v1.6.2-dev
    on linux_amd64

(base) dev@cd-dev-001:~/Documents/Otus/DataWarehouse$ dbt --version
    Core:
    - installed: 1.6.6
    - latest:    1.6.6 - Up to date!

    Plugins:
    - snowflake: 1.6.4 - Up to date!
    - trino:     1.6.2 - Up to date!
    - redshift:  1.6.2 - Up to date!
    - bigquery:  1.6.7 - Up to date!
    - postgres:  1.6.6 - Up to date!


(base) dev@cd-dev-001:~/Documents/Otus/DataWarehouse$ yc --version
            Yandex Cloud CLI 0.112.0 linux/amd64

(base) dev@cd-dev-001:~/Documents/Otus/airbyte_lab/airbyte_lab$ devcontainer build . --workspace-folder .
        [7 ms] @devcontainers/cli 0.52.1. Node.js v20.9.0. linux 6.2.0-35-generic x64.
        [5211 ms] Resolving Feature dependencies for 'ghcr.io/devcontainers/features/common-utils:2'...
        [11716 ms] Resolving Feature dependencies for 'ghcr.io/stuartleeks/dev-container-features/shell-history:0'...
        [15339 ms] Soft-dependency 'ghcr.io/meaningful-ooo/devcontainer-features/fish' is not required.  Removing from installation order...
        [16885 ms] Start: Run: docker buildx build --load --build-arg BUILDKIT_INLINE_CACHE=1 -f /tmp/devcontainercli-dev/container-features/0.52.1-1698600595867/Dockerfile-with-features -t vsc-airbyte_lab-639819ab18fcc5f584402ba820d734f118a965ef78e5fcb4adae932448bd9af9 --target dev_containers_target_stage --build-context dev_containers_feature_content_source=/tmp/devcontainercli-dev/container-features/0.52.1-1698600595867 --build-arg _DEV_CONTAINERS_BASE_IMAGE=dev_container_auto_added_stage_label --build-arg _DEV_CONTAINERS_IMAGE_USER=root --build-arg _DEV_CONTAINERS_FEATURE_CONTENT_SOURCE=dev_container_feature_content_temp /home/dev/Documents/Otus/airbyte_lab/airbyte_lab
        [+] Building 149.1s (21/21) FINISHED                            docker:desktop-linux
        => [internal] load .dockerignore                                               0.1s
        => => transferring context: 2B                                                 0.0s
        => [internal] load build definition from Dockerfile-with-features              0.1s
        => => transferring dockerfile: 3.58kB                                          0.0s
        => resolve image config for docker.io/docker/dockerfile:1.4                    3.0s
        => docker-image://docker.io/docker/dockerfile:1.4@sha256:9ba7531bd80fb0a85863  1.4s
        => => resolve docker.io/docker/dockerfile:1.4@sha256:9ba7531bd80fb0a858632727  0.0s
        => => sha256:9ba7531bd80fb0a858632727cf7a112fbfd19b17e94c4e84 2.00kB / 2.00kB  0.0s
        => => sha256:ad87fb03593d1b71f9a1cfc1406c4aafcb253b1dabebf569768d 528B / 528B  0.0s
        => => sha256:1e8a16826fd1c80a63fa6817a9c7284c94e40cded14a9b0d 2.37kB / 2.37kB  0.0s
        => => sha256:1328b32c40fca9bcf9d70d8eccb72eb873d1124d72dadce0 9.94MB / 9.94MB  1.2s
        => => extracting sha256:1328b32c40fca9bcf9d70d8eccb72eb873d1124d72dadce04db8b  0.1s
        => [context dev_containers_feature_content_source] load .dockerignore          0.0s
        => => transferring dev_containers_feature_content_source: 2B                   0.0s
        => [internal] load metadata for docker.io/fishtownanalytics/dbt:1.0.0          1.6s
        => [context dev_containers_feature_content_source] load from client            0.1s
        => => transferring dev_containers_feature_content_source: 69.11kB              0.0s
        => [dev_container_auto_added_stage_label 1/5] FROM docker.io/fishtownanalyti  24.4s
        => => resolve docker.io/fishtownanalytics/dbt:1.0.0@sha256:4c9462867d2db6869a  0.0s
        => => sha256:4c9462867d2db6869a048ba429d3557a562ac20337d4ce25 3.06kB / 3.06kB  0.0s
        => => sha256:e5ae68f740265288a4888db98d2999a638fdcb6d725f4 31.37MB / 31.37MB  14.5s
        => => sha256:d4a99467e40c5f7df417e80af41be8672d48682d2d6c4443 1.08MB / 1.08MB  0.4s
        => => sha256:b8216313f4d89e1fe394bb2c37bd59eeea39e50b50eda1 11.01MB / 11.01MB  1.6s
        => => sha256:d874bacd7d192afda4a6de4f328b270428403d9a048a7b 11.45kB / 11.45kB  0.0s
        => => sha256:f88fae61fe7c594c2a84341972e25a0c57e12352751f2f48a38c 232B / 232B  1.4s
        => => sha256:cb549977f6eba802dc63731bb599b12af52b677801aa0cd6 2.64MB / 2.64MB  2.5s
        => => sha256:d86dbea59b9636193dc39815d13173ef8cdf4ab53e4 113.95MB / 113.95MB  17.4s
        => => sha256:3db15e53f615bf1f2fb54706bf8fd24dda62bab264621423 5.76MB / 5.76MB  5.2s
        => => sha256:5e8fa73257597bce7aae3b6308355a60e8a252870413395da63e 159B / 159B  5.4s
        => => sha256:a4fbe57de8cab5b3e1e71060d5daa498ca7fb68992a79 23.95MB / 23.95MB  16.7s
        => => extracting sha256:e5ae68f740265288a4888db98d2999a638fdcb6d725f427678814  1.1s
        => => sha256:0818d148a5a69e7a3da9dc2d59482347a25a826531094a1 8.82MB / 8.82MB  17.9s
        => => extracting sha256:d4a99467e40c5f7df417e80af41be8672d48682d2d6c444365f6f  0.1s
        => => extracting sha256:b8216313f4d89e1fe394bb2c37bd59eeea39e50b50eda11e9699e  0.4s
        => => extracting sha256:f88fae61fe7c594c2a84341972e25a0c57e12352751f2f48a38c3  0.0s
        => => extracting sha256:cb549977f6eba802dc63731bb599b12af52b677801aa0cd6e6568  0.1s
        => => sha256:7ba9308eae23d962907576170521958fcd847682d262ae4 7.26MB / 7.26MB  18.4s
        => => sha256:d82924b87c6e7cad9f8716bc155c6e048485cd091e1a2 21.98MB / 21.98MB  20.2s
        => => extracting sha256:d86dbea59b9636193dc39815d13173ef8cdf4ab53e4e1938acb48  2.9s
        => => sha256:6f83952feddf57f234a8d001e6ce983a3939c90a83c888e 9.04kB / 9.04kB  18.2s
        => => extracting sha256:3db15e53f615bf1f2fb54706bf8fd24dda62bab26462142350285  0.3s
        => => extracting sha256:5e8fa73257597bce7aae3b6308355a60e8a252870413395da63e8  0.0s
        => => extracting sha256:a4fbe57de8cab5b3e1e71060d5daa498ca7fb68992a79cd851cef  1.1s
        => => extracting sha256:0818d148a5a69e7a3da9dc2d59482347a25a826531094a14c3039  0.6s
        => => extracting sha256:7ba9308eae23d962907576170521958fcd847682d262ae41bbfc0  0.3s
        => => extracting sha256:d82924b87c6e7cad9f8716bc155c6e048485cd091e1a2dfd77d1f  0.8s
        => => extracting sha256:6f83952feddf57f234a8d001e6ce983a3939c90a83c888e97dd27  0.0s
        => [dev_container_auto_added_stage_label 2/5] RUN apt -y update     && apt -  48.8s
        => [dev_container_auto_added_stage_label 3/5] RUN set -ex     && python -m p  19.4s
        => [dev_container_auto_added_stage_label 4/5] RUN curl https://storage.yande  12.3s
        => [dev_container_auto_added_stage_label 5/5] RUN curl -sL https://hashicorp-  4.8s
        => [dev_containers_feature_content_normalize 1/2] COPY --from=dev_containers_  0.1s
        => [dev_containers_target_stage 1/5] RUN mkdir -p /tmp/dev-container-features  0.4s
        => [dev_containers_feature_content_normalize 2/2] RUN chmod -R 0755 /tmp/buil  0.4s
        => [dev_containers_target_stage 2/5] COPY --from=dev_containers_feature_conte  0.1s
        => [dev_containers_target_stage 3/5] RUN echo "_CONTAINER_USER_HOME=$( (comma  0.2s
        => [dev_containers_target_stage 4/5] RUN --mount=type=bind,from=dev_containe  30.9s
        => [dev_containers_target_stage 5/5] RUN --mount=type=bind,from=dev_container  0.4s
        => preparing layers for inline cache                                           1.0s
        => exporting to image                                                          0.0s
        => => exporting layers                                                         0.0s
        => => writing image sha256:4b2da67343259708cf0046dba27b7c91bffaad22cc4f32c036  0.0s
        => => naming to docker.io/library/vsc-airbyte_lab-639819ab18fcc5f584402ba820d  0.0s
        {"outcome":"success","imageName":["vsc-airbyte_lab-639819ab18fcc5f584402ba820d734f118a965ef78e5fcb4adae932448bd9af9"]}


(base) dev@cd-dev-001:~/Documents/Otus/airbyte_lab/airbyte_lab$ terraform init

        Initializing the backend...

        Initializing provider plugins...
        - Finding latest version of yandex-cloud/yandex...
        - Installing yandex-cloud/yandex v0.100.0...
        - Installed yandex-cloud/yandex v0.100.0 (unauthenticated)

        Terraform has created a lock file .terraform.lock.hcl to record the provider
        selections it made above. Include this file in your version control repository
        so that Terraform can guarantee to make the same selections by default when
        you run "terraform init" in the future.

        ╷
        │ Warning: Incomplete lock file information for providers
        │ 
        │ Due to your customized provider installation methods, Terraform was forced to calculate lock file checksums locally for the following providers:
        │   - yandex-cloud/yandex
        │ 
        │ The current .terraform.lock.hcl file only includes checksums for linux_amd64, so Terraform running on another platform will fail to install these providers.
        │ 
        │ To calculate additional checksums for another platform, run:
        │   terraform providers lock -platform=linux_amd64
        │ (where linux_amd64 is the platform to generate)
        ╵

        Terraform has been successfully initialized!

        You may now begin working with Terraform. Try running "terraform plan" to see
        any changes that are required for your infrastructure. All Terraform commands
        should now work.

        If you ever set or change modules or backend configuration for Terraform,
        rerun this command to reinitialize your working directory. If you forget, other
        commands will detect it and remind you to do so if necessary.

(base) dev@cd-dev-001:~/Documents/Otus/airbyte_lab/airbyte_lab$ terraform validate
S       uccess! The configuration is valid.


(base) dev@cd-dev-001:~/Documents/Otus/airbyte_lab/airbyte_lab$ terraform plan


(base) dev@cd-dev-001:~/Documents/Otus/airbyte_lab/airbyte_lab$ terraform apply


        Apply complete! Resources: 8 added, 0 changed, 0 destroyed. 

        Outputs: