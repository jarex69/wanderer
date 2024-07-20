import os
import re

def replace_in_files(directory, old_word, new_word):
    print(f"Rozpoczynam przeszukiwanie i zamianę w katalogu: {directory}")
    file_count = 0
    modified_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Sprawdzamy, czy słowo występuje w pliku
                if re.search(r'\b' + re.escape(old_word) + r'\b', content, re.IGNORECASE):
                    # Zamieniamy słowo, zachowując wielkość liter
                    new_content = re.sub(r'\b' + re.escape(old_word) + r'\b', 
                                         lambda m: new_word if m.group(0).islower() else new_word.capitalize(), 
                                         content, 
                                         flags=re.IGNORECASE)
                    
                    # Zapisujemy zmiany tylko jeśli coś zostało zmienione
                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Zmodyfikowano plik: {file_path}")
                        modified_count += 1
                
                file_count += 1
            
            except (UnicodeDecodeError, FileNotFoundError, PermissionError) as e:
                print(f'Błąd przetwarzania {file_path}: {e}')

    print(f"\nStatystyki:")
    print(f"Przeszukanych plików: {file_count}")
    print(f"Zmodyfikowanych plików: {modified_count}")

# Użycie funkcji
replace_in_files('src', 'wanderer', 'VisitGlacensis.pl')