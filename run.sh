
docker_cli(){

}


install_dependencies(){
  pip install requirements.txt
}


format(){
  pip install git+git://github.com/psf/black
  black .
}

test(){
  # TODO
}


@