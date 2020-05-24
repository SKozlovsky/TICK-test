## TICK test
The dummy project to test TICK stack.
InfluxDb, Grafana, Telegram with a plugin to collect Docker metrics, and custom python app will be started in Docker.

* InfluxDb is used to store all needed data and metrics
* Telegraf collects docker metrics and push it to InfluxDb
* Grafana is used as monitoring frontend
* App - dummy python web-server, used as a monitoring target

The App container could be restarted by REST API.
And the main goal of the project - to be able to monitor from Grafana every time service goes down by triggering `api/down`


#### Grafana monitoring [http://127.0.0.1:3000] 
It doesn't require authorisation and anonymous users can see `TICK-test docker metrics` dashboard.

The main dashboard widget - `" Just started containers"`.
If all containers are started and work as expected, the widget Normal state will `No data`.
After triggering `api/down` and app container restarting the status will be changed and show the number of just started containers

### Requirements
* docker and docker-compose installed
* 8000 and 3000 ports are available

### Usage:

* `docker-compose up --build -d` or `make start` to start all containers
* wait some time while containers are starting and provisioning
* `http://127.0.0.1:3000` in web browser to monitor Docker metrics from Grafana
* `curl http://127.0.0.1:5000/api/down` (or use web browser) - to restart App container 