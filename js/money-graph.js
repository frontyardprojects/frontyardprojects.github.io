(function () {

  function ready(fn) {
    if (document.readyState != 'loading'){
      fn();
    } else if (document.addEventListener) {
      document.addEventListener('DOMContentLoaded', fn);
    } else {
      document.attachEvent('onreadystatechange', function() {
        if (document.readyState != 'loading')
          fn();
      });
    }
  }

  ready(drawGraph);

  function drawGraph() {
    var parseTime = d3.timeParse("%d/%m/%Y");
    var data = frontyardMoney.map(function(v, i) {
        return {
          value: v.value,
          date: parseTime(v.date)
        };
      }).reverse();

    var svg =
      d3.select("div#moneygraph svg")
        .attr("preserveAspectRatio", "xMinYMin meet")
        .attr("viewBox", "0 0 600 100")
        .classed("svg-content", true),
      margin = {top: 5, right: 50, bottom: 4, left: 10},
      width = 600 - margin.left - margin.right,
      height = 100 - margin.top - margin.bottom;

    svg.selectAll("*").remove();
    var g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");


    var x = d3.scaleTime()
        .rangeRound([0, width])
        .domain(d3.extent(data, function(d) { return d.date; }));

    var y = d3.scaleLinear()
        .rangeRound([height, 0])
        .domain([0, d3.max(data, function(d) { return d.value; })])
        .nice();

    var line = d3.line()
        .x(function(d) { return x(d.date); })
        .y(function(d) { return y(d.value); });

    // g.append("g")
    //   .attr("transform", "translate(0," + height + ")")
    //   .call(d3.axisBottom(x))

      g.append("g")
        .attr("transform", "translate( " + width + ", 0 )")
        .call(d3.axisRight(y)
          .ticks(2)
          .tickFormat(function(d) { return '$'+d3.format(",")(d); })
        );
      // .append("text")
      //   .attr("fill", "#000")
      //   .attr("transform", "rotate(-90)")
      //   .attr("y", 6)
      //   .attr("dy", "0.71em")
      //   .attr("text-anchor", "end")
      //   .text("Price ($)");

    g.append("path")
      .datum(data)
      .attr("fill", "none")
      .attr("stroke", "black")
      .attr("stroke-linejoin", "round")
      .attr("stroke-linecap", "round")
      .attr("stroke-width", 2.5)
      .attr("d", line);

    g.append("text")
     .attr("fill", "#000")
     .attr("y", 10)
     .style("font-weight", "bold")
     .text("Our bank balance over time");
  }
})()
