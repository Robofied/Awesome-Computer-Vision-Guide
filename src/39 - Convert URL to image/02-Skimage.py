from skimage import io
import cv2

def url_to_image(url):
	image = io.imread(url)
	cv2.imshow("Incorrect", image)
	cv2.imshow("Correct", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

url_to_image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/OpenCV_Logo_with_text_svg_version.svg/1200px-OpenCV_Logo_with_text_svg_version.svg.png")
cv2.waitKey(0)
cv2.destroyAllWindows()
