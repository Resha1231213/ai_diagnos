import os
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

load_dotenv()

# Создаём клиента OpenAI с API ключом
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def analyze_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prompt = data.get('text', '')

            # Запрос к ChatGPT
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "Ты медицинский ассистент. Анализируй текст пациента, объясняй диагнозы и предупреждай о рисках."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=800
            )

            result = response.choices[0].message.content
            return JsonResponse({'result': result})

        except OpenAIError as e:
            return JsonResponse({'result': f'Ошибка OpenAI: {str(e)}'}, status=500)
        except Exception as e:
            return JsonResponse({'result': f'Общая ошибка: {str(e)}'}, status=500)

    return JsonResponse({'result': 'Неверный метод запроса'}, status=400)
