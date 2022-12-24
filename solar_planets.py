import cv2

img = cv2.imread("solar-system.png")

cv2.putText(img,
            "sun",
            (50,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )

cv2.putText(img,
            "mercury",
            (50,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6,
            (225,225,225)
            )

cv2.putText(img,
            "sun",
            (150,550),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )

cv2.imshow("Display",img)
print(img) 
cv2.waitKey(0)
