import numpy as np
import matplotlib
matplotlib.use("Agg")  # Headless
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

def generate_closed_curve(seed=0):
    np.random.seed(seed)
    num_points = 100
    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    radius = 1 + 0.2 * np.random.rand(num_points)
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    return x, y

def generate_curve_image(params):
    seed = params.get("seed", 0)
    x, y = generate_closed_curve(seed)

    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot(np.append(x, x[0]), np.append(y, y[0]), 'k-', lw=2)
    ax.set_aspect('equal')
    ax.axis('off')

    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf)

