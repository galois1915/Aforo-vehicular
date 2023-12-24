# AFORO VEHICULAR

Weights version of YOLOv7:
* Small: https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-tiny.pt
* Medium: https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt
* Large: https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6e.pt

We use tiny model modificaing <code> nc: 2  # number of classes</code> in cfg directory
* data
  * FineTuned_YOLO
    * images        # from videos
    * labels        # from CVAT
    * Train         # files "images" and "labels"
    * Val           # files "images" and "labels"
    * Test          # files "images" and "labels"
    * data.yaml     # path of data and config classes nc: 2, names: ["Moto lineal", "Mototaxi"]
  * videos           # videos and annotations
* yolov7
  * ...
  * cfg
    * ...
    * training      # many structures of models depending on the weights used
  * ...
  * runs
    * detect        # output from the test on video and img, detect.py
    * train         # here, there are weights from fine-tuning, train.py
  * ...

Files structure:
|------- data
|           |---- FineTuned_YOLO : data used to tuning YOLO
|           |       |------ images : from videos
|           |       |------ labels : from CVAT
|           |       |------ Train  : files "images" and "labels"
|           |       |------ Val    : files "images" and "labels"
|           |       |------ Test   : files "images" and "labels"
|           |       |------ data.yaml : path of data and config classes <code>nc: 2, names: ["Moto lineal", "Mototaxi"]</code>
|           |---- videos : videos and annotations
|
|------- yolov7
            |---- ...
            |---- cfg
            |       |------  ...
            |       |------ training : many structure of models depending of the weights used
            |---- ...
            |---- runs
            |       |------ detect : output from test on video and img, <code>detect.py</code>
            |       |------ train  : here, there are weights from the fine-tuning, <code>train.py</code>
            |---- ...




https://medium.com/@manuktiwary/coco-format-what-and-how-5c7d22cf5301
https://learnopencv.com/fine-tuning-yolov7-on-custom-dataset/
https://kikaben.com/yolov5-transfer-learning-dogs-cats/#freeze-the-yolov5-backbone 
https://docs.ultralytics.com/yolov5/tutorials/transfer_learning_with_frozen_layers/
https://prakhargurawa.medium.com/creating-a-vehicle-detection-and-classification-ml-pipeline-using-yolo-and-mobilenet-transfer-a15f7b1e8ec9


https://heartbeat.comet.ml/train-your-own-yolov7-object-detection-model-9b21a9e04860
https://docs.ultralytics.com/yolov5/tutorials/transfer_learning_with_frozen_layers/#freeze-all-layers
https://heartbeat.comet.ml/train-your-own-yolov7-object-detection-model-9b21a9e04860

https://medium.com/@prishanga1/yolov7-training-on-custom-data-c6d8ec030e13
