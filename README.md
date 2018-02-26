# frontyardprojects.github.io
the official website for frontyard projects inc.

## Updating the website

### Updating the BreathingSpace information

![screen shot 2018-02-27 at 10 22 09 am](https://user-images.githubusercontent.com/1239550/36701901-1d58fec8-1ba9-11e8-93e0-ace00bf30411.png)

The [BreathingSpace chart and text](http://www.frontyardprojects.org/#moneygraph) is based on the data in [_data/_money.yml file](https://github.com/frontyardprojects/frontyardprojects.github.io/blob/master/_data/money.yml).

To update the chart, [edit _data/_money.yml](https://github.com/frontyardprojects/frontyardprojects.github.io/edit/master/_data/money.yml) to add a new month’s entry to the top of the list, following the formatting of the existing entries:

```
- value: 8.46
  date: 29/1/2018
- value: 10.49
  date: 31/12/2017
- value: 10.12
  date: 30/11/2017
```

## development

To hack on this site make sure you have [Jekyll installed](https://jekyllrb.com/docs/installation/):

    gem install jekyll

Then run:

    jekyll serve
