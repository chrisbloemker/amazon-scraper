# Amazon Price Scraper

A python based web scraper targeting Amazon.com items.

## Running

### Docker CLI

For now, a local build is required to run. As the remaining tasks get built out, the image will be pushed to DockerHub.

**Build:**
```shell
docker build -t amazon_scraper .
```

**Run:**
```shell
docker run --rm -it --net="host" --name amazon_scraper
```

### Docker Compose

Not yet implemented

## Remaining Tasks:

- Make the email use the URL variable instead of hardcoded text
- Use environment variables for the email credentials
- Cleaner way to extract the price into a float from a string. (Limitations right now are digit length of price
- Replace email route with a slack webhook.
- Have program exit when an email has been set to avoid email storm
- Figure out how to input more than 1 price check item
- Convert into web app using bottle/flask

## Completed Tasks:

- ~~Build into docker image~~