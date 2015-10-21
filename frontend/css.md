## Main principles
* If style is not defined then browser uses default styles.
* In the start you can use placeholders to determine instead of actual content. Like
`<div>text</dev> ` or `<div>image</div>`
* Most specific rule apply in case of css. Like a National rule or a state rule or a house rule.
* Styling can be done at these places.
  * the default style of a browser (different browsers have slightly different styles)
  * stylesheet in a separate file (this is what you will be mostly using)
  * stylesheet inside HTML (this can be done for small projects but is not ideal)
  * inline style in an element (this can also be done but should be avoided)
* "Cascading" means that rules are applied not only to the elements they directly match, but also to all of those elements' child elements. However, if a child element has multiple, overlapping rules defined for it, the more specific rule takes effect.
* Element width = Content width + padding + Border width.
* Padding = Box around content.
* Border = Box around padding.
* Margin = Box around border.
* `* {box-sizing:border-box;}` => This makes element size equal to content + border + padding. This way we can set the total width of box and all individual sizes will adjust.
* For above use `-webkit-box-sizing`, `-moz-box-sizing`, `-ms-box-sizing` as per the browser. Since they are developed recently so we have to add browser specifc specification.
* Use percentage as it is based on the page size. Fixed pixel sizes may lead to bad user experience.
* Can also set max-width which will make the box no more than the given max-widht.
* Generally to keep images on left and text on the right. As people read from left to right. So image will capture the attention first.
* Responsive design => Website works same on all the different screens.Page is going to resize automatically.
* We need to create row of 100% page width and column of 1/12-12/12 page width. 1/12=8.33%, 2/12=16.66%, 12/12=100%. Row can be named as .row and column can be named as col-1 to col-12 being 1 column to 12 column wide.
* overflow=auto => to add the slider to the page and not allow the text to overflow.
* Media Queries => Change page css properties depending upon device, screen size and color.

### class
.classname{
color:red;
}



## Links to Read
* [CSS Selectors](https://css-tricks.com/how-css-selectors-work/)
* [Because these rules differ sometimes between browsers, there are efforts to promote consistency in styles across browsers. One popular solution to this issue is using what is referred to as a CSS reset such as normalize.css.](http://necolas.github.io/normalize.css/)
* [CSS Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)
* [Default style rule by browsers](http://www.w3.org/TR/CSS21/sample.html)
* [Box Model](http://assignments.udacity-extras.appspot.com/courses/html-css/samples/box-model.html)
* [Guide to flex boxes](http://css-tricks.com/snippets/css/a-guide-to-flexbox/)
* [To verify HTML: ](http://validator.w3.org/#validate_by_input)
* [To verify CSS: ](http://jigsaw.w3.org/css-validator/#validate_by_input)
* [Flex](https://developer.mozilla.org/en-US/docs/Web/CSS/flex)
* [Flex Wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap)
* [Flex Boxes](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
* [Chrome Device Emulator](https://developer.chrome.com/devtools/docs/device-mode)
* [Place Holder images](http://placekitten.com/200/200)
* [Place holder](http://placehold.it)
* [Google Fonts](https://www.google.com/fonts)
* [Udacity style sheet guide](http://udacity.github.io/frontend-nanodegree-styleguide/)
* [Process for bootstrap](https://www.udacity.com/course/viewer#!/c-ud304/l-2794148535/m-2788768642)
* [Css](http://docs.webplatform.org/wiki/css)
* [DOM css properties reference](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference)
* [Style using DOM](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style)
