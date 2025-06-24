import argparse
from closed_curves import draw
from datetime import datetime
import os

def main():
    parser = argparse.ArgumentParser(description="Draw and save a closed curve.")
    parser.add_argument("--output", type=str, default="diagrams/curve.png")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--log", action="store_true", help="Save log of generation parameters")
    args = parser.parse_args()

    image = draw.generate_curve_image({"seed": args.seed})
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    image.save(args.output)

    if args.log:
        os.makedirs("diagrams/logs", exist_ok=True)
        with open("diagrams/logs/record.txt", "a") as f:
            f.write(f"{datetime.now().isoformat()} | seed={args.seed} -> {args.output}\n")

if __name__ == "__main__":
    main()

