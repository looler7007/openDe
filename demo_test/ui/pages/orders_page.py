from PySide6.QtWidgets import QWidget
from database.connection import session
from database.models.Order import OrderModel
from database.models.Product import ProductModel
from ui.widgets.OrderCard import Ui_OrderCard
from ui.widgets.OrdersPage import Ui_OrdersPage


class OrderCardWidget(QWidget, Ui_OrderCard):

    def __init__(self, product_name, quantity_of_products, date_of_create):
        super().__init__()
        self.setupUi(self)
        self.setFixedHeight(130)

        self.product_name.setText(product_name)
        self.quantity_of_products.setText("Количество заказанной продукции: " + quantity_of_products + " шт")
        self.date_of_create.setText("Дата создания заказа: " + date_of_create)


class OrderPageWidget(QWidget, Ui_OrdersPage):

    def __init__(self, controller, partner_id):
        super().__init__()
        self.controller = controller

        self.setupUi(self)  #

        self.Title.setText("Заказы")

        self.BackButton.setText("Назад")
        from app import MainWindow
        self.BackButton.clicked.connect(lambda: MainWindow.switch_to_partner_page(controller))

        for order in session.query(OrderModel).filter(OrderModel.fk_company_id == partner_id).all():
            custom_widget = OrderCardWidget(
                str(session.query(ProductModel.name).filter(ProductModel.id == order.fk_product_id).scalar()),
                str(order.quantity_of_products),
                str(order.date_of_create)
            )
            self.verticalLayout_4.addWidget(custom_widget)
