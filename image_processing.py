import cv2; img = cv2.imread('../image_processing/mt_kailash/visiting-mount-kailash-two.jpeg'); cv2.imshow('Gray', cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)); cv2.waitKey(0); cv2.destroyAllWindows()
