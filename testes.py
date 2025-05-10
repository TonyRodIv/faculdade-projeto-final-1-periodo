from letterboxdpy import movie

filme = movie.Movie("The substance")

print(f"Título: {filme.title}")
print(f"Ano: {filme.year}")
print(f"Diretor: {filme.directors}")
print(f"Avaliação: {filme.rating}/5")
print(f"Gêneros: {filme.genres}")
