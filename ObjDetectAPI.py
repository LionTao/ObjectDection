from opencvdnn import do_object_detection as detect
import os


def obj_dection(path, network="MobileNet"):
    if network == "MobileNet":
        prototxt = "MobileNetSSD_deploy.prototxt.txt"
        model = "MobileNetSSD_deploy.caffemodel"
    else:
        raise Exception("Network not existed")

    if os.path.exists(path) and os.path.isfile(path) and os.path.isfile(prototxt) and os.path.isfile(model):
        return detect(path, prototxt=prototxt, model=model)
    else:
        raise FileExistsError
