import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
import pygame as pg
import sqlite3


class Level():
    def __init__(self):
        self.objects = self.load_objects_from_db()
        self.names = self.objects.keys()

    def draw(self, screen, color):
        for obj in self.names:
            x0 = self.objects[obj][0]
            y0 = self.objects[obj][1]
            w = self.objects[obj][2]
            h = self.objects[obj][3]
            pg.draw.rect(screen, color, (x0, y0, w, h))

    def add(self, name, x, y, w, h):
        self.objects[name] = (x, y, w, h)
        self.save_object_to_db(name, x, y, w, h)

    def load_objects_from_db(self):
        conn = sqlite3.connect('objects.db')
        cursor = conn.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS objects (name TEXT PRIMARY KEY, x INTEGER, y INTEGER, width INTEGER, height INTEGER)')
        conn.commit()

        cursor.execute('SELECT * FROM objects')
        objects = {row[0]: (row[1], row[2], row[3], row[4]) for row in cursor.fetchall()}

        conn.close()
        return objects

    def save_object_to_db(self, name, x, y, w, h):
        conn = sqlite3.connect('objects.db')
        cursor = conn.cursor()

        cursor.execute('INSERT OR REPLACE INTO objects VALUES (?, ?, ?, ?, ?)', (name, x, y, w, h))
        conn.commit()

        conn.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.level = Level()

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.play_button = QPushButton('Add Object', self)
        self.play_button.clicked.connect(self.add_object)

        self.name_label = QLabel('Name:')
        self.x_label = QLabel('X:')
        self.y_label = QLabel('Y:')
        self.width_label = QLabel('Width:')
        self.height_label = QLabel('Height:')

        self.name_input = QLineEdit()
        self.x_input = QLineEdit()
        self.y_input = QLineEdit()
        self.width_input = QLineEdit()
        self.height_input = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.x_label)
        layout.addWidget(self.x_input)
        layout.addWidget(self.y_label)
        layout.addWidget(self.y_input)
        layout.addWidget(self.width_label)
        layout.addWidget(self.width_input)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.play_button)

        central_widget.setLayout(layout)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('PyQt5 and Pygame with SQLite Example')
        self.show()

    def add_object(self):
        name = self.name_input.text()
        x = int(self.x_input.text())
        y = int(self.y_input.text())
        width = int(self.width_input.text())
        height = int(self.height_input.text())

        self.level.add(name, x, y, width, height)
        self.update()

    def update(self):
        pg.init()
        screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("PyQt5 and Pygame with SQLite Example")

        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            screen.fill((255, 255, 255))
            self.level.draw(screen, (0, 0, 255))
            pg.display.flip()

        pg.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
