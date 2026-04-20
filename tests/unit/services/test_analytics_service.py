def test_get_abc(analytics_service):
    result = analytics_service.get_abc()

    assert isinstance(result, list)
    assert len(result) > 0

    for r in result:
        assert "product_code" in r
        assert "revenue" in r
        assert "category" in r


def test_get_xyz(analytics_service):
    result = analytics_service.get_xyz()

    assert isinstance(result, list)

    for r in result:
        assert "cv" in r
        assert "xyz_category" in r
        assert r["xyz_category"] in ["X", "Y", "Z"]


def test_get_seasonality(analytics_service):
    result = analytics_service.get_seasonality()

    assert isinstance(result, list)

    for r in result:
        assert "month" in r
        assert "revenue" in r