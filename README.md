# Blur Dataset
## Description
This dataset contains 1050 blurred and sharp images (350 triplets), each image triplet is a set of three photos of the same scene: sharp, defocused-blurred and motion-blurred images.

The dataset was created to validate the blur detection algorithm. The dataset can also be used for testing image deblurring, hovewer, the triplets are not "pixel-to-pixel" images, so, one cannot compare blurred and sharp images on the basis of PSNR or SSIM but sharp images can be used for visual comparison.

## Dataset structure

The dataset contains three folders: sharp, defocused-blurred and motion-blurred images.

The filename structure is as follows: id_device_type.extension where
 - ID - a number from 0 to 349;
 - device - the image capture device;
 - type - one of [S, F, M]. S stands for Sharp image, F - deFocused-blurredimage and M - Motion-blurred image.
          
The dataset contains 70 devices, these are typically smartphones, but several cameras are also provided.
<details> 
<summary>Devices list:</summary>
<p> 
HONOR-7X: 34
HONOR-8X: 33
IPHONE-SE: 30
NIKON-D3400-35MM: 25
XIAOMI-PROCOFONE-F1: 23
NIKON-D3400-18-55MM: 21
IPHONE-7: 13
IPHONE-6S: 12
XIAOMI-MI8-SE: 9
SAMSUNG-GALAXY-J3: 7
ASUS-ZENFONE-LIVE-ZB501KL: 6
HONOR-7C: 6
HUAWEI-P20-LITE: 6
SONY-NEX-5T: 6
HONOR-10: 5
HUAWEI-P20: 5
IPHONE-8-PLUS: 5
XIAOMI-REDMI-7: 5
HUAWEI-MATE20: 4
HUAWEI-Y9: 4
IPHONE-8: 4
CANON-6D-100MM: 3
HONOR-9: 3
HUAWEI-NOVA-LITE: 3
IPHONE-7-PLUS: 3
SAMSUNG-GALAXY-A8: 3
SAMSUNG-GALAXY-J5: 3
WILEYFOX-SWIFT-2-PLUS: 3
XIAOMI-REDMI-3S: 3
XIAOMI-REDMI-NOTE-7: 3
HUAWEI-P30-PRO: 2
ONEPLUS-3T: 2
SAMSUNG-GALAXY-A5: 2
SAMSUNG-GALAXY-A6: 2
SAMSUNG-GALAXY-J7: 2
XIAOMI-REDMI-5-PLUS: 2
ASUS-ZE500KL: 1
BQ-5512L: 1
CANON-6D-70-200MM: 1
HONOR-4C: 1
HONOR-6X: 1
HONOR-9-LITE: 1
HUAWEI-ATH: 1
HUAWEI-P-SMART: 1
HUAWEI-P30: 1
HUAWEI-P30-LITE: 1
IPHONE-5S: 1
IPHONE-6: 1
IPHONE-XR: 1
LG-Q6: 1
MEIZU-M2-NOTE: 1
MEIZU-M3S-MINI: 1
NOKIA-21: 1
PANASONIC-DMC-TZ35: 1
PRESTIGIO-MULTI-PHONE: 1
SAMSUNG-EDGE-7C: 1
SAMSUNG-GALAXY-7-NEO: 1
SAMSUNG-GALAXY-A3: 1
SAMSUNG-GALAXY-A8-PLUS: 1
SAMSUNG-GALAXY-GRAND-PRIME: 1
SAMSUNG-GALAXY-GRAND-PRIME-PLUS: 1
SAMSUNG-GALAXY-S5: 1
SONY-XPERIA-E5: 1
XIAOMI-MI8-LITE: 1
XIAOMI-MI8-PRO: 1
XIAOMI-REDMI-4: 1
XIAOMI-REDMI-4X: 1
XIAOMI-REDMI-NOTE-2: 1
XIAOMI-REDMI-NOTE-4X: 1
XIAOMI-REDMI-NOTE-5A-PRIME: 1
</p> 
</details>
## Download
Kaggle dataset (images were scaled to 1024 pixels by the widest side): todo

Google drive (source images): todo

## Images samples

## Licence
todo

## How to cite
todo


Данная база представляет собой 1050 изображений (350 троек), каждая тройка изображений - это фото одной и той же сцены: чёткое фото, расфокусированное изображение и смазанное в движении.

База создана для проверки алгоритма детектирования блюра на изображении. Также можно использовать для тестов деблюра изображений, однако, это не пиксель в пиксель изображения, поэтому вы не можете использовать сравнение с помощью psnr, ssim и тд, но можно использовать для визуального анализа.

В базе три папки соответственно с чёткими, расфокусированными и смазанными в движении изображениями.

Структура имени файла следующая: ид_девайс_тип. ID - число от 0 до 349, девайс - устройство, которым сделан снимок, тип - дублирующая информация, одно из трех - S sharp, F defocus, M movement blur.

В базе представлены N устройств, в основном, это смартфоны, но есть и фото с фотоаппаратов


