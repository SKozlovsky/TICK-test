SH := /bin/bash -c

start:
	$(SH) "docker-compose up --build -d"

stop:
	$(SH) "docker-compose down"

logs:
	$(SH) "docker-compose logs -f"

destroy: stop
	$(SH) "docker volume rm test-singapoore_grafana-ds && docker volume rm test-singapoore_db-data "