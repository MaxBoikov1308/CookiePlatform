import sys
import pygame as pg
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QComboBox
from peewee import SqliteDatabase, Model, TextField, IntegerField
from files.scripts.objects import *
from files.levels.level2 import Level2
from files.levels.level1 import Level1


currect_level = Level2
db = SqliteDatabase(f"files/levels/level2.db")


class MapBuilder(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.object_type_label = QLabel("Object Type:")
        self.object_type_combobox = QComboBox()
        self.object_type_combobox.addItems(["block", "cookie", "finish", "start", "enemy", "spike"])
        
        self.x_label = QLabel("X:")
        self.x_edit = QLineEdit()

        self.y_label = QLabel("Y:")
        self.y_edit = QLineEdit()

        self.width_label = QLabel("Width:")
        self.width_edit = QLineEdit()

        self.height_label = QLabel("Height:")
        self.height_edit = QLineEdit()

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_to_database)

        layout = QVBoxLayout()
        layout.addWidget(self.object_type_label)
        layout.addWidget(self.object_type_combobox)
        layout.addWidget(self.x_label)
        layout.addWidget(self.x_edit)
        layout.addWidget(self.y_label)
        layout.addWidget(self.y_edit)
        layout.addWidget(self.width_label)
        layout.addWidget(self.width_edit)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_edit)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self.setWindowTitle("Map Builder")
        self.show()

    def save_to_database(self):
        object_type = self.object_type_combobox.currentText()
        x = int(self.x_edit.text()) * 50
        y = int(self.y_edit.text()) * 50
        width = int(self.width_edit.text()) * 50
        height = int(self.height_edit.text()) * 50

        currect_level.create(Object_type=object_type, x=x, y=y, w=width, h=height)
        self.show_result_window()

    def show_result_window(self):
        pg.init()
        screen_width = 1920 / 5
        screen_height = 1080 / 5
        screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption("Map Result")

        clock = pg.time.Clock()

        objects = currect_level.select()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()


            screen.fill((0, 0, 0))

            for obj in objects:
                color = (255, 255, 255)  # Default color
                if obj.Object_type == "block":
                    color = (255, 0, 0)  # Red color
                elif obj.Object_type == "cookie":
                    color = (0, 255, 0)  # Green color
                elif obj.Object_type == "finish":
                    color = (0, 0, 255)  # Blue color
                elif obj.Object_type == "start":
                    color = (255, 255, 0)  # Yellow color
                elif obj.Object_type == "enemy":
                    color = (255, 0, 255)  # Magenta color
                elif obj.Object_type == "spike":
                    color = (0, 255, 255)  # Cyan color

                pg.draw.rect(screen, color, (obj.x / 5, obj.y / 5, obj.w / 5, obj.h / 5))
            pg.display.flip()
            clock.tick(60)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    builder = MapBuilder()
    sys.exit(app.exec_())
