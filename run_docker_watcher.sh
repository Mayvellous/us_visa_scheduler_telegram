docker build -t shch_usvs2 --network=host .
docker run -it --rm --net=host --name shch_sdc_usvs_wself2 -v "$PWD":/app -w /app shch_usvs2 python visa_no_payment.py --config config_watcher_israel.yaml
