from transformers import pipeline

generator = pipeline("text-generation")
result = generator("lets do it", max_new_tokens=50)  # Ganti angka 50 dengan jumlah token yang Anda inginkan
print(result[0]['generated_text'])
