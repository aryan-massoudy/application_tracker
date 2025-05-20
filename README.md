Projekt Dokumentation: Internship Tracker

Ziel:
Eine einfache Web-App zur Verwaltung von Bewerbungen für Praktika/Jobs.
Nutzer koennen ihren Bewerbungsstatus tracken (z. B. "Beworben", "Interview", "Abgelehnt", "Angebot").

Funktionen:
- Benutzerverwaltung
  - Registrierung & Login
  - Persoenliche Dashboard-Ansicht
- Bewerbungs-Tracking
  - Neue Bewerbungen erfassen
  - Status aktualisieren (Beworben -> Interview -> Angebot usw.)
  - Notizen, Links und Kontakt-Emails speichern
- Uebersichtliche Darstellung
  - Farbliche Markierung je nach Status
  - Statistik: Wie viele Bewerbungen in welchem Status
  - Liste aller Bewerbungen mit Filter- und Suchoptionen (via Admin-Bereich)

Technik:
- Backend: Django (Python)
- Frontend: HTML + Bootstrap (kein JavaScript!)
- Datenbank: SQLite (Standard bei Django)

Wie starten?

Projekt installieren:
pip install django crispy-forms crispy-bootstrap5
python manage.py migrate
python manage.py createsuperuser

Server starten:
python manage.py runserver

Im Browser: http://localhost:8000

Fuer Entwickler:
Erweiterbar um:
- Erinnerungen (z. B. fuer Follow-ups)
- PDF-Uploads (Anschreiben/Lebenslauf)
- Export als CSV/PDF

Ein minimalistisches Tool fuer weniger Chaos im Bewerbungsprozess!
Bei Fragen: Einfach melden!
