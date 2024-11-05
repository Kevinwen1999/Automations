# Shawarma Legend autoClicker

import pyautogui
import pydirectinput
import time

pyautogui.PAUSE = 0.01

# Path to the image you want to detect and click on
entryPointPath = "./shawarmaCaptureImages/entryPoint.png"
startWorkPath = "./shawarmaCaptureImages/startWork.png"
potatoPlacePath = "./shawarmaCaptureImages/potatoImage.png"
fullyFriedPath = "./shawarmaCaptureImages/fullyFried.png"
knifePath = './shawarmaCaptureImages/knife.png'
chefPath = './shawarmaCaptureImages/chef3.png'
cucumberPath = './shawarmaCaptureImages/cucumber.png'
sourCreamPath = './shawarmaCaptureImages/sourCream.png'
customerPath = './shawarmaCaptureImages/shawarmaRequest.png'
doughStackPath = './shawarmaCaptureImages/doughStack.png'
wrapStackPath = './shawarmaCaptureImages/wrapStack.png'
unWrappedPath = './shawarmaCaptureImages/unWrapped.png'
wrappedPath = './shawarmaCaptureImages/wrapped2.png'
deskPath = './shawarmaCaptureImages/desk.png'
wallPath = './shawarmaCaptureImages/wall.png'


entered = False
started = False
friesFrying = False
friesCount = 0
meatCount = 0
cucumberCount = 0
sourCreamCount = 0
shawarmaCount = 0
counterOffset = 0
wallRelativeConstant = 100



def clickRelativeToCenter(location, x_offset, y_offset, holdtime):
    center_x = location.left + location.width // 2
    center_y = location.top + location.height // 2
    adjusted_x = center_x + x_offset
    adjusted_y = center_y + y_offset
    pyautogui.moveTo(adjusted_x, adjusted_y)
    pyautogui.mouseDown()
    time.sleep(holdtime)
    pyautogui.mouseUp()

def clickXTimesRelativeToCenter(location, x_offset, y_offset, holdtime, clickTimes):
    center_x = location.left + location.width // 2
    center_y = location.top + location.height // 2
    adjusted_x = center_x + x_offset
    adjusted_y = center_y + y_offset
    pyautogui.moveTo(adjusted_x, adjusted_y)
    time.sleep(0.01)
    for i in range(clickTimes):
        """ pyautogui.moveTo(adjusted_x, adjusted_y)
        pyautogui.mouseDown()
        pyautogui.sleep(holdtime)  # Optional: small pause between down and up
        pyautogui.mouseUp() """
        """ pyautogui.moveTo(adjusted_x, adjusted_y)
        pydirectinput.click() """
        pyautogui.mouseDown()
        time.sleep(0.01)
        pyautogui.mouseUp()
    time.sleep(0.01)

def dragRelativeToCenter(location, x_offset1, y_offset1, x_offset2, y_offset2):
    center_x = location.left + location.width // 2
    center_y = location.top + location.height // 2
    adjusted_x1 = center_x + x_offset1
    adjusted_y1 = center_y + y_offset1
    adjusted_x2 = center_x + x_offset2
    adjusted_y2 = center_y + y_offset2
    pyautogui.moveTo(adjusted_x1, adjusted_y1)
    time.sleep(0.01)
    pyautogui.mouseDown()
    for x in range(adjusted_y1, adjusted_y2, -10):
        pyautogui.moveTo(adjusted_x1, x)
        time.sleep(0.05)
    # pyautogui.dragTo(adjusted_x2, adjusted_y2, duration=0.1)
    pyautogui.mouseUp()
    time.sleep(0.01)

def dragClickRelativeToCenter(location, x_offset1, y_offset1, x_offset2, y_offset2):
    global counterOffset
    center_x = location.left + location.width // 2
    center_y = location.top + location.height // 2
    adjusted_x1 = center_x + x_offset1 + counterOffset
    adjusted_y1 = center_y + y_offset1
    adjusted_x2 = center_x + x_offset2 + counterOffset
    adjusted_y2 = center_y + y_offset2
    for x in range(adjusted_x1, adjusted_x2, 100):
        pyautogui.moveTo(x, adjusted_y1)
        time.sleep(0.01)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    time.sleep(0.01)
    counterOffset = 50 - counterOffset

