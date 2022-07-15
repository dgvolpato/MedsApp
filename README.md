# MedsApp

Records the state of medication taken each day (for our HoloLens project).

## Instructions

### Setup

1. install docker: docs.docker.com/engine/install/ubuntu

2. run:
```
sudo usermod -a -G docker $USER
reboot
```

### Execution

#### run server (docker)

```
bash scripts/docker-build.sh
bash scripts/docker-run.sh
```

#### stop docker containers

```
bash scripts/docker-stop.sh
```

#### clean docker compose volume (clean up database)

```
bash scripts/docker-cleanup.sh
```

#### run server (locally)

```
uvicorn backend.app.main:app --reload
```

#### api test

```
bash scripts/test.sh
```

#### clean daily status

```
bash scripts/test-reset.sh
```

## Links

### frontend access page

http://localhost

### api access page

http://localhost:8008

### api docs page

http://localhost:8008/docs


### open api json definition

http://localhost:8008/openapi.json


