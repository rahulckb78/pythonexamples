import io
from customers import customers

class orders:
    """_summary_
    """
    
    def __init__(self, product_cat, product_num, product_qty, currency, amount) -> None:
        self.__qty = product_qty
        self.__cat = product_cat
        self.__product_num = product_num
        self.__product_qty = product_qty
        self.__curr = currency
        self.__amt = amount
    
    def create_order(self, customer_id) -> bool:
        """_summary_

        Args:
            customer_id (_type_): _description_

        Returns:
            bool: _description_
        """
        customer = customers()
        customer_details = customer.get_customer_details(customer_id)
        self.save_order()
        
