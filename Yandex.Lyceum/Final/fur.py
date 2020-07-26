from PIL import Image, ImageDraw


class DonkeyWagonImageDraw(ImageDraw.ImageDraw):
    def wagon(self, xy, fill):
        x, y, w, h = xy
        wagon_color, window_color, wheel_color = fill

        self.rectangle(((x, y), (x + w, y + h)), wagon_color)

        window_border = h // 10
        window_side = h - 2 * window_border
        window_x = x + window_border
        window_y = y + window_border

        self.rectangle(((window_x, window_y),
                          (window_x + window_side, window_y + window_side)), window_color)

        wheel_size = w // 5
        wheel_x = x + w // 4 - wheel_size / 2
        wheel_y = y + h
        self.ellipse(((wheel_x, wheel_y),
                        (wheel_x + wheel_size, wheel_y + wheel_size)), wheel_color)

        wheel2_x = x + w - w // 4 - wheel_size / 2
        wheel2_y = y + h
        self.ellipse(((wheel2_x, wheel2_y),
                        (wheel2_x + wheel_size, wheel2_y + wheel_size)), wheel_color)

img = Image.new('RGB', (200, 200), '#000000')
drw = DonkeyWagonImageDraw(img)
drw.wagon((10, 30, 180, 100), ('#ffffff', '#999999', '#666666'))
img.save('result.png')