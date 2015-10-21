### String
* `var s = "audacity"`
* `s = s[1].toUpperCase() + s.slice(2)` //Equals "Udacity"
* [String Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)


### Boolean
* Falsey => false, 0,"",null, undefined, NaN
* Truthy => true, Non zero numbers, "strings", objects, arrays,functions
* [Truthy and Falsey](http://www.sitepoint.com/javascript-truthy-falsy/)

### Array
* `var myArray = ["Euler", 3.141, {name : "Tarun", job : "Course Developer"}, myFunc]` // we can have a mixed array
* append will add an element at the end of array.
* `var skills = ["A", "B", "C"]` `$("#main").append(skills)` => It will append as "ABC"
* [Array Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
* `array.join(" ")` => To join elements of an array seperated by space character.


### Objects
* There are no classes in java script.
* `var myObj = {}` => Empty obj
* They are defined by key value paris. `var myResume = {"name" :"Tarun", "age" : 34, "skills" : ["A", "B", "C"]}`
* To access use `$("#main").append(myResume.name)`
* They are like python dictionaries . See the [link](http://stackoverflow.com/questions/20987485/python-dictionaries-vs-javascript-objects) for the differences.
* To add properties to objects use `myResume.city = "Pune India"`. Notice that we dint used var as we are adding properties to a object not adding variable. Also we can use the bracket notation like `myResume["email"] = "a@b.com"`
* [Difference btw dot and bracket notation](http://www.dev-archive.net/articles/js-dot-notation/)
* [Equality and Inequality Comparison](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness)

