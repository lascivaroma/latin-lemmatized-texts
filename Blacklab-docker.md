## 1. Index and create a volume blacklab-data

```sh
docker run --rm  --name blacklab-indexer --mount 'type=bind,src=/path/to/blacklab-docker/corpora,dst=/input' \
   --mount 'type=bind,src=/path/to/blacklab-docker/blacklab/formats,dst=/etc/blacklab/formats' --mount 'type=volume,src=blacklab-data,dst=/data' \
   instituutnederlandsetaal/blacklab     /bin/bash -c "cd /usr/local/lib/blacklab-tools && \
   java -cp '*' nl.inl.blacklab.tools.IndexTool create /data/index/latin /input/latin/ tei-msd"
```

## 2. Download the front-end

`git clone https://github.com/INL/corpus-frontend/`

## 3. Change the content of `corpus-frontend/docker-compose.yml`

Search the volumes line of frontend, and change the one using $CORPUS_DIR to `- blacklab-data:/data/index/`

At the end, add

```yml
volumes:
  blacklab-data:
    external: true  # Tell Docker Compose this volume is external and already created
```

## 4. Run

In the corpus-frontend, run `docker compose build` and then `docker compose up -d`
