# build command example:
# DOCKER_BUILDKIT=1 docker build --file I_NEED_A/docker/Dockerfile --output I_NEED_A/docker .

# base image 
FROM ubuntu:focal AS stage_build

# python
RUN apt-get update -y && apt-get install -y \ 
    python3 \
    python3-pip

# copy code base to the image
COPY I_NEED_A/. I_NEED_A

# install packages
RUN pip3 install -r I_NEED_A/docker/requirements.txt

# get statistics
RUN radon mi /I_NEED_A/pacman_solid > /I_NEED_A/docker/radon_mi.txt
RUN radon cc /I_NEED_A/pacman_solid > /I_NEED_A/docker/radon_cc.txt
FROM scratch AS stage_export
COPY --from=stage_build /I_NEED_A/docker/radon_mi.txt .
COPY --from=stage_build /I_NEED_A/docker/radon_cc.txt .

# run the listing of packages
ENTRYPOINT ["pip3", "list"]
