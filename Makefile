project = $(shell basename `pwd` | sed 's/-//g')
current_path = $(shell pwd)

all: usage

usage:
	@echo "Tools to create a Flask environment."
	@echo ""
	@echo "When you clone this project, clone into your project name."
	@echo "Because *make will rename all 'skeleton' modules and params with this name."
	@echo "Default is 'flaskskeleton'."
	@echo ""
	@echo "    example: git clone https://github.com/ahmet2mir/flask-skeleton.git myproject"
	@echo "    		    cd myproject"
	@echo "    		    make local"
	@echo ""
	@echo "Allowed targets:"
	@echo ""
	@echo "    usage: this help."
	@echo ""
	@echo "    local: create virtualenv, install requirements and run."
	@echo "        auto-reload: yes."
	@echo "        ctrl+c: stop process."
	@echo "        next make local: start main.py."
	@echo ""
	@echo "    docker: build image and run."
	@echo "        auto-reload: yes."
	@echo "        ctrl+c: remove container."
	@echo "        next make docker: start container."	
	@echo ""
	@echo "    heroku: create, push, scale and run application."
	@echo "        auto-reload: no, need to push content."
	@echo "        ctrl+c: stop log tail but application still running."
	@echo "        next make herok: start web, show info and tail logs."
	@echo ""
	@echo "/!\ .deployed is a state file, if you remove it, the next time "\
		  "you will run make, it will remove your git environment."
	@echo ""

.deployed:
	rm -rf .git
	git init
	mv skeleton ${project}
	find . -type f ! -name Makefile -print0 | xargs -0 sed -i 's/skeleton/${project}/g'
	git add -A
	git commit -m "initial commit"
	touch .deployed

local: .deployed
	@if [ ! -d .venv ] ; \
	then \
		pip install virtualenv ; \
		virtualenv .venv ; \
		.venv/bin/pip install -r requirements.txt ; \
	fi;
	.venv/bin/python main.py

docker: .deployed
	@if [ -z `docker images -q ${project}` ] ; \
	then \
		docker build -t ${project} . ; \
	fi;
	docker run --rm -p 5000:5000 -v ${current_path}:/apps --name ${project} ${project}

heroku: .deployed
	@if [ -z `heroku info` ] ; \
	then \
		heroku create ; \
		git push heroku master ; \
	fi;
	heroku ps:scale web=1 ; \
	heroku info ; \
	heroku logs --tail
