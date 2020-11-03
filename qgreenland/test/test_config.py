from qgreenland.config import CONFIG


def test_get_layer_config_all():
    layer_config = CONFIG['layers']

    # There are at least 2 layers.
    assert len(layer_config.keys()) >= 2


def test_get_layer_config_one():
    # If the layer does not exist, an exception will be raised and pytest will
    # appropriately fail.
    CONFIG['layers']['ne_coastlines']
