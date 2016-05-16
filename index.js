/**
 * Created on 2016/5/14.
 */
function graph1(){
    var margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    var formatDate = d3.time.format("%Y-%m-%d");
    var obj = {};
    var startTime = new Pikaday({ field: document.getElementById('startTime')});
    var endTime = new Pikaday({ field: document.getElementById('endTime')});
    function load(name,flag){
        obj = {};
        d3.csv("data/" + name, function(error, d) {
            if (error) throw error;
            d.forEach(function (d) {
                obj[d.date.slice(0,8)] = typeof obj[d.date.slice(0,8)] === 'undefined'?0:obj[d.date.slice(0,8)]+= parseInt(d.value);
            });
            var data = [];
            for(var i in obj){
                data.push({
                    date:i,
                    value:obj[i]
                });
            }
            for(var i in data){
                data[i].date = formatDate.parse(data[i].date.slice(0,4)+"-"+data[i].date.slice(4,6)+"-"+data[i].date.slice(6,8));
            }
            if(flag){
                startTime.setDate(d3.min(data, function (d) {return d.date}));
                endTime.setDate(d3.max(data, function (d) {return d.date}));
            }

            startTime.setMinDate(d3.min(data, function (d) {return d.date}));
            startTime.setMaxDate(d3.max(data, function (d) {return d.date}));
            endTime.setMinDate(d3.min(data, function (d) {return d.date}));
            endTime.setMaxDate(d3.max(data, function (d) {return d.date}));
            var start = startTime.getDate();
            var end = endTime.getDate();
            data = data.filter(function (item,index,arrty) {
                return item.date >= start && item.date<=end;
            });

            render(data);

        });
    }
    function render(data){
        var svg = d3.select("#svg1")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
        var x = d3.time.scale()
            .range([0, width])
            .domain(d3.extent(data, function(d) { return d.date;}));
        var y = d3.scale.linear()
            .range([height, 0])
            .domain([0, d3.max(data, function(d) { return d.value; })]);
        var xAxis = d3.svg.axis()
            .scale(x)
            .orient("bottom")
        var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left");
        svg.append("g")
            .attr('class', 'axis')
            .attr('transform', 'translate(0,' + height + ')')
            .call(xAxis)
            .append('text')
            .text('date')
            .attr('transform', 'translate(' + width + ', 0)');

        svg.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text("Count ");
        var line = d3.svg.line()
            .x(function(d) { return x(d.date); })
            .y(function(d) { return y(d.value); })
            .interpolate('monotone');

        var path = svg.append('path')
            .attr('class', 'line')
            .attr('d', line(data));
        var g = svg.selectAll('circle')
            .data(data)
            .enter()
            .append('g')
            .append('circle')
            .attr('class', 'linecircle')
            .attr('cx', line.x())
            .attr('cy', line.y())
            .attr('r', 3.5)
            .on('mouseover', function() {
                d3.select(this).transition().duration(500).attr('r', 5);
            })
            .on('mouseout', function() {
                d3.select(this).transition().duration(500).attr('r', 3.5);
            });
    }
   // load('hour_taxi.csv',true);
    load('trip_count_all.csv',true);  //the data file for taxi and time
    var reload = function () {
        d3.selectAll("#svg1 > *").remove();
        var selectValue = document.getElementById('first-type').value;
        var type = ['trip_count_all.csv ','hour_citibike.csv']; //the data file of taxi, citibike time file
        load(type[selectValue],false);
    };
    d3.select('#first-type').on('change', reload);
    d3.select('#change1').on('click',reload);
}
function graph2(){
    var margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;
    var startTemp = document.getElementById('startTemp');
    var endTemp = document.getElementById('endTemp');

    startTemp.addEventListener("change",function(){
        d3.select('#startSpan').text(startTemp.value);
    });
    endTemp.addEventListener('change', function () {
        d3.select('#endSpan').text(endTemp.value);
    });
    function load(name,flag){
        d3.csv("data/" + name, function(error, d) {
            var data = [];
            d.forEach(function (d) {
                data.push({
                    temp: parseInt(d.temp),
                    value: parseInt(d.value)
                });
            });
            if (error) throw error;
            startTemp.setAttribute('min',d3.min(data,function(d){return d.temp;}));
            startTemp.setAttribute('max',d3.max(data,function(d){return d.temp;}));
            endTemp.setAttribute('min',d3.min(data,function(d){return d.temp;}));
            endTemp.setAttribute('max',d3.max(data,function(d){return d.temp;}));
            if(flag){
                startTemp.value = d3.min(data,function(d){return d.temp;});
                endTemp.value = d3.max(data,function(d){return d.temp;});
                d3.select('#startSpan').text(startTemp.value);
                d3.select('#endSpan').text(endTemp.value);
            }
            var start = startTemp.value;
            var end = endTemp.value;
            data = data.filter(function (item,index,arrty) {
                return item.temp>=start && item.temp<=end;
            });
            console.log("data2"+data);
            render(data);

        });
    }
    function render(data){
        var svg = d3.select("#svg2")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
        var x = d3.scale.linear()
            .range([0, width])
            .domain(d3.extent(data, function(d) { return d.temp;}));
        var y = d3.scale.linear()
            .range([height, 0])
            .domain([0, d3.max(data, function(d) { return d.value; })]);
        var xAxis = d3.svg.axis()
            .scale(x)
            .orient("bottom")
        var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left");
        svg.append("g")
            .attr('class', 'axis')
            .attr('transform', 'translate(0,' + height + ')')
            .call(xAxis)
            .append('text')
            .text('temp')
            .attr('transform', 'translate(' + width + ', 0)');

        svg.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text("Count ");
        var line = d3.svg.line()
            .x(function(d) { return x(d.temp); })
            .y(function(d) { return y(d.value); })
            .interpolate('monotone');

        var path = svg.append('path')
            .attr('class', 'line')
            .attr('d', line(data));

        var g = svg.selectAll('circle')
            .data(data)
            .enter()
            .append('g')
            .append('circle')
            .attr('class', 'linecircle')
            .attr('cx', line.x())
            .attr('cy', line.y())
            .attr('r', 3.5)
            .on('mouseover', function() {
                d3.select(this).transition().duration(500).attr('r', 5);
            })
            .on('mouseout', function() {
                d3.select(this).transition().duration(500).attr('r', 3.5);
            });
    }
    load('temp_taxi.csv',true);   //weather and taxi data
    var reload = function () {
        d3.selectAll("#svg2 > *").remove();
        var selectValue = document.getElementById('second-type').value;
        var type = ['temp_taxi.csv','temp_bike.csv'];//weather join taxi/weather join citibike data
        load(type[selectValue],false);
    };
    d3.select('#second-type').on('change', reload);
    d3.select('#change2').on('click',reload);
}


function addLoadEvent(func) {
    var oldonload = window.onload;
    if (typeof window.onload != 'function') {
        window.onload = func;
    } else {
        window.onload = function() {
            oldonload();
            func();
        }
    }
}
addLoadEvent(graph1);
addLoadEvent(graph2);
