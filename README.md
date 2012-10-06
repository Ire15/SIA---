Proyecto-SIA
============

Proyecto programado de SIA


Para correr el webservice:

	sudo apt-get install mysql-server
	sudo apt-get install python-pip
	sudo apt-get install python-setuptools
	sudo apt-get install python-docutils
	ladon2.7ctl testserve -p 8080 testservice.py

Para correr el cliente:

	sudo apt-get install build-essential libgtk-3-dev
	sudo apt-get install glade
	sh ./Cliente.sh

Para correr la consola de mysql:
	
	mysql -u root -p