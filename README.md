

CB allows some HTML in the **About me** and **Wishlist** profile fields. You can only use this HTML tags: `a p i strong b u ul ol li h1 h2 h3 img font br span` with inline stylesheets (`style=` attribute).
For easier development, however, normal CSS selectors are used and embedded at the end with some tool.

For example https://github.com/Stranger6667/css-inline

``` 
cargo install css-inline
css-inline index.html --load-remote-stylesheets
```