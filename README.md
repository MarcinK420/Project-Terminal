Projekt własnej implementacji powłoki systemowej (shell) napisany w Pythonie. Program imituje podstawowe zachowania Basha, oferując wsparcie dla wbudowanych komend, potoków, przekierowań oraz autouzupełniania.

Funkcje
Wbudowane komendy: echo, pwd, cd, type, exit.

Autouzupełnianie (TAB): Dynamiczne podpowiadanie komend z $PATH oraz ścieżek plików/katalogów w bieżącym folderze.

Potoki (Pipes): Możliwość łączenia komend za pomocą | (np. cat file.txt | grep "coś").

Przekierowania:

Standardowe wyjście: > oraz >> (nadpisanie/dopisanie).

Błędy (stderr): 2> oraz 2>>.

Historia komend:

Zapisywana automatycznie do ~/.shell_history.

Wsparcie dla flag: history -r (odczyt), -w (zapis), -a (dopisanie).

Zarządzanie procesami: Podstawowa obsługa zadań w tle za pomocą &.

Obsługa cudzysłowów: Poprawne parsowanie argumentów dzięki modułowi shlex.

Struktura projektu
Aplikacja została podzielona na moduły dla lepszej czytelności:

main.py – Główna pętla REPL i dispatcher komend.

filename_completion.py – Logika autouzupełniania (wykorzystuje bibliotekę readline).

pipeline.py – Obsługa potoków i komunikacji między procesami.

redirection.py – Obsługa przekierowań strumieni do plików.

history.py – Zarządzanie historią i plikiem .shell_history.

navigation.py – Implementacja cd i pwd.

quoting.py – Obsługa komend echo i cat z uwzględnieniem argumentów.

Jak to odpalić?
Upewnij się, że masz Pythona 3.x.

(Opcjonalnie) Shell najlepiej działa na systemach Unixowych (Linux/macOS) ze względu na bibliotekę readline.

Uruchom plik główny:

Bash
python3 main.py
Przykłady użycia
Nawigacja i pliki:

Bash
$ cd /home/user/Documents
$ pwd
/home/user/Documents
$ cat plik.txt
Potoki i przekierowania:

Bash
$ echo "test" > output.txt
$ cat output.txt | type echo
echo is a shell builtin
Historia:

Bash
$ history 5  # pokaże 5 ostatnich komend
$ history -w backup_history.txt
Do zrobienia (TODO)
[ ] Pełna obsługa sygnałów (np. Ctrl+C nie powinno zamykać całego shella).

[ ] Implementacja komendy jobs (obecnie to tylko placeholder).

[ ] Bardziej zaawansowana obsługa zmiennych środowiskowych.

Projekt stworzony w celach edukacyjnych, aby zrozumieć jak pod spodem działają strumienie systemowe i procesy.
