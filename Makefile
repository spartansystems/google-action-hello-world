NAME = "spartan/google-home"


.PHONY:	all build shell

run = docker run --rm -it \
		-v `pwd`:/code \
		--env-file .env \
		$(NAME) $1

all : build

build :
	docker build -t $(NAME) .

shell :
	$(call run,bash,$(ENV))
