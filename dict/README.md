# Dictionaries (EN, PL) on Linux Mint/Ubuntu

Install `aspell` and English dictionary

```
$ apt install aspell aspell-en
```

Install `aspell` and Polish dictionary

```
$ apt install aspell aspell-pl
```

The same way you can install dictionary for other languages.

```
$ apt search aspell
```

---

Create list of Polish words (with variations)

```
$ aspell -d pl dump master \
  | aspell -l pl expand \
  | sed "s/ \+/\n/g" \
  | tr '[:upper:]' '[:lower:]' \
  | sort \
  | uniq \
  | grep -v "'s" \  
  > dict-pl.txt
```

Create list of Polish words (without variations)

```
$ aspell -d pl dump master \
  | sed "s/ \+/\n/g" \
  | tr '[:upper:]' '[:lower:]' \
  | sort \
  | uniq \
  | grep -v "'s" \  
  > dict-pl.txt
```

English dictionary needs `grep -v "'s"` to skip words with `'s` at the end.


Split words by length

```  
$ egrep '^.{4}$' dict-pl.txt > dict-pl-4.txt
$ egrep '^.{5}$' dict-pl.txt > dict-pl-5.txt
$ egrep '^.{6}$' dict-pl.txt > dict-pl-6.txt
```

---

Source:
- [How to convert aspell dictionary to simple list of words?](https://superuser.com/questions/137957/how-to-convert-aspell-dictionary-to-simple-list-of-words)
- [How to convert a string to lower case in Bash?](https://stackoverflow.com/questions/2264428/how-to-convert-a-string-to-lower-case-in-bash)


