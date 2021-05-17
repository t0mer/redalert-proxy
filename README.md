# Red Alert Docker
__________________________________________

Ubuntu based image running python and flask application that proxys Oref API.
The Application has 2 endpoints:
* /alerts - Returns current alert
* /history - Returns alerts hitory

## Base Image
`From ubuntu:18.04` described [here](https://hub.docker.com/_/ubuntu).

## Image configuration
### Enviroment variables
- *LANGUAGE*</br>
Set the language for alert history only (he,en,ru,ar), Default is he (Hebrew).
- *REGION*</br>
used for setting the region for monitoring. default is * (any)

## Usage

#### docker-compose from hub
```yaml
version: "3.6"
services:
  redalert-proxy:
    image: techblog/redalert-proxy
    container_name: redalert_proxy
    restart: always
    environment:
      - LANGUAGE=[Alerts History Language]
      - REGION=[* for any or region name)
    ports:
      - "8080:8080"
```

