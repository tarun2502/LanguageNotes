### Good Links
* [understanding computer bits and ram](https://www.udacity.com/course/viewer#!/c-cs101/l-48727569/m-48658928)
[Link2](https://www.udacity.com/course/viewer#!/c-cs101/l-48727569/m-48738019)
[Link3](https://www.udacity.com/course/viewer)
### Lists

* Sequence of anything => p = ["tarun", 25, 5.25]
* To access elements => p[1] = 25
* This returns a list => p[0:2] = ["tarun", 25]
* General Grammer => <list> = [<expression>, <expression>]
* Empty List => p = []
* List inside a list =>mixed list = ['apple', 3, 'oranges',27, [1, 2['alpha','beta']]]
* Another example => beatles = [['John', 1940],['Paul', 1942],['George', 1943], ['Ringo', 1943]]

* Another example => beatles = [['John', 1940],['Paul', 1942],['George', 1943], ['Ringo', 1943]]
* You can mutuate lists but can not mutuate strings. Like s = "Hello", 
s  = "Yello", so Yello is altogether a different string. Now we are reffering it with variable s. We can no longer refer "Hello". Similary when we add two strings like "Hello" + "w" -> A new string "w" is created and then a altogether new string "Hellow" is created. 
* [Good Explanation](https://www.udacity.com/course/viewer#!/c-cs101/l-48727569/m-48532662)

* p = ['H', 'E','L'] => p[0] = 'Y' => print p

* q = p => q[0] = 'T' => p = ['T', 'E', 'L']

* List Append 
  * <list>.append(<elem>) => You are mutating the list its invoked on. Eleement is added at the end.
  * p = [1, 2, 3] => p.append(4) => p = [1,2,3,4]
* List Length = len(<list>)
