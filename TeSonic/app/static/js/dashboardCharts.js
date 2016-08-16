$(function () {
    $('#dashboardChartContainer').highcharts({
        title: {
            text: 'Product Dashboard Chart',
            x: -20 //center
        },
        subtitle: {
            text: 'Source: TeSonic',
            x: -20
        },
        xAxis: {
            categories: ['1 Jul', '2 Jul', '3 Jul', '5 Jul', '6 Jul', '7 Jul','8 Jul', '9 Jul', '10 Jul', '11 Jul', '12 Jul', '13 Jul']
        },
        yAxis: {
            title: {
                text: '用例通过率（%）'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }],
//            min: 0,
//            max: 100
        },
        tooltip: {
            valueSuffix: '%'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: '保险',
            data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 43.3, 68.3, 73.9, 95.6]
        }, {
            name: '基金',
            data: [0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.9, 30.1, 34.1, 38.6, 42.5]
        }, {
            name: 'P2P',
            data: [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 38.6, 57.9, 74.3, 90.0, 93.9, 100.0]
        }, {
            name: '交易所',
            data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 26.6, 34.2, 40.3, 66.6, 74.8]
        }]
    });
});