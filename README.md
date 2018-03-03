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

## Updating the monthly donors records

![screen shot 2018-02-27 at 10 21 24 am](https://user-images.githubusercontent.com/1239550/36701902-1d924dea-1ba9-11e8-977d-fbd4d2f77bad.png)

The monthly donors information is fed from the data in the [files in /_supporters](https://github.com/frontyardprojects/frontyardprojects.github.io/tree/master/_supporters). There is a file for each month, named `$sequential_month_number.$month_name.md`, e.g. [`01.march.md`](https://github.com/frontyardprojects/frontyardprojects.github.io/blob/master/_supporters/01.march.md) for the first month and [`24.february.md`](https://github.com/frontyardprojects/frontyardprojects.github.io/blob/master/_supporters/24.february.md) for february in Frontyard’s second year.

Each file has a [YAML statement](https://en.wikipedia.org/wiki/YAML). It states the `month` this file represents, then the items covered. Each item entry states the name of the item (`item`), its value (`value`), and the name of the donor who covered it (`name`):

```
---
month: February 2018
covered:
  - item: Internets
    value: 65
    name: 
  - item: Rent
    value: 30
    name: 
  - item: 100% renewably powered lights
    value: 50
    name: circle square paper
  - item: 100% renewable computer power
    value: 50
    name: T Malott
  - item: Water
    value: 50
    name: Andrew Fedorovitch
  - item: Fresh food for residents
    value: 50
    name: 
  - item: Workshop supplies
    value: 40
    name: Anonymous
  - item: Cuppas
    value: 20
    name: 
  - item: Risograph paper and ink
    value: 50
    name: circle square paper
  - item: Special public liability funds
    value: 635
    name: 
---
```

To update an existing month, amend exiting entries or add new entries to the file for that month.

To add a new month’s data, [create a new file in the /_supporters directory](https://github.com/frontyardprojects/frontyardprojects.github.io/new/master/_supporters), with the correct name and YAML formatted entries.


## development

To hack on this site make sure you have [Jekyll installed](https://jekyllrb.com/docs/installation/):

    gem install jekyll

Then run:

    jekyll serve
