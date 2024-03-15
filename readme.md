|                 | Digital Image Processing              |
| :-------------- | :------------------------------------ |
| **Library**     | OpenCV2                               |
| **Run Program** | Open every single folder to run demo. |

---

|                                        |                                                Directory                                                | Description                                                                                   |
| :------------------------------------- | :-----------------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------------- |
| **Basic**                              |          [DIR](https://github.com/kaytervn/Digital-Image-Processing-Practice/tree/main/co_ban)          | Display images, face and eyes regconition, take camera screenshots.                           |
| **Face Detection**                     |     [DIR](https://github.com/kaytervn/Digital-Image-Processing-Practice/tree/main/dnn_face_detect)      | Face detection with presenting eye, nose, and mouth coordinates.                              |
| **Object Detection**                   |    [DIR](https://github.com/kaytervn/Digital-Image-Processing-Practice/tree/main/dnn_object_detect)     | Import custom datasets, create tkinter GUI, local web service to upload images for detection. |
| **Face Detection with Custom Dataset** | [DIR](https://github.com/kaytervn/Digital-Image-Processing-Practice/tree/main/nhan_dang_khuon_mat_onnx) | Collect image stocks from people to create a dataset for training detection.                  |
| **Negative Image Processing**          |     [DIR](https://github.com/kaytervn/Digital-Image-Processing-Practice/tree/main/xu_ly_anh_am_ban)     | Browse an image to export negative version.                                                   |

<h1>Object Detection</h1>

<h2>Chạy trên CMD:</h2>

**Image Detection:**

```cmd
python object_detection.py --input=image01.jpg --model=yolov8n.onnx --scale=0.00392 --width=640 --height=640 --rgb --postprocessing=yolov8 --classes=object_detection_classes_yolo.txt
```

**Real time Camera:**

```cmd
python object_detection.py --input= --model=yolov8n.onnx --scale=0.00392 --width=640 --height=640 --rgb --postprocessing=yolov8 --classes=object_detection_classes_yolo.txt
```

<h2>Chạy trên VSCode:</h2>

**1.** Tạo file json trong mục Debug: Current File -> Tạo file `launch.json` nằm trong thư mục `.vscode`

**2.** Thêm args, với model và classes tương ứng:

```json
   "args": [
   "--input",
   "image06.jpg",
   "--model",
   "ktr_dataset.onnx",
   "--scale",
   "0.00392",
   "--width",
   "640",
   "--height",
   "640",
   "--rgb",
   "--postprocessing",
   "yolov8",
   "--classes",
   "ktr_dataset.txt"
   ]
```

- Real time Camera:
  - Đổi dòng code trong `object_detection.py`:

```py
cap = cv.VideoCapture(0)
```

**3.** Chọn Run -> Run Without Debugging

<h1>Web Service</h1>

[ <i>Có thể đổi lại model `best.pt`</i> ]

**1.** Chạy CMD và cd tới đường dẫn chứa folder `web_service`:

```cmd
cd D:\..\..\dnn_object_detect\web_service
python object_detector.py
```

**2.** Sau đó, Mở đường dẫn sau trên trình duyệt: `http:///localhost:8080`

<h1>Đánh nhãn hình ảnh</h1>

**1.** Chuẩn hóa hết tệp ảnh thành 640x640 bằng file `chuan_hoa_anh_640x640.py` trong folder `nhan_dang_trai_cay`.

**2.** Tải source code: https://github.com/HumanSignal/labelImg

**3.** Chạy CMD và cd tới folder `labelImg`:

```cmd
cd D:\..\..\labelImg
```

**4.** Sau đó, nhập:

```cmd
pyrcc5 -o libs/resources.py resources.qrc
```

**5.** Cuối cùng, chạy file `labelImg.py` để khởi tạo ứng dụng đánh nhãn (cd tới đường dẫn chứa folder của kho ảnh và file tên các class):

```cmd
python labelImg.py D:\..\..\trai_cay_640x640\sau_rieng D:\..\..\trai_cay.txt
```

<h1>Training YOLOv8</h1>

|                                   | Step-by-step                                                                                                                                                           |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Free Code Camp**                | [LINK](https://www.freecodecamp.org/news/how-to-detect-objects-in-images-using-yolov8/)                                                                                |
| **Roboflow (tác giả của yolov8)** | [LINK](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb#scrollTo=FyRdDYkqAKN4) |

<h2>Train trên Google Colaboratory</h2>

**1.** Upload dataset lên Google Drive.

**2.** Tạo file notebook `.ipynb`.

**3.** Trên thanh menu, Chỉnh sửa -> cài đặt sổ tay -> tích vào `T4 GPU`.

**4.** Thực hiện chạy các lệnh sau:

**Kết nối với Google Drive**

```py
from google.colab import drive
drive.mount('/content/drive')
```

**Chuyển tới thư mục chứa dataset**

```py
%cd '/content/drive/MyDrive/TrainingYOLOv8/trai_cay_yolo8'
```

**Tải thư viện `ultralytics`**

```py
!pip install ultralytics
```

**Import model `yolov8m.pt`**

```py
from ultralytics import YOLO
model = YOLO("yolov8m.pt")
```

**Bắt đầu train với 30 epoch**

```py
model.train(data="data.yaml", epochs=30)
```

**Chuyển hướng tới thư mục chứa model đã train**

```py
%cd '/content/drive/MyDrive/TrainingYOLOv8/trai_cay_yolo8/runs/detect/train2/weights'
```

**Chuyển định dạng thành `.onnx`**

```py
model = YOLO("best.pt")
path = model.export(format="onnx")
```

**5.** Tải file `best.onnx`.
