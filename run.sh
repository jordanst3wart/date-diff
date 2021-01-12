
docker_cli(){
  echo "TODO"
}


install_dependencies(){
  pip3 install requirements.txt
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