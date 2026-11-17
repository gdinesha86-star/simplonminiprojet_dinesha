import matplotlib.pyplot as plt

produits = ['Produit A', 'Produit B', 'Produit C']
ventes = [1750, 1055, 575]
ca = [17500, 15825, 11500]

plt.figure(figsize=(8, 5))
plt.bar(produits, ventes, color=['#4CAF50', '#FFC107', '#2196F3'])
plt.title('Ventes par produit (quantité)')
plt.ylabel('Quantité vendue')
plt.savefig('ventes_produit.png')
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(produits, ca, color=['#4CAF50', '#FFC107', '#2196F3'])
plt.title("Chiffre d'affaires par produit (€)")
plt.ylabel("Chiffre d'affaires (€)")
plt.savefig('ca_produit.png')
plt.show()