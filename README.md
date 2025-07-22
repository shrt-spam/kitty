# Kitty's CB profile

# dev notes
CB allows some HTML in the **About me** and **Wishlist** profile fields. You can only use this HTML tags: `a p i strong b u ul ol li h1 h2 h3 img font br span` with inline stylesheets (`style=` attribute).
For easier development, however, normal CSS selectors are used and embedded at the end with some tool.

For example https://github.com/Stranger6667/css-inline

``` 
cargo install css-inline
css-inline index.html --load-remote-stylesheets --base-url "https://shrt-spam.github.io/kitty/"
```



Maunal patches:

remove html, body and head tags. Move the :root stuff to main container.

add urls

```
sed -i 's|./img/|https://shrt-spam.github.io/kitty/img/|g' inlined.index.html
```

remove newlines:

```
cargo install minhtml
minhtml --output inlined.index.min.html --keep-closing-tags inlined.index.html
```


