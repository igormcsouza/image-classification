import cv2

class GrayScalePreprocessor:
    def __init__(self, color=cv2.COLOR_BGR2GRAY):
        """ ## Grayscale Preprocessor
        ...
        """
        self.color = color

    def preprocess(self, image):
        # appçy grayscale to an given image
        return cv2.cvtColor(image, self.color)