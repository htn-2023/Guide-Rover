import cv2
from ultralytics import YOLO
import math
from robomaster import robot
from communication import decision
import asyncio

model = YOLO("./yolov8n.pt")
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush", "hat"
              ]

frame_width = 500
frame_height = 500

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))


def jsonToMovement(movement):
    direction = movement['direction']
    distance = movement['distance']

    if not distance or not direction:
        return 0, 0

    radians = math.radians(movement['direction'])

    x = math.cos(radians) / 10
    y = math.sin(radians) / 10

    return x, y


async def waitOneSecond():
    await asyncio.sleep(1)
    return 0, 0

if __name__ == '__main__':
    class RobotController:
        def __init__(self):
            self.ep_robot = robot.Robot()
            self.ep_robot.initialize(conn_type="ap")
            self.ep_chassis = self.ep_robot.chassis
            self.ep_camera = self.ep_robot.camera
            self.x_val = 0
            self.y_val = 0
            self.prev = None
            self.loop = asyncio.get_event_loop()
            self.go_for_time = 100

        def move(self, json):
            x_val, y_val = jsonToMovement(json)
            self.ep_chassis.drive_speed(x=x_val, y=y_val, z=0, timeout=json['distance']/5)
            self.ep_chassis.drive_speed(x=0, y=0, z=0, timeout=0)

        def camera(self):
            img = self.ep_camera.read_cv2_image()

            results = model(img, stream=True)

            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    print(x1, y1, x2, y2)
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                    conf = math.ceil((box.conf[0] * 100)) / 100
                    cls = int(box.cls[0])
                    class_name = classNames[cls]
                    label = f'{class_name}{conf}'
                    t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                    c2 = x1 + t_size[0], y1 - t_size[1] - 3
                    cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)  # filled
                    cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)
            out.write(img)
            cv2.imshow("Robot", img)
            cv2.waitKey(1)


# Camera code
# def camera():
#     img = ep_camera.read_cv2_image()
#
#     results = model(img, stream=True)
#
#     for r in results:
#         boxes = r.boxes
#         for box in boxes:
#             x1, y1, x2, y2 = box.xyxy[0]
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#             print(x1, y1, x2, y2)
#             cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
#             conf = math.ceil((box.conf[0] * 100)) / 100
#             cls = int(box.cls[0])
#             class_name = classNames[cls]
#             label = f'{class_name}{conf}'
#             t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
#             c2 = x1 + t_size[0], y1 - t_size[1] - 3
#             cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)  # filled
#             cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)
#     out.write(img)
#     cv2.imshow("Robot", img)
#     cv2.waitKey(1)

# Robot movement code
    # ep_robot = robot.Robot()
    # ep_robot.initialize(conn_type="ap")
    #
    # ep_chassis = ep_robot.chassis
    # ep_camera = ep_robot.camera
    #
    # x_val = 0
    # y_val = 0
    # prev = None
    # loop = asyncio.get_event_loop()
    #
    # go_for_time = 100
    #
    # ep_camera.start_video_stream(display=False)
    # for i in range(0, go_for_time):
    #     if i % 3 == 0:
    #         response = decision.response_dict
    #         print(response)
    #         if prev != response:
    #             x_val, y_val = jsonToMovement(response)
    #         else:
    #             x_val, y_val = loop.run_until_complete(waitOneSecond())
    #             loop.close()
    #
    #         if i < go_for_time/2:
    #             ep_chassis.drive_speed(x=x_val, y=x_val, z=0, timeout=2)
    #         else:
    #             ep_chassis.drive_speed(x=-x_val, y=-x_val, z=0, timeout=2)
    #         camera()
    #
    # ep_chassis.drive_speed(x=0, y=0, z=0, timeout=0)
    #
    # for i in range(0, go_for_time*2):
    #     camera()
    #
    # cv2.destroyAllWindows()
    # ep_camera.stop_video_stream()
    #
    # ep_robot.close()
    # out.release()
