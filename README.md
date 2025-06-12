# Nature Web App

This simple Flask web application lets visitors explore flora and fauna in a self-guided tour. Each entry includes a short description, an image, and an audio clip. You can serve the site from a Docker container and link to individual species pages with QR codes.

## Running locally

1. Build the Docker image:
   ```bash
   docker build -t naturewebapp .
   ```
2. Start the container:
   ```bash
   docker run --rm -p 5000:5000 naturewebapp
   ```
3. Open `http://localhost:5000` in your browser.

## Adding new species

Edit `data/species.json` and add an entry with an `id`, `name`, `description`, `image`, and `audio` filename. You can use a remote URL for `image` or place your own file in the `static/` directory.

Each species page is available at `/species/<id>`—these URLs can be used for QR codes around your conservation area.
