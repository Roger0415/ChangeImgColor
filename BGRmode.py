///此範例是在BGR模式下對圖片顏色進行調整///

import cv2

img = cv2.imread("圖片路徑")

img_bgr = img.copy()
# 用slice的方式變換顏色 圖片[X,Y,Z]。
# X&Y是圖片size , Z是指Chanel --> 0是藍色 ; 1是綠色 ; 2是紅色。
# 要調整該顏色濃淡深淺, 在slice後面新增"加減乘除"就可以了。

g = img_bgr[:,:,0] 
g1 = img_bgr[:,:,2] * 2   


cv2.imshow('img',img)
cv2.imshow('test',g)
cv2.imshow('g1',g1)

#要結束程式時,案ESC即可終止程式運行。
k = cv2.waitKey(0) & 0xFF
if k == 27: # 27代表ASICII的值,此數字代表著"ESC"按鍵。
 cv2.destroyAllWindows()