def dragBetweenTwoLocation(location1, location2, numSteps):
    center_x1 = location1.left + location1.width // 2
    center_y1 = location1.top + location1.height // 2
    center_x2 = location2.left + location2.width // 2
    center_y2 = location2.top + location2.height // 2

    delta_x = (center_x2 - center_x1) / numSteps
    delta_y = (center_y2 - center_y1) / numSteps

    pyautogui.moveTo(center_x1, center_y1)
    pyautogui.mouseDown()
    time.sleep(0.05)

    for i in range(numSteps):
        step_x = center_x1 + delta_x * (i + 1)
        step_y = center_y1 + delta_y * (i + 1)
        pyautogui.moveTo(step_x, step_y)
        time.sleep(0.05)
    
    pyautogui.mouseUp()

def meatCutting(location, x_offset, y_offset, addTo):
    center_x = location.left + location.width // 2
    center_y = location.top + location.height // 2
    adjusted_x = center_x + x_offset
    adjusted_y = center_y + y_offset
    meat_x_offset = -40
    pyautogui.moveTo(adjusted_x, adjusted_y)
    pyautogui.mouseDown()
    global meatCount
    added = 0
    for i in range(meatCount, addTo, 2):
        pyautogui.moveTo(adjusted_x + meat_x_offset, adjusted_y - 270)
        time.sleep(0.05)
        pyautogui.moveTo(adjusted_x + meat_x_offset, adjusted_y - 250)
        time.sleep(0.05)
        pyautogui.moveTo(adjusted_x + meat_x_offset, adjusted_y - 220)
        time.sleep(0.05)
        pyautogui.moveTo(adjusted_x + meat_x_offset, adjusted_y - 200)
        time.sleep(0.05)
        pyautogui.moveTo(adjusted_x + meat_x_offset, adjusted_y - 180)
        time.sleep(0.05)
        pyautogui.moveTo(adjusted_x + meat_x_offset, adjusted_y - 150)
        time.sleep(0.05)
        pyautogui.moveTo(adjusted_x + meat_x_offset, adjusted_y - 120)
        time.sleep(0.05)
        pyautogui.moveTo(adjusted_x + meat_x_offset, adjusted_y - 100)
        time.sleep(0.05)
        pyautogui.moveTo(adjusted_x + meat_x_offset, adjusted_y - 50)
        time.sleep(0.05)
        pyautogui.moveTo(adjusted_x + meat_x_offset, adjusted_y - 20)
        time.sleep(0.05)
        added += 2
    meatCount += added
    meatCount = max(meatCount, 34)
    pyautogui.mouseUp()
    time.sleep(0.01)

def prepMeat(toAdd):
    try:
        knife = pyautogui.locateOnScreen(knifePath, confidence=0.7)
        if knife:
            print("Cut meat started")
            meatCutting(knife, 0, 0, toAdd)
            print("Cut meat finished!")
            global meatCount
    except:
        print("Trying to cut meat")
        """ time.sleep(0.01) """



