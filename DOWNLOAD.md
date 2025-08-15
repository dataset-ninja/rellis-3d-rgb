Dataset **RELLIS-3D: RGB** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMzA5NF9SRUxMSVMtM0Q6IFJHQi9yZWxsaXMzZC1yZ2ItRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiU3luMkY1QnpPdnJuQU1TTlBydEF1ZlpqVTZjR0crQlNjT2VIYUZrUzQrRT0ifQ==?response-content-disposition=attachment%3B%20filename%3D%22rellis3d-rgb-DatasetNinja.tar%22)

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