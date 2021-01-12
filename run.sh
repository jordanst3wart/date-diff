
docker_cli(){
  echo "TODO"
}


install_dependencies(){
  pip install requirements.txt
}


format(){
  pip install git+git://github.com/psf/black
  black .
}

test(){
  python3 -m unittest discover tests
}


"$@"