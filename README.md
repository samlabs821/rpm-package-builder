# RPM Package Builder

## Use case

This repository contains rpm specs for packages that is not available in centos and a `package` script to build.

`package` script can build package either natively on centos host or build using docker.

## How to use
There is two options:
  - build
  - build_in_docker

For building natively on centos you need to specify one of the two options as ${1} and path to a spec file as ${2}.

`./package build SPECS/my-spec-file.spec`

There is a way to do that inside docker container if you can not build natively on centos.

`./package build_in_docker SPECS/my-spec-file.spec`
