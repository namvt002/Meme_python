"""MemeGenerator."""


from PIL import Image, ImageDraw, ImageFont
import random


class MemeGenerator:
    """The MemeEngine class drawing text to mages."""

    def __init__(self, output_dir: str):
        """
        Initialize the MemeGenerator class.

        :param output_dir: The directory path will be saved.
        """
        self.output_dir = output_dir

    def make_meme(self,
                  img_path: str,
                  text: str,
                  author: str,
                  width: int = 500) -> str:
        """Load image from disk and resize"""
        try:
            image = Image.open(img_path)
        except Exception as e:
            print(f"Error: Could not save image file 29.Err: {str(e)}")

            return ""

        aspect_ratio = width / float(image.size[0])
        height = int(aspect_ratio * float(image.size[1]))

        try:
            image = self.resize_image(img_path, width)
            print(image)

            # Add caption to image
            image = self.add_caption(image, text, author)
            print(image)
            str_ran = str(random.randint(0, 1000))
            output_path = self.output_dir + '/' + str_ran + '.jpg'
            print(output_path)
            image.save(output_path, "JPEG")
        except Exception as e:
            print(f"Error: Could not save image file .Err: {str(e)}")

            return ""

        return output_path

    def add_caption(self, img: Image, text: str, author: str) -> Image:
        """add caption."""
        draw = ImageDraw.Draw(img)
        text = text.replace("\u2019", "")
        author = author.replace("\u2019", "")
        caption = f"{text}\n- {author}"
        font_size = max(1, int(img.width / 20))
        # Determine random location for caption
        x = random.randint(0, img.width - int(font_size / 2) - 50)
        y = random.randint(0, img.height - font_size * 2)
        # x = random.randint(0, int(img.width / 2))
        # y = random.randint(0, int(img.height / 2))
        print(x, y)
        # Set caption color and outline
        text_color = (0, 0, 0)
        ol_color = "white"

        # Draw caption text on the image
        draw.text((x-1, y-1), caption, fill=ol_color)
        draw.text((x+1, y-1), caption, fill=ol_color)
        draw.text((x-1, y+1), caption, fill=ol_color)
        draw.text((x+1, y+1), caption, fill=ol_color)
        draw.text((x, y), caption, fill=text_color)

        return img

    def resize_image(self, img_path: str, width: int) -> Image:
        """resize image"""
        img = Image.open(img_path)
        if img.width > width:
            ratio = width / float(img.width)
            height = int(ratio * img.height)
            img = img.resize((width, height), Image.NEAREST)
        return img
