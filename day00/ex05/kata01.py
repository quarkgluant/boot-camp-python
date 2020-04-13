#!/usr/bin/env python3
# -*-coding:utf-8 -*


languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

for language, author in languages.items():
    print(f"{language} was created by {author}")
