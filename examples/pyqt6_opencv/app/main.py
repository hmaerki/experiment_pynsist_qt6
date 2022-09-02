import sys
import pathlib

from PySide6.QtCore import Slot
from PySide6.QtCore import QFile
from PySide6.QtGui import QImage
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

from .camera import CameraDevice

DIRECTORY_OF_THIS_FILE = pathlib.Path(__file__).parent.absolute()

def main():
    app = QApplication(sys.argv)

    loader = QUiLoader()
    file = QFile(DIRECTORY_OF_THIS_FILE / 'mainwindow.ui')
    file.open(QFile.ReadOnly)
    ui = loader.load(file)
    file.close()

    @Slot(QImage)
    def update_video_label(image):
        pixmap = QPixmap.fromImage(image)
        ui.video.setPixmap(pixmap)
        ui.video.update()

    try:
        camera = CameraDevice()
    except ValueError:
        ui.video.setText("Device not found!\n\nIs FFMPEG available?")
    else:
        camera.frame_ready.connect(update_video_label)
        ui.video.setMinimumSize(*camera.size)

    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
