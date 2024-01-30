# Rivian LogScale
Rivian Telemetry to Crowdstrike's LogScale

<img src="https://github.com/sween/rivian-logscale/raw/main/assets/rivian-logscale.png" alt="Aspiring Brick Builder">

Documentation:
[LogScale](https://library.humio.com/integrations/api-ingest.html)

Build:

```
docker build -t rivian-logscale .
docker image tag rivian-logscale sween/rivian-logscale:latest
docker push sween/rivian-logscale:latest
```

Create a namespace and add your Rivian Credentials, LogScale apikey as a secret:

```
kubectl create ns rivian
kubectl create secret generic rivian-user-pass -n rivian \
    --from-literal=rivian_username='ron.sweeney+api@hotmale.com' \
    --from-literal=rivian_password='12345' # same as your luggage

kubectl create secret generic cs-logscale-creds -n rivian \
    --from-literal=apikey='xyz.....'
```

Apply as a Deployment

```
kubectl apply -f deploy/cronjob.yaml -n rivian
```

Apply as a Deployment

```
kubectl apply -f deploy/deployment.yaml -n rivian
```

More Documentation and Errata over @ [Deez Watts - A Rivian Data Adventure](https://www.deezwatts.com)

## Props
The Mace [the-mace/rivian-python-api](https://github.com/the-mace/rivian-python-api)  

kaedenbrinkman [kaedenbrinkman/rivian-api](https://github.com/kaedenbrinkman/rivian-api)  


## Author
Ron Sweeney [sween](https://www.github.com/sween)

