from variables import *
import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QBrush, QColor

class ObjectManager:
    def __init__(self):
        self.objects = []
        self.grid_size = GRID_SIZE
    
    def add_object(self, coords, size):
        obj = QGraphicsRectItem(coords, size)
        self.objects.append(obj)
        return obj
    
    def remove_onject(self, coords, size):
        obj = QGraphicsRectItem(coords, size)
        self.objects.remove(obj)
        return obj
    
class GraficsScene(QGraphicsScene):
    def __init__(self, object_manager):
        super(QGraphicsScene, self).__init__()
        self.object_manager = object_manager
        self.selected_object = "{}"
        self.draw_grid()

class MainWindow(QMainWindow):
    def __init__(self):
        self.object_manager = ObjectManager()
        self.scene = QGraphicsScene(self.object_manager)