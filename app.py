# Programme Python pour résoudre une équation non linéaire f(x) = 0
# en utilisant la méthode de la sécante.
# La méthode nécessite deux approximations initiales (bornes de l'intervalle).
# L'utilisateur est demandé à entrer la fonction f(x) non linéaire.  

print("Bienvenue à l'Application Dufay!","\nCette application vous permet de résoudre toutes les équations non linéaires avec x comme variable","\nElle vous propose à la fin la valeur de x et celle de la foction f(x) approximée")
print()
import math
#fonction entrée par l'utilisateur
f_str=input("Veuillez entrer votre fonction non linéaire f(x): ")

#Entrée des bornes de l'intervalle par l'utilisateur

x0 = float(input("Entrez la première borne de l'intervalle (x0) : "))
x1 = float(input("Entrez la seconde borne de l'intervalle (x1) : "))
r1 = eval(f_str, {"__builtins__": {}}, {"x": x0, "math": math})
r2 = eval(f_str, {"__builtins__": {}}, {"x": x1, "math": math})
# Paramètres de convergence
tol = 1e-100  # Tolérance pour l'erreur de la solution
max_it = 1000  # Nombre maximum d'itérations

# Méthode de la sécante
it = 0
while it < max_it:
    r1 = eval(f_str, {"__builtins__": {}}, {"x": x0, "math": math})
    r2 = eval(f_str, {"__builtins__": {}}, {"x": x1, "math": math})
    fx0 = r1
    fx1 = r2
# Vérifier si une des valeurs est déjà une racine
    if abs(fx0) < tol:
        print(f"La racine trouvée est : x = {x0} après {it} itérations.")
        print(f"La valeur de f(x) est : {fx0}")
        break
    if abs(fx1) < tol:
        print(f"La racine trouvée est : x = {x1} après {it} itérations.")
        print(f"La valeur de f(x) est : {fx1}")
        break
# Calcul de la nouvelle approximation x2
    if fx1 - fx0 == 0:
        print("La division par zéro n'est pas possible! Les bornes choisies ne sont pas adaptées.","\nVeuillez en choisir d'autres")
        break
    
    x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
# Actualisation des valeurs
    x0 = x1
    x1 = x2
    r2 = eval(f_str, {"__builtins__": {}}, {"x": x1, "math": math})  
    it += 1
# Vérifier la convergence
    if abs(x1 - x0) < tol:
        print(f"La racine approximée est : x ≈ {x1} après {it} itérations.")
        print(f"La valeur de f(x) est : {r2}")
        break
else:
    print("Méthode non convergée dans le nombre maximum d'itérations.","\nVeuillez choisir de nouvelles bornes au départ")
