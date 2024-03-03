docker build -t rivian-logscale .
docker image tag rivian-logscale sween/rivian-logscale:latest
docker push sween/rivian-logscale:latest