# Film Manager

Film Manager adalah aplikasi untuk mengelola film-film yang anda tonton, selain itu aplikasi ini juga menghadirkan fitur rekomendasi film untuk teman anda berdasarkan genre dari film yang sudah pernah anda tonton.

Film Manager menghadirkan fitur-fitur utama, yaitu:
- Watched film list (title, director, genre, release year, & rating)
- Add new film
- Delete film
- Update rating
- Get recommendations (by genre)

# Data Structures & Algorithm

Kami menggunakan beberapa struktur data di aplikasi ini, yaitu:

1. Hashmap/Hash Table, untuk menyimpan data film.
2. Array (List), untuk mengelola film.
3. Quick Sort, untuk mengurutkan list film berdasarkan rating tertinggi.

# Systems
Pada aplikasi Film Manager ini, kami menggunakan **Shelve** untuk _database_ dan **PySimpleGuiQt** untuk _GUI_.
___
**Kenapa lebih memilih _PySimpleGui_?**

Alasan kami memilih _library **PySimpleGuiQt**_ (Qt-based) dari pada library lain seperti **Tkinter** atau **PyQt5** adalah karena penggunaannya yang simpel & mudah tapi menghasilkan tampilan yang clean dan modern (seperti Qt), ini cocok digunakan untuk project dengan waktu deadline yang relatif pendek dan butuh waktu pengerjaan yang cepat.

___
**Kenapa menggunakan _Shelve_ untuk mengelola database (.db)?**

_**Shelve**_ adalah library untuk mengelola database (.db) yang mudah digunakan dan berbasis **Hashmap/Hash Table**, karena itu kami memmilih ini. Dengan struktur data **Hashmap**, maka untuk sistem pencarian akan mudah dan cepat karena memiliki kompleksitas O(1).


## Installation

```bash
python -m pip install PySimpleGUIQt
```

## Import
```python
import PySimpleGuiQt as qt
import shelve
```
