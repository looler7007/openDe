import sys
from PySide6.QtCore import QTranslator, QLibraryInfo
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from ui.pages.create_update import CreateUpdatePageWidget
from ui.pages.orders_page import OrderPageWidget
from ui.pages.partner_page import PartnerPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Партнеры")
        self.setGeometry(400, 400, 980, 500)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        # self.partner_page_widget = PartnerPageWidget()
        self.partner_page = PartnerPage(self)
        self.central_widget.addWidget(self.partner_page)
        self.order_page = None

    def switch_to_update_page(self, partner_id: int):
        self.setWindowTitle("Обновление заявки")

        self.order_page = CreateUpdatePageWidget(self, "update", partner_id)
        self.central_widget.addWidget(self.order_page)

        self.central_widget.setCurrentWidget(self.order_page)

    def switch_to_create_page(self):
        self.setWindowTitle("Создание заявки")

        self.order_page = CreateUpdatePageWidget(self, "create")
        self.central_widget.addWidget(self.order_page)

        self.central_widget.setCurrentWidget(self.order_page)

    def switch_to_order_page(self, partner_id: int):
        self.setWindowTitle("Заказы")

        self.order_page = OrderPageWidget(self, partner_id)
        self.central_widget.addWidget(self.order_page)

        self.central_widget.setCurrentWidget(self.order_page)

    @staticmethod
    def switch_to_partner_page(self):
        self.setWindowTitle("Партнеры")

        self.new_partner_page = PartnerPage(self)
        self.central_widget.addWidget(self.new_partner_page)
        self.central_widget.setCurrentWidget(self.new_partner_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load("qtbase_ru", QLibraryInfo.path(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)
    window = MainWindow()
    window.setWindowIcon(QPixmap("myui/icons/Master_pol.ico"))
    window.show()
    app.exec()
