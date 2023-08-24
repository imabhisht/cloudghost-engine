docker stop cg-steampipe
docker build -t  cg-steampipe .
docker run -d -p 5550:5550 -p 9193:9193  --rm --name cg-steampipe cg-steampipe