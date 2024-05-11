from PIL import Image

# 이미지 파일 경로 설정
image_path = 'C:/Users/najw1/Desktop/KAIST/2024_Spring/AI_ML/project/PIFu/sample_images/person.png'
mask_path = 'C:/Users/najw1/Desktop/KAIST/2024_Spring/AI_ML/project/PIFu/sample_images/person_mask.png'

# 이미지 열기
image = Image.open(image_path)
mask = Image.open(mask_path)


print("Image mode:", image.mode)  # 예: 'RGB'
print("Mask mode:", mask.mode)    # 예: 'L' (그레이스케일) 또는 'RGB'

# 이미지와 마스크 크기 조정
new_size = (512, 512)
resized_image = image.resize(new_size, Image.Resampling.LANCZOS)  # Updated resampling method
resized_mask = mask.resize(new_size, Image.Resampling.LANCZOS)

# 조정된 이미지와 마스크 저장
resized_image.save('C:/Users/najw1/Desktop/KAIST/2024_Spring/AI_ML/project/PIFu/sample_images/resized_person.png')
resized_mask.save('C:/Users/najw1/Desktop/KAIST/2024_Spring/AI_ML/project/PIFu/sample_images/resized_person_mask.png')

print("Images resized and saved at 512x512 pixels.")
