import math
import cv2
import numpy as np
import math
from collections import defaultdict


class Hough:
    def __init__(self, img):
        self.img = img

    def getImg(self):
        return self.img

    def __get_edges(self, img, min_edge_threshold=100, max_edge_threshold=200):

        # convert to gray scale
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Edge detection on the input image
        edge_image = cv2.Canny(
            gray_image, min_edge_threshold, max_edge_threshold)
        return edge_image

    def __superimpose(self, lines, color):
        img = self.getImg()
        src = np.copy(img)
        for i in range(len(lines)):
            r, theta = lines[i]
            pt1, pt2 = (0, 0), (0, 0)
            a, b = math.cos(math.radians(theta)), math.sin(math.radians(theta))
            x0, y0 = a * r, b * r
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            cv2.line(src, pt1, pt2, color, 1, cv2.LINE_AA)
        return src

    def __hough_lines(self, src, threshold):
        diagonal = math.ceil(
            math.sqrt(src.shape[0] * src.shape[0] + src.shape[1] * src.shape[1]))
        # declare the accumulator matrix as zero matrix
        acc = np.zeros((2 * diagonal, 180), dtype=np.uint8)
        lines = []

        # find the location of edges
        rows, cols = np.nonzero(src)

        cos_theta = np.cos(np.radians(np.arange(-90, 90)))
        sin_theta = np.sin(np.radians(np.arange(-90, 90)))
        for row, col in zip(rows, cols):
            # calculate the hough transform for each edge
            r = np.round(col * cos_theta + row * sin_theta)
            acc[r.astype(int), np.arange(180)] += 1

        for i in range(acc.shape[0]):
            for j in range(acc.shape[1]):
                if acc[i, j] >= threshold:
                    lines.append((i, j - 90))

        return lines

    def detect_lines(self, threshold, color=(255, 0, 0)):
        img = self.getImg()
        edges = self.__get_edges(img, 50)
        lines = self.__hough_lines(edges, threshold)
        # draw the lines on the original image
        res = self.__superimpose(lines, color)

        return res

    
