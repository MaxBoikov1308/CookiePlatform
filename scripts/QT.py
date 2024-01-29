from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QPushButton, QVBoxLayout, QWidget, QInputDialog, QComboBox
from PyQt5.QtCore import Qt, QThreadPool, QRunnable, QObject, pyqtSignal
import sys
import peewee
import json

db = peewee.SqliteDatabase('maps.db')

class Map(peewee.Model):
    name = peewee.CharField()
    data = peewee.BlobField()

    class Meta:
        database = db

class DraggableRectItem(QGraphicsRectItem):
    def __init__(self, x, y, width, height, cell_size):
        super().__init__(x, y, width, height)
        self.setFlag(QGraphicsRectItem.ItemIsMovable)
        self.cell_size = cell_size
        self.snap_to_grid()

    def snap_to_grid(self):
        x = round(self.x() / self.cell_size) * self.cell_size
        y = round(self.y() / self.cell_size) * self.cell_size
        self.setPos(x, y)

class WorkerSignals(QObject):
    finished = pyqtSignal()

class Worker(QRunnable):
    def __init__(self, func, *args):
        super(Worker, self).__init__()
        self.func = func
        self.args = args
        self.signals = WorkerSignals()

    def run(self):
        self.func(*self.args)
        self.signals.finished.emit()

class MapEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)

        self.cell_size = 50  # Размер клетки
        self.grid_width = 10  # Количество клеток по горизонтали
        self.grid_height = 10  # Количество клеток по вертикали

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.view)

        self.init_ui()

    def init_ui(self):
        self.btnAddBlock = QPushButton('Add Block', self)
        self.btnAddBlock.clicked.connect(self.add_block)

        self.btnAddSpike = QPushButton('Add Spike', self)
        self.btnAddSpike.clicked.connect(self.add_spike)

        self.btnSaveMap = QPushButton('Save Map', self)
        self.btnSaveMap.clicked.connect(self.save_map_to_db)

        self.comboObject = QComboBox(self)
        self.comboObject.addItem("Block")
        self.comboObject.addItem("Spike")

        layout = self.layout()

        layout.addWidget(self.comboObject)
        layout.addWidget(self.btnAddBlock)
        layout.addWidget(self.btnAddSpike)
        layout.addWidget(self.btnSaveMap)

        self.view.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.draw_grid()

        self.threadpool = QThreadPool()

    def draw_grid(self):
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                rect = QGraphicsRectItem(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                rect.setPen(Qt.lightGray)
                self.scene.addItem(rect)

    def add_block(self):
        x, y = self.snap_to_grid(self.view.mapToScene(self.view.viewport().rect().topLeft()))
        worker = Worker(self.add_block_at_position, x, y)
        self.threadpool.start(worker)

    def add_spike(self):
        x, y = self.snap_to_grid(self.view.mapToScene(self.view.viewport().rect().topLeft()))
        worker = Worker(self.add_spike_at_position, x, y)
        self.threadpool.start(worker)

    def save_map_to_db(self):
        map_name, ok = self.get_text_input('Enter map name:', 'Save Map')
        if ok and map_name:
            map_data = self.serialize_map_data()
            Map.create(name=map_name, data=map_data)
            print(f'Map "{map_name}" saved to the database.')

    def get_text_input(self, prompt, title):
        text, ok = QInputDialog.getText(self, title, prompt)
        return text, ok

    def serialize_map_data(self):
        items = []
        for item in self.scene.items():
            if isinstance(item, DraggableRectItem):
                item_data = {
                    'type': 'block' if item.brush().color() == Qt.black else 'spike',
                    'x': item.x(),
                    'y': item.y(),
                    'width': item.rect().width(),
                    'height': item.rect().height(),
                }
                items.append(item_data)
        return json.dumps(items)

    def add_block_at_position(self, x, y):
        block = DraggableRectItem(x, y, self.cell_size, self.cell_size, self.cell_size)
        block.snap_to_grid()
        self.scene.addItem(block)

    def add_spike_at_position(self, x, y):
        spike = DraggableRectItem(x, y, self.cell_size, self.cell_size, self.cell_size)
        spike.setBrush(Qt.red)
        spike.snap_to_grid()
        self.scene.addItem(spike)

    def snap_to_grid(self, position):
        x = round(position.x() / self.cell_size) * self.cell_size
        y = round(position.y() / self.cell_size) * self.cell_size
        return x, y

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MapEditor()
    main_window.show()
    sys.exit(app.exec_())
