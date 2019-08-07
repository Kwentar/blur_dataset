import cv2
import numpy as np


def generate_defocused_kernel(kernel_size: int, n: int, kernel_value=250):
    """
    Generate kernel (PSF) for defocused-blurred images generation
    :param kernel_size: Size of result kernel, usually <= 128
    :param n: -1 for circle, >2 means amount of angles for regular polygon,
    4 for square and so on, 0, 1 and 2 not allowed
    :param kernel_value: default pixel value on kernel
    :return: PSF as image with size kernel_size x kernel_size and 1 channel
    """
    kernel = np.zeros((kernel_size, kernel_size))
    r = kernel_size*0.4
    if n == -1:
        cv2.circle(kernel, (kernel_size//2, kernel_size//2), int(r),
                   kernel_value, -1)
    else:
        points = np.zeros((n, 2), dtype=np.int32)
        for i in range(n):
            x = int(r * np.cos(2*np.pi * i / n))+kernel_size//2
            y = int(r * np.sin(2*np.pi * i / n))+kernel_size//2
            points[i] = [x, y]
        cv2.fillPoly(kernel, pts=[points], color=kernel_value)
    kernel = cv2.blur(kernel, (3, 3))
    noise = np.random.normal(0, 2, (kernel_size, kernel_size))
    print(np.max(noise), np.min(noise))
    mask = kernel.copy()*255/kernel_value

    return cv2.bitwise_and((kernel + noise), mask)

def 
if __name__ == '__main__':
    img = generate_defocused_kernel(400, 16)
    cv2.imshow('img', img.astype(np.uint8))
    cv2.waitKey()
