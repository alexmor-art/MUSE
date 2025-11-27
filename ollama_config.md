# Ollama Configuration Guide

## Установка Ollama

### Linux
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### macOS
```bash
brew install ollama
```

### Windows
Скачайте установщик с официального сайта: https://ollama.ai

## Запуск Ollama

```bash
ollama serve
```

## Установка моделей

```bash
ollama pull llama2
ollama pull mistral
ollama pull gemma:2b
```

## Использование через командную строку

```bash
ollama run llama2
```

## Использование через API

### Запуск модели
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Почему небо синее?"
}'
```

### Создание модели
```bash
curl http://localhost:11434/api/create -d '{
  "name": "mymodel",
  "modelfile": "FROM llama2\nSYSTEM Вы - полезный ассистент"
}'
```

## Настройка для доступа извне (если нужно)

По умолчанию Ollama слушает только localhost. Для доступа извне:

```bash
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

Или установите переменную окружения в файле `.env`:

```
OLLAMA_HOST=0.0.0.0:11434
```

## Пример Python-скрипта для взаимодействия с Ollama

```python
import requests
import json

def query_ollama(prompt, model="llama2"):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(url, json=data)
    return response.json()["response"]

# Пример использования
result = query_ollama("Расскажи о себе")
print(result)
```

## Доступные модели

- llama2
- llama3
- mistral
- gemma
- phi
- neural-chat
- starling-lm
- qwen
- command-r
- many more...

Для просмотра всех доступных моделей посетите: https://ollama.ai/library