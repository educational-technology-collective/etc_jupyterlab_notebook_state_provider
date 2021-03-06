# ETC JupyterLab Notebook State Provider

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/educational-technology-collective/etc_jupyterlab_notebook_state_provider/main?urlpath=lab)


The ETC JupyterLab Notebook State Provider produces sequential diffs of Notebooks.  Each call to `ETCJupyterLabNotebookStateProvider#getNotebookState` produces a representation of the Notebook where cells that are unchanged since the last call contain just their IDs.  Cells that have not changed since the last call contain their unaltered content.  The diffs can be used in order to reconstruct the Notebook at each point in the sequence.

This strategy allows for the state of the Notebook to captured at many points while reducing the amount of storage and network resources needed in order to store the Notebooks.

## Usage

In the below minimal example, a NotbookPanel is registered with the `ETCJupyterLabNotebookStateProvider`.  The call to `getNotebookState` returns an object that contains a session ID, sequence number, and a serializable representation of the Notebook.  Each subsequent call to `getNotebookState` will return a representation of the Notebook where cells that are unchanged since the last call contain just their IDs.  Cells that have not changed since the last call contain their unaltered content.

```js
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'PLUGIN_ID',
  autoStart: true,
  requires: [
    INotebookTracker,
    IETCJupyterLabNotebookStateProvider
  ],
  activate: (
    app: JupyterFrontEnd,
    notebookTracker: INotebookTracker,
    etcJupyterLabNotebookStateProvider: IETCJupyterLabNotebookStateProvider
  ) => {

    notebookTracker.widgetAdded.connect(async (sender: INotebookTracker, notebookPanel: NotebookPanel) => {

      etcJupyterLabNotebookStateProvider.addNotebookPanel({ notebookPanel });

      let notebookState = etcJupyterLabNotebookStateProvider.getNotebookState({ notebookPanel });

      console.log(notebookState);
    });
  }
};
```

## Requirements

* JupyterLab >= 3.0

## Install

To install the extension, execute:

```bash
pip install etc_jupyterlab_notebook_state_provider
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall etc_jupyterlab_notebook_state_provider
```


## Troubleshoot

If you are seeing the frontend extension, but it is not working, check
that the server extension is enabled:

```bash
jupyter server extension list
```

If the server extension is installed and enabled, but you are not seeing
the frontend extension, check the frontend extension is installed:

```bash
jupyter labextension list
```


## Contributing

### Development install

Note: You will need NodeJS to build the extension package.

The `jlpm` command is JupyterLab's pinned version of
[yarn](https://yarnpkg.com/) that is installed with JupyterLab. You may use
`yarn` or `npm` in lieu of `jlpm` below.

```bash
# Clone the repo to your local environment
# Change directory to the etc_jupyterlab_notebook_state_provider directory
# Install package in development mode
pip install -e .
# Link your development version of the extension with JupyterLab
jupyter labextension develop . --overwrite
# Server extension must be manually installed in develop mode
jupyter server extension enable etc_jupyterlab_notebook_state_provider
# Rebuild extension Typescript source after making changes
jlpm run build
```

You can watch the source directory and run JupyterLab at the same time in different terminals to watch for changes in the extension's source and automatically rebuild the extension.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
jlpm run watch
# Run JupyterLab in another terminal
jupyter lab
```

With the watch command running, every saved change will immediately be built locally and available in your running JupyterLab. Refresh JupyterLab to load the change in your browser (you may need to wait several seconds for the extension to be rebuilt).

By default, the `jlpm run build` command generates the source maps for this extension to make it easier to debug using the browser dev tools. To also generate source maps for the JupyterLab core extensions, you can run the following command:

```bash
jupyter lab build --minimize=False
```

### Development uninstall

```bash
# Server extension must be manually disabled in develop mode
jupyter server extension disable etc_jupyterlab_notebook_state_provider
pip uninstall etc_jupyterlab_notebook_state_provider
```

In development mode, you will also need to remove the symlink created by `jupyter labextension develop`
command. To find its location, you can run `jupyter labextension list` to figure out where the `labextensions`
folder is located. Then you can remove the symlink named `@educational-technology-collective/etc_jupyterlab_notebook_state_provider` within that folder.

### Packaging the extension

See [RELEASE](RELEASE.md)
