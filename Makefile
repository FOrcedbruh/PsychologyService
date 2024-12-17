build_image: 
	docker build -t ilchpl/psychoimage -f ./dockerfile .

create_container:
	docker run --name PsychologyService -p 7979:7979 ilchpl/psychoimage

stop_container:
	docker stop PsychologyService