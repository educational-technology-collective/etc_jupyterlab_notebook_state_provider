from ._version import __version__
from .application import ETCJupyterLabNotebookStateProviderApp
import json
from pathlib import Path

HERE = Path(__file__).parent.resolve()

with (HERE / "labextension" / "package.json").open() as fid:
    data = json.load(fid)

def _jupyter_labextension_paths():
    return [{
        "src": "labextension",
        "dest": data["name"]
    }]

def _jupyter_server_extension_points():
    return [{
        "module": "etc_jupyterlab_notebook_state_provider",
        "app": ETCJupyterLabNotebookStateProviderApp
    }]

load_jupyter_server_extension = ETCJupyterLabNotebookStateProviderApp.load_classic_server_extension
