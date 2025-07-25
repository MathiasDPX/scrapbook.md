# scrapbook.md

GitHub README add-on to embed a [scrapbook](https://scrapbook.hackclub.com/) post in README. Made for [REAMDE](https://github.com/idksarah/REAMDE)

## Example

You can find an update script in `.github\workflows\update_scrapbook.yml`

### Latest post
[![Scrapbook post](https://scrapbook.mathias.hackclub.app/latest-post/mathias?v=0&update=1)](https://scrapbook.hackclub.com/mathias)

```markdown
[![Scrapbook post](https://scrapbook.mathias.hackclub.app/latest-post/mathias?v=0&update=1)](https://scrapbook.hackclub.com/mathias)
```

### Specific post
You can add a `v` parameter in the url to tell scrapbook.md to exclude every post after this timestamp

[![Scrapbook post](https://scrapbook.mathias.hackclub.app/latest-post/mathias?v=1751973575)](https://scrapbook.hackclub.com/mathias)

```markdown
[![Scrapbook post](https://scrapbook.mathias.hackclub.app/latest-post/mathias?v=1751973575)](https://scrapbook.hackclub.com/mathias)
```