# Wait until the image appears
desk = None
try:

    while True:
        try:
            desk = pyautogui.locateOnScreen(deskPath, confidence=0.9)
            print("desk found")
            break
        except:
            print('Continue to look for desk')
            continue


    while True:
        time.sleep(0.4)
        
        """ if not entered:
            try:
                entryLocation = pyautogui.locateOnScreen(entryPointPath, confidence=0.5)  # Confidence level can be adjusted
                if entryLocation:
                    clickRelativeToCenter(entryLocation, -10, 90, 0.2)
                    print("Entry found and clicked!")
                    entered = True
                    time.sleep(5)
            except:
                time.sleep(0.1)
                continue

        if not started:
            try:
                startWorkPath = pyautogui.locateOnScreen(startWorkPath, confidence=0.5)  # Confidence level can be adjusted
                if startWorkPath:
                    clickRelativeToCenter(startWorkPath, 0, 0, 0.5)
                    print("Start Work found and clicked!")
                    started = True
                    time.sleep(1)
            except:
                time.sleep(0.1)
                continue """

         # Detect if customer request exist
        if shawarmaCount > 0:
            try:
                customer = pyautogui.locateOnScreen(customerPath, confidence=0.5)
                wrapped = pyautogui.locateOnScreen(wrappedPath, confidence=0.7)
                dragBetweenTwoLocation(wrapped, customer, 5)
                time.sleep(0.02)
                clickRelativeToCenter(customer, 0, 0, 0)
                time.sleep(0.7)
                dragClickRelativeToCenter(desk, -400, 0, 400, 0)
                dragClickRelativeToCenter(desk, -400, 0, 400, 0)
                print("delivery complete")
                shawarmaCount -= 1
                continue

            except:
                print("Trying to find customer")
                """ time.sleep(0.01) """

        # Fries making
        if friesCount <= 0 and friesFrying == False:
            try:
                potato = pyautogui.locateOnScreen(potatoPlacePath, confidence=0.5)  # Confidence level can be adjusted
                if potato:
                    clickRelativeToCenter(potato, 0, 0, 5)
                    print("potato founded and clicked!")
                    friesFrying = True
                    continue
            except:
                print("Trying to find Potato to Cut")
                """ time.sleep(0.01)
 """
        if friesFrying and friesCount <= 0:
            try:
                potatoReady = pyautogui.locateOnScreen(fullyFriedPath, confidence=0.9)
                if potatoReady:
                    clickRelativeToCenter(potatoReady, 0, 0, 0.05)
                    print("fried potato founded and clicked!")
                    friesCount += 18
                    friesFrying = False
                    continue
            except:
                print("Trying to find Fried Potato")
                """ time.sleep(0.01)     """

        # Meat Cutting
        if meatCount <= 0:
            prepMeat(34)
            continue

        # Garnish Adding
        if cucumberCount <= 0:
            try:
                wall = pyautogui.locateOnScreen(wallPath, confidence=0.9)
                if wall:
                    clickRelativeToCenter(wall, wallRelativeConstant, 0, 0.4)
                    cucumber = pyautogui.locateOnScreen(cucumberPath, confidence=0.5)
                    if cucumber:
                        clickXTimesRelativeToCenter(cucumber, 0, 0, 0.01, 10)
                        print("finish adding cucumber")
                        cucumberCount += 33
                        clickRelativeToCenter(wall, wallRelativeConstant, 0, 0.01)
                        clickRelativeToCenter(wall, 0, 0, 0.01)
                        continue
            except:
                print("Trying to add cucumber")
                """ time.sleep(0.01) """

        if sourCreamCount <= 0:
            try:
                wall = pyautogui.locateOnScreen(wallPath, confidence=0.9)
                if wall:
                    clickRelativeToCenter(wall, wallRelativeConstant, 0, 0.6)
                    sourCream = pyautogui.locateOnScreen(sourCreamPath, confidence=0.6)
                    if sourCream:
                        clickXTimesRelativeToCenter(sourCream, 0, 0, 0.01, 10)
                        print("finish adding sourcream")
                        sourCreamCount += 33
                        clickRelativeToCenter(wall, wallRelativeConstant, 0, 0.01)
                        clickRelativeToCenter(wall, 0, 0, 0.01)
                        continue
            except:
                print("Trying to add sourcream")
                """ time.sleep(0.01) """

        
        # make Shawarma
        if meatCount > 0 and friesCount > 0 and cucumberCount > 0 and sourCreamCount > 0 and shawarmaCount < 3:
            try:
                doughStack = pyautogui.locateOnScreen(doughStackPath, confidence=0.5)
                pyautogui.moveTo(doughStack)
                clickRelativeToCenter(doughStack, 0, 0, 0.05)
                clickXTimesRelativeToCenter(doughStack, -100, -100, 0, 3)
                clickXTimesRelativeToCenter(doughStack, 20, -100, 0, 3)
                clickXTimesRelativeToCenter(doughStack, 200, -100, 0, 3)
                clickXTimesRelativeToCenter(doughStack, 300, -100, 0, 3)
                meatCount -= 3
                friesCount -= 3
                cucumberCount -= 3
                sourCreamCount -= 3
                dragRelativeToCenter(doughStack, 300, 0, 300, -110)
                wrapStack = pyautogui.locateOnScreen(wrapStackPath, confidence=0.8)
                unWrapped = pyautogui.locateOnScreen(unWrappedPath, confidence=0.9)
                dragBetweenTwoLocation(wrapStack, unWrapped, 5)
                clickRelativeToCenter(unWrapped, 0, -50, 0)
                shawarmaCount += 1
                continue
            except:
                print("Can't make Shawarma")
                """ time.sleep(0.01) """

        
        if meatCount < 34:
            """ dragClickRelativeToCenter(desk, -400, 0, 400, 0)
            dragClickRelativeToCenter(desk, -400, 0, 400, 0) """
            prepMeat(34)
        

except KeyboardInterrupt:
    print("\nProcess interrupted by user. Exiting...")
