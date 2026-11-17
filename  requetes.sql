-- a. Chiffre d'affaires total
SELECT SUM(prix * qte) AS chiffre_affaires_total
FROM Sales;

-- b. Ventes par produit (quantité + argent)
SELECT produit, 
       SUM(qte) AS total_ventes_quantite,
       SUM(prix * qte) AS chiffre_affaires
FROM Sales
GROUP BY produit
ORDER BY total_ventes_quantite DESC;

-- c. Ventes par région
SELECT region, SUM(qte) AS total_ventes, SUM(prix * qte) AS chiffre_affaires
FROM Sales
GROUP BY region;