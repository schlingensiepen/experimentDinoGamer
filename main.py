import cv2 as cv
import numpy as np
import pyautogui
import pygame
from time import time
from windowcapture import WindowCapture
from vision import Vision
from vision_D import Vision_D
from vision_B import Vision_B



loop_time = time()
while(True):



    # initialize the WindowCapture class
    wincap = WindowCapture('pygame window')
    # initialize the Vision class
    vision_cactus = Vision('D_cactus.JPG')
    vision_cactus2 = Vision('D_cactus2.JPG')
    vision_bird = Vision_B('D_bird.JPG')
    vision_dino = Vision_D('D_dino.JPG')



    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    points = vision_cactus.find(screenshot, 0.5, 'rectangles')
    points = vision_cactus2.find(screenshot, 0.5, 'rectangles')
    points = vision_bird.find(screenshot, 0.7, 'rectangles')
    points = vision_dino.find(screenshot, 0.38, 'rectangles')
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()


    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
