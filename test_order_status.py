
from orders import orders

from unittest.mock import patch

@patch('builtins.input', side_effect= (3,0 ,4) )
@patch('builtins.print')
@patch('orders.orders_list', side_effect = [{'name': 'sajeevan', 'address': 'bur road ', 'phone': 6789998212, 'courier': 3, 'Order status': 'Preparing'}, {'name': 'nicki ', 'address': 'trinidad', 'phone': 928321, 'courier': 2, 'Order status': 'Preparing'}])
def test_order_status(mock_input, mock_print):
    # mock_orders_list = MagicMock()
    # mock_orders_list = [{'name': 'sajeevan', 'address': 'bur road ', 'phone': 6789998212, 'courier': 3, 'Order status': 'Preparing'}, {'name': 'nicki ', 'address': 'trinidad', 'phone': 928321, 'courier': 2, 'Order status': 'Preparing'}]
    orders()
    
    assert mock_input.call_count == 3
    assert mock_print.call_count == 1 
    mock_print.assert_called_with([{'name': 'sajeevan', 'address': 'bur road ', 'phone': 6789998212, 'courier': 3, 'Order status': 'Cancelled'}])    

