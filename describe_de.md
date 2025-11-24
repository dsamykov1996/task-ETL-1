# 📘 Projektbeschreibung

## ✔ Was wurde gemacht
Im Rahmen der Datenanalyse und -bereinigung wurden folgende Schritte durchgeführt:

1. Laden des Rohdatensatzes und erste Übersicht:
   - `head()`, `info()`, `describe()`
   - Analyse von fehlenden Werten und Duplikaten
   - Überprüfung der Spaltenstruktur

2. Datenbereinigung:
   - Entfernen von überflüssigen Leerzeichen, Vereinheitlichung von Textfeldern
   - Umwandlung der E-Mail-Adressen in Kleinbuchstaben
   - Bereinigung der Telefonnummern (nur Ziffern + optionales „+“)
   - Vereinheitlichung der Schreibweise von Namen, Städten und Adressen

3. Feature Engineering:
   - Erstellung von `full_name` aus Vor- und Nachname
   - Extraktion von `email_domain` aus der E-Mail-Adresse
   - `city_length` — Länge des Stadtnamens
   - `is_gmail` — Kennzeichnung von Gmail-Nutzern

4. Datenauswahl und Stichproben:
   - Auswahl der Gmail-Nutzer
   - Filterung von Unternehmen mit „LLC“ oder „LTD“
   - Positionsbasierte Auswahl über `iloc`
   - Zufallsstichproben über `sample`

5. Gruppierung und Statistik:
   - Anzahl der Personen pro Stadt
   - Anzahl der eindeutigen E-Mail-Domains pro Stadt
   - TOP-5 Städte
   - TOP-5 E-Mail-Domains
   - Aggregation mittels `groupby()` und `agg()`

6. Export der Ergebnisse:
   - `cleaned.csv` — bereinigter Datensatz
   - `gmail_users.csv` — Gmail-Nutzer
   - `tops.xlsx` — Excel-Datei mit zwei Tabellenblättern (Top-Städte und Domains)

---

## ⚠ Gefundene Probleme im Datensatz
Während der Analyse wurden folgende Probleme festgestellt:

- uneinheitliche Textformate (Groß/Kleinschreibung, Leerzeichen)
- unterschiedliche Formate der E-Mail-Adressen
- Telefonnummern mit Sonderzeichen oder Text
- einzelne fehlende Werte
- mögliche doppelte Einträge
- uneinheitliche Bezeichnungen von Städten und Unternehmen

---

## ⭐ Wichtigste Transformationen
- Standardisierung von Textfeldern → bessere Gruppierung  
- Bereinigung der Telefonnummern → einheitliches Format  
- Extraktion von `email_domain` → erleichtert Domain-Analysen  
- Hinzufügen von `is_gmail` → schnelle Segmentierung  
- Aggregation mit `agg()` → mehrere Kennzahlen gleichzeitig  

---

## 🔍 Interessante Erkenntnisse
- Gmail ist der am häufigsten verwendete E-Mail-Anbieter.
- Einige Städte enthalten den Großteil der Einträge (TOP-5).
- Unternehmen mit „LLC“ oder „LTD“ häufen sich in bestimmten Regionen.
- Die Länge der Städtenamen wirkt konsistent — keine Ausreißer.
- E-Mail-Domain-Segmentierung eignet sich gut für Marketinganalysen.

---

## 🚀 Verbesserungsmöglichkeiten für die Zukunft
1. Einsatz der Bibliothek `phonenumbers` für bessere Validierung.
2. Normalisierung von Städtenamen (z. B. Kiew/Kyiv).
3. Hinzufügen von Geodaten für Kartenvisualisierungen.
4. Tiefere Analyse der E-Mail-Domain-Muster.
5. Erkennung von Anomalien oder ungewöhnlichen Einträgen.
6. Aufbau einer automatisierten Datenverarbeitungspipeline.