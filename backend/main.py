from fastapi import FastAPI
import toml
import uvicorn
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

app = FastAPI()


def serve_features(model_name: str, model_config: file, feature_date: date):
    @app.get(f"/predictions/{model_name}/{date}")
    async def get_predictions():

        return {"model": model_name, "data:" "Model prediction"}
    
def get_features(model_name: str, model_config: file, feature_date: date):
    @app.post(f"/predictions/{model_name}/{date}")
    async def get_predictions():

        return {"model": model_name, "data:" "Model prediction"}
    
def load_config():
    with open("model_configs.yaml", "r") as file:
        config = yaml.safe_load(file)
        for model_name, model_config in config.items():
            get_predictions_route(model_name, model_config)

class ConfigFileChangeHandler(FileSystemEventHandler):
    def on_modification(self, event):
        if event.src_path.endswith("config.yaml"):
            load_config()

observer = Observer()
observer.schedule(ConfigFileChangeHandler(), path='.', recursive=False)
observer.start()

load_config()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)