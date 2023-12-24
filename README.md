https://medium.com/@manuktiwary/coco-format-what-and-how-5c7d22cf5301
https://learnopencv.com/fine-tuning-yolov7-on-custom-dataset/
https://kikaben.com/yolov5-transfer-learning-dogs-cats/#freeze-the-yolov5-backbone 
https://docs.ultralytics.com/yolov5/tutorials/transfer_learning_with_frozen_layers/
https://prakhargurawa.medium.com/creating-a-vehicle-detection-and-classification-ml-pipeline-using-yolo-and-mobilenet-transfer-a15f7b1e8ec9


https://heartbeat.comet.ml/train-your-own-yolov7-object-detection-model-9b21a9e04860
https://docs.ultralytics.com/yolov5/tutorials/transfer_learning_with_frozen_layers/#freeze-all-layers
https://heartbeat.comet.ml/train-your-own-yolov7-object-detection-model-9b21a9e04860

https://medium.com/@prishanga1/yolov7-training-on-custom-data-c6d8ec030e13

Weights version of YOLOv7:
* Small: https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-tiny.pt
* Medium: https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt
* Large: https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6e.pt

Files:
|------- data
|           |---- FineTuned_YOLO : data used to tuning YOLO
|           |       |------ images : from videos
|           |       |------ labels : from CVAT
|           |       |------ Train
|           |       |------ Val
|           |       |------ Test
|           |---- videos : videos and annotations
|
|------- yolov7