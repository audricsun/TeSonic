$(function () {

	$('#productDetailChart').highcharts({

	    chart: {
	        polar: true,
	        type: 'line'
	    },

	    title: {
	        text: 'Product Status',
	        x: +30
	    },

	    pane: {
	    	size: '85%'
	    },

	    xAxis: {
	        categories: ['Cover', 'Delay', 'Request', 'Quality',
	                'Stable', 'Agile'],
	        tickmarkPlacement: 'on',
	        lineWidth: 0
	    },

	    yAxis: {
	        gridLineInterpolation: 'polygon',
	        lineWidth: 0,
	        min: 0,
	        max: 100
	    },

	    tooltip: {
	    	shared: true,
	        pointFormat: '<span style="color:{series.color}">{series.name}: <b>{point.y:,.0f}%</b><br/>'
	    },

	    legend: {
	        align: 'right',
	        verticalAlign: 'top',
	        y: 70,
	        layout: 'vertical'
	    },

	    series: [{
	        name: 'Average',
	        data: [70, 90, 90, 90, 97, 95],
	        pointPlacement: 'on'
	    }, {
	        name: 'Current',
	        data: [50, 60, 80, 70, 90, 65],
	        pointPlacement: 'on'
	    }]

	});
});
