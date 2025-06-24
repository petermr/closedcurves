from closedcurves import draw

def test_image_generation():
    image = draw.generate_curve_image({"seed": 123})
    assert image is not None
    assert image.size[0] > 0
    assert image.size[1] > 0

