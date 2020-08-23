# RPM Package Builder

## Use case

This repository contains rpm specs for packages that is not available in centos and a `package` script to lint or build them.

`package` script can lint and build package either natively on centos host or using docker.

## How to use
There is four options:
  - lint
  - lint_in_docker
  - build
  - build_in_docker

For linting or building natively on centos you need to specify one of the two options as ${1} and path to a spec file as ${2}.

`./package lint SPECS/my-spec-file.spec`

`./package build SPECS/my-spec-file.spec`

There is a way to do that inside docker container if you can not build natively on centos.

`./package lint_in_docker SPECS/my-spec-file.spec`

`./package build_in_docker SPECS/my-spec-file.spec`
