#!/bin/sh
# some useful shell functions
# run like: ./run.sh $function

docker_build_cli(){
  docker build . --tag date-diff:latest
}

# requires build first
cli(){
  docker run date-diff:latest "$@"
}

# no dependencies (maybe argparse)
install_dependencies(){
  pip3 install requirements.txt
}

generate_dependencies(){
  pip3 freeze > requirements.txt
}


format(){
  # use black to format python code
  # pip3 install git+git://github.com/psf/black
  black .
}

test(){
  python3 -m unittest discover tests
}


"$@"