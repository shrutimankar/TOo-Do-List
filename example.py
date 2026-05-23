 from PIL import Image, ImageDraw, ImageFont

# Create an image for Minimax Tree with Alpha-Beta Pruning Example
width, height = 800, 600
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Font settings
try:
    font = ImageFont.truetype("arial.ttf", 18)
except IOError:
    font = ImageFont.load_default()

# Draw tree structure manually
draw.text((380, 40), "MAX", fill="black", font=font)        # Root
draw.text((180, 120), "MIN", fill="black", font=font)       # Left child
draw.text((580, 120), "MIN", fill="black", font=font)       # Right child

# Leaf nodes
draw.text((100, 200), "3", fill="black", font=font)
draw.text((260, 200), "5", fill="black", font=font)
draw.text((500, 200), "6", fill="black", font=font)
draw.text((660, 200), "9", fill="gray", font=font)  # Pruned

# Draw lines from parent to children
draw.line((400, 60, 200, 120), fill="black", width=2)
draw.line((400, 60, 600, 120), fill="black", width=2)
draw.line((200, 140, 120, 200), fill="black", width=2)
draw.line((200, 140, 280, 200), fill="black", width=2)
draw.line((600, 140, 520, 200), fill="black", width=2)
draw.line((600, 140, 680, 200), fill="gray", width=2)

# Pruning annotation
draw.text((700, 240), "Pruned", fill="gray", font=font)

# Save image
image.save("minimax_alpha_beta_pruning_example.png")
