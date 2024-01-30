import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QPushButton, QVBoxLayout, QWidget
from PySide2.QtGui import QBrush, QColor
from peewee import SqliteDatabase, Model, TextField, IntegerField

# Инициализация базы данных
db = SqliteDatabase("C:/Users/n-pas/PycharmProjects/CookiePlatform/levels/level2.db")


class Level(Model):
    name = TextField()
    x = IntegerField()
    y = IntegerField()
    h = IntegerField()
    w = IntegerField()

    class Meta:
        database = db


# Создание таблицы, если её нет
db.connect()
db.create_tables([Level], safe=True)


class ObjectManager:
    def __init__(self):
        self.objects = []
        self.grid_size = 50

    def add_object(self, x, y, w, h, is_block):
        obj = GraphicsRectItem(x, y, w, h, is_block)
        self.objects.append(obj)
        return obj

    def save_to_database(self):
        for obj in self.objects:
            Level.create(name="object", x=obj.x(), y=obj.y(), h=obj.rect().height(), w=obj.rect().width())


class GraphicsRectItem(QGraphicsRectItem):
    def __init__(self, x, y, w, h, is_block):
        super(GraphicsRectItem, self).__init__(x, y, w, h)
        self.is_block = is_block

    def save_to_database(self, x, y, w, h):
        Level.create(name="object", x=x, y=y, h=h, w=w)


class GraphicsScene(QGraphicsScene):
    def __init__(self, object_manager):
        super(GraphicsScene, self).__init__()
        self.object_manager = object_manager
        self.selected_object = "block"
        self.draw_grid()
        self.load_objects_from_database()

    def draw_grid(self):
        for x in range(0, 501, self.object_manager.grid_size):
            for y in range(0, 501, self.object_manager.grid_size):
                self.addRect(x, y, self.object_manager.grid_size, self.object_manager.grid_size)

    def load_objects_from_database(self):
        for obj in Level.select():
            x, y, w, h = obj.x, obj.y, obj.w, obj.h
            is_block = True  # Assuming all objects loaded from the database are blocks
            color = QColor(255, 0, 0) if is_block else QColor(0, 255, 0)
            brush = QBrush(color)
            graphics_rect_item = self.object_manager.add_object(x, y, w, h, is_block)
            graphics_rect_item.setBrush(brush)
            self.addItem(graphics_rect_item)


    def mousePressEvent(self, event):
        x = int(event.scenePos().x() // self.object_manager.grid_size) * self.object_manager.grid_size
        y = int(event.scenePos().y() // self.object_manager.grid_size) * self.object_manager.grid_size
        w = self.object_manager.grid_size
        h = self.object_manager.grid_size

        is_block = self.selected_object == "block"
        color = QColor(255, 0, 0) if is_block else QColor(0, 255, 0)
        brush = QBrush(color)
        obj = self.object_manager.add_object(x, y, w, h, is_block)
        obj.setBrush(brush)
        self.addItem(obj)
        obj.save_to_database(x, y, w, h)

    def set_selected_object(self, obj):
        self.selected_object = obj



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.object_manager = ObjectManager()
        self.scene = GraphicsScene(self.object_manager)
        self.view = QGraphicsView(self.scene)

        block_button = QPushButton("Block", self)
        block_button.clicked.connect(lambda: self.scene.set_selected_object("block"))

        spike_button = QPushButton("Spike", self)
        spike_button.clicked.connect(lambda: self.scene.set_selected_object("spike"))

        save_button = QPushButton("Save Database", self)
        save_button.clicked.connect(self.object_manager.save_to_database)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(block_button)
        layout.addWidget(spike_button)
        layout.addWidget(save_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle("Level Editor")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
