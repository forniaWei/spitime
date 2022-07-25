
import os
from getRootPath import root_dir




def getScreen(driver,caseName):
    picture_path = os.path.join(root_dir, "pictures")
    # picture_path = os.path.join(picture_path, direc)
    picture = os.path.join(picture_path, caseName + ".png")
    driver.save_screenshot(picture)

