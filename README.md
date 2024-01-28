# Rivian LogScale
Rivian Telemetry to Crowdstrike's LogScale

<img src="https://github.com/sween/rivian-logscale/raw/main/assets/rivian-logscale.png" alt="Aspiring Brick Builder">

Create a namespace and add your Rivian Credentials as a secret:

```
kubectl create ns rivian
kubectl create secret generic rivian-user-pass -n rivian \
    --from-literal=rivian_username='ron.sweeney+api@hotmale.com' \
    --from-literal=rivian_password='12345' # same as your luggage

kubectl create secret generic cs-logscale-creds -n rivian \
    --from-literal=apikey='xyz.....'
```

Apply the Deployment

```
kubectl apply -f deploy/deployment.yaml -n rivian
```

More Documentation and Errata over @ [Deez Watts - A Rivian Data Adventure](https://www.deezwatts.com)

## Props
The Mace [the-mace/rivian-python-api](https://github.com/the-mace/rivian-python-api)  

kaedenbrinkman [kaedenbrinkman/rivian-api](https://github.com/kaedenbrinkman/rivian-api)  


## Author
Ron Sweeney [sween](https://www.github.com/sween)

