def test_order_service(order_service, business_params):
    result = order_service.calculate_recommended_orders(business_params)

    assert isinstance(result, list)
    assert len(result) > 0

    for r in result:
        assert "SKU" in r
        assert "recommended_quantity" in r