#!/usr/bin/env python3
"""
Простой клиент для взаимодействия с Ollama
"""

import requests
import json
import os

class OllamaClient:
    def __init__(self, host="http://localhost:11434"):
        self.host = host
        self.api_base = f"{host}/api"
        
    def generate(self, model, prompt, system=None, options=None, stream=False):
        """Генерация текста с помощью модели"""
        url = f"{self.api_base}/generate"
        data = {
            "model": model,
            "prompt": prompt,
            "stream": stream
        }
        
        if system:
            data["system"] = system
        if options:
            data["options"] = options
            
        response = requests.post(url, json=data)
        response.raise_for_status()
        
        if stream:
            return response.json()
        else:
            return response.json()["response"]
    
    def list_models(self):
        """Получение списка доступных моделей"""
        url = f"{self.api_base}/tags"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["models"]
    
    def pull_model(self, model_name):
        """Загрузка модели"""
        url = f"{self.api_base}/pull"
        data = {"name": model_name}
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

def main():
    # Инициализация клиента
    client = OllamaClient()
    
    # Показать доступные модели
    print("Доступные модели:")
    try:
        models = client.list_models()
        for model in models:
            print(f"- {model['name']}")
    except Exception as e:
        print(f"Не удалось получить список моделей: {e}")
        print("Убедитесь, что Ollama запущен командой 'ollama serve'")
        return
    
    # Пример генерации
    print("\nПример генерации:")
    try:
        response = client.generate(
            model="llama2", 
            prompt="Кратко объясни, что такое искусственный интеллект"
        )
        print(response)
    except Exception as e:
        print(f"Ошибка при генерации: {e}")
        print("Убедитесь, что модель установлена командой 'ollama pull llama2'")

if __name__ == "__main__":
    main()