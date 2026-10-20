# azure-web-app

## Run locally

Install the locked dependencies and start the Flask app:

```sh
uv sync
uv run launch-app
```

Then open `http://127.0.0.1:5000`. The home page is at `/`, and the Meme Time
Capsule page is at `/memes`.

## Azure App Service

The GitHub Actions deployment workflow deploys the repository root. Azure's
Oryx build reads `requirements.txt`; regenerate it after dependency changes with:

```sh
uv export --format requirements.txt --output-file requirements.txt
```

Set the App Service startup command to:

```sh
gunicorn --bind=0.0.0.0 --timeout 600 --chdir src "azure_web_app.app:create_app()"
```