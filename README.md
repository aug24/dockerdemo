# dockerdemo

Trivial little docker project

# Starting

To start, install docker, check out this repo and issue the following command at the repo root:

```
docker build . > build.log
build_id=$(tail -1 build.log | awk '{print $NF}')
docker run -d -p 127.0.0.1:5000:5000 $build_id
```

You can now access the trivial little python project at

```
curl -is localhost:5000
```
