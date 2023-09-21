from django.shortcuts import render

books = [
  {
    'name': 'Don Quichotte de la Manche',
    'genre': 'classique',
    'description': "Le message que souhaite faire passer Don Quichotte est une vision dialectique de la vie sous la forme d'une lutte entre le réel et l'imaginaire, l'idéal. Pour vivre son imaginaire, il ne suffit pas de le penser.",
    'year': 1605},
  {'name': 'Le Petit Prince', 'genre': 'classique', 'description': 'Un aviateur tombe en panne au beau milieu du désert du Sahara. De là naît la rencontre avec un garçon, qui va lui demander le très célèbre « s’il vous plaît… dessine-moi un mouton ».', 'year': 1990},
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def books_index(request):
  return render(request, 'books/index.html',
    {
      'books': books,
    })
