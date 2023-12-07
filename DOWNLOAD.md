Dataset **RELLIS-3D: RGB** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/o/d/ju/B0BUs76Ue35eaw951pRaLeGb25vg2zengvQVbyuY2OzUnxdY3Lipx0q8OlWvGC70bOPuy2X5wf60cDbLKXJlN7NttLOEy3O945gJ9lS49RoI2LfgQUjFfM7MQFHV.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='RELLIS-3D: RGB', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://drive.google.com/drive/folders/1aZ1tJ3YYcWuL3oWKnrTIC5gq46zx1bMc).