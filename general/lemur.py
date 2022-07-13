from PIL import Image
from PIL import ImageChops

# Open plaintext file with hex
lemur = Image.open('/Users/chaewonlee/Downloads/lemur_ed66878c338e662d3473f0d98eedbd0d.png')
flag = Image.open('/Users/chaewonlee/Downloads/flag_7ae18c704272532658c10b5faad06d74.png')

out = ImageChops.add(ImageChops.subtract(lemur, flag), ImageChops.subtract(flag, lemur))

out.save("save.png")
