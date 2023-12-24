# AFORO VEHICULAR

Weights version of YOLOv7:
* Small: https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-tiny.pt
* Medium: https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt
* Large: https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6e.pt

We use tiny model modificaing <code> nc: 2  # number of classes</code> in cfg directory

Files structure:
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

Comand to train YOLO:

<code>!python train.py --batch-size 10 --data "../data/FineTuned_YOLO/data.yaml" --img 1080 1920 --weight "./yolov7-tiny.pt" --name yolov7-custom --epoch 10</code>

For more see the last cells of <code>FineTunning-YOLO.ipynb</code>